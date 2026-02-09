# Evann - User Login Application

A simple and elegant user login application with a modern interface.

## Features

- **User Login**: Secure login form with username and password fields
- **Password Validation**: Minimum 6 characters required for passwords
- **Session Management**: User session persists during browsing
- **Logout Functionality**: Easy logout to clear session and return to login page
- **Responsive Design**: Modern, gradient-based UI that works on all devices

## Getting Started

### Running the Application

1. Clone this repository
2. Open `index.html` in your web browser, or serve it using a simple HTTP server:
   ```bash
   python3 -m http.server 8000
   ```
3. Navigate to `http://localhost:8000` in your browser

### Using the Application

1. Enter any username
2. Enter a password (must be at least 6 characters long)
3. Click "Login" to access the home page
4. Click "Logout" to return to the login page

## Files

- `index.html` - Login page
- `home.html` - Home page (displayed after successful login)
- `styles.css` - Styling for the application
- `login.js` - Login functionality and validation
- `home.js` - Home page functionality and logout

## Technical Details

- Pure HTML, CSS, and JavaScript (no frameworks required)
- Uses sessionStorage for client-side session management
- Client-side password validation (6 character minimum)
- Gradient-based modern UI design

## Note

This is a front-end demonstration application. In a production environment, authentication should be handled securely on the server-side with proper password hashing, HTTPS, and backend validation.