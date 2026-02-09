"""
Unit tests for the user registration feature.
"""
import unittest
import json
import os
import sys
from app import app, init_db, validate_email, validate_password, validate_username

# Add the parent directory to the path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))


class TestValidation(unittest.TestCase):
    """Test validation functions."""
    
    def test_validate_email(self):
        """Test email validation."""
        self.assertTrue(validate_email('user@example.com'))
        self.assertTrue(validate_email('test.user@domain.co.uk'))
        self.assertFalse(validate_email('invalid-email'))
        self.assertFalse(validate_email('@example.com'))
        self.assertFalse(validate_email('user@'))
    
    def test_validate_password(self):
        """Test password validation."""
        self.assertTrue(validate_password('password123'))
        self.assertTrue(validate_password('12345678'))
        self.assertFalse(validate_password('short'))
        self.assertFalse(validate_password('1234567'))
    
    def test_validate_username(self):
        """Test username validation."""
        self.assertTrue(validate_username('user123'))
        self.assertTrue(validate_username('abc'))
        self.assertTrue(validate_username('User1234567890'))
        self.assertFalse(validate_username('ab'))  # Too short
        self.assertFalse(validate_username('a' * 21))  # Too long
        self.assertFalse(validate_username('user@123'))  # Special chars


class TestUserRegistration(unittest.TestCase):
    """Test user registration endpoints."""
    
    def setUp(self):
        """Set up test client and database."""
        app.config['TESTING'] = True
        self.client = app.test_client()
        
        # Use a test database file
        import app as app_module
        self.test_db = 'test_users.db'
        app_module.DATABASE = self.test_db
        
        # Initialize the database
        init_db()
    
    def tearDown(self):
        """Clean up test database."""
        import app as app_module
        if os.path.exists(self.test_db):
            os.remove(self.test_db)
        app_module.DATABASE = 'users.db'  # Reset to default
    
    def test_index_page(self):
        """Test index page loads."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to Evann', response.data)
    
    def test_register_page_get(self):
        """Test registration page loads."""
        response = self.client.get('/register')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Create Account', response.data)
    
    def test_register_success_form(self):
        """Test successful user registration via form."""
        response = self.client.post('/register', data={
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'password123',
            'confirm_password': 'password123'
        }, follow_redirects=True)
        
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Registration successful', response.data)
    
    def test_register_password_mismatch(self):
        """Test registration with mismatched passwords."""
        response = self.client.post('/register', data={
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'password123',
            'confirm_password': 'different'
        })
        
        self.assertIn(b'Passwords do not match', response.data)
    
    def test_register_invalid_email(self):
        """Test registration with invalid email."""
        response = self.client.post('/register', data={
            'username': 'testuser',
            'email': 'invalid-email',
            'password': 'password123',
            'confirm_password': 'password123'
        })
        
        self.assertIn(b'Invalid email format', response.data)
    
    def test_register_weak_password(self):
        """Test registration with weak password."""
        response = self.client.post('/register', data={
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'short',
            'confirm_password': 'short'
        })
        
        self.assertIn(b'Password must be at least 8 characters', response.data)
    
    def test_register_invalid_username(self):
        """Test registration with invalid username."""
        response = self.client.post('/register', data={
            'username': 'ab',  # Too short
            'email': 'test@example.com',
            'password': 'password123',
            'confirm_password': 'password123'
        })
        
        self.assertIn(b'Username must be 3-20 alphanumeric characters', response.data)
    
    def test_api_register_success(self):
        """Test successful user registration via API."""
        response = self.client.post('/api/register',
            data=json.dumps({
                'username': 'apiuser',
                'email': 'api@example.com',
                'password': 'password123'
            }),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertEqual(data['message'], 'Registration successful')
        self.assertEqual(data['user']['username'], 'apiuser')
    
    def test_api_register_duplicate_user(self):
        """Test API registration with duplicate username."""
        # Register first user
        self.client.post('/api/register',
            data=json.dumps({
                'username': 'duplicate',
                'email': 'first@example.com',
                'password': 'password123'
            }),
            content_type='application/json'
        )
        
        # Try to register with same username
        response = self.client.post('/api/register',
            data=json.dumps({
                'username': 'duplicate',
                'email': 'second@example.com',
                'password': 'password123'
            }),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, 409)
        data = json.loads(response.data)
        self.assertIn('already exists', data['error'])
    
    def test_api_register_invalid_data(self):
        """Test API registration with invalid data."""
        response = self.client.post('/api/register',
            data=json.dumps({
                'username': 'ab',  # Too short
                'email': 'invalid',
                'password': 'short'
            }),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertIn('error', data)


if __name__ == '__main__':
    unittest.main()
