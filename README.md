# Evann - User Registration System

A simple Flask-based web application with user registration functionality.

## Features

- **User Registration Form**: Clean, modern web interface for user registration
- **Input Validation**: Comprehensive validation for username, email, and password
- **Password Security**: Passwords are hashed using Werkzeug's security functions
- **API Endpoint**: RESTful API for programmatic user registration
- **SQLite Database**: Simple database storage for user data
- **Responsive Design**: Mobile-friendly interface

## Requirements

- Python 3.7+
- Flask 3.0.0
- Werkzeug 3.0.1

## Installation

1. Clone the repository:
```bash
git clone https://github.com/sushmithakongara66-droid/evann.git
cd evann
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Running the Application

Start the Flask development server:
```bash
python app.py
```

The application will be available at `http://localhost:5000`

### Registration Form

Navigate to `http://localhost:5000/register` to access the registration form.

**Validation Rules:**
- Username: 3-20 alphanumeric characters
- Email: Valid email format
- Password: Minimum 8 characters
- Passwords must match

### API Endpoint

**POST /api/register**

Register a new user via API.

Request body (JSON):
```json
{
    "username": "testuser",
    "email": "test@example.com",
    "password": "password123"
}
```

Success response (201):
```json
{
    "message": "Registration successful",
    "user": {
        "id": 1,
        "username": "testuser",
        "email": "test@example.com"
    }
}
```

Error response (400/409):
```json
{
    "error": "Error message"
}
```

## Testing

Run the test suite:
```bash
python -m pytest test_app.py -v
```

Or using unittest:
```bash
python test_app.py
```

## Project Structure

```
evann/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── test_app.py           # Unit tests
├── README.md             # Documentation
├── .gitignore            # Git ignore rules
└── templates/            # HTML templates
    ├── base.html         # Base template
    ├── index.html        # Home page
    └── register.html     # Registration form
```

## Security Features

- Passwords are hashed using PBKDF2 SHA-256
- Input validation to prevent invalid data
- SQL injection protection through parameterized queries
- Unique constraints on username and email
- CSRF protection via Flask's session management

## Database Schema

```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## License

MIT License