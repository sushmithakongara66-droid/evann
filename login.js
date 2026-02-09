// Simple login authentication
document.getElementById('loginForm').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const errorMessage = document.getElementById('errorMessage');
    
    // Clear previous error messages
    errorMessage.textContent = '';
    
    // Simple validation - in a real application, this would be done securely on the server
    // For demonstration purposes, we're using basic client-side validation
    // NOTE: This demo accepts ANY username with a password of 6+ characters
    if (username && password) {
        // Demo credentials (in production, this would be handled by backend)
        if (password.length >= 6) {
            // Store user session
            sessionStorage.setItem('isLoggedIn', 'true');
            sessionStorage.setItem('username', username);
            
            // Redirect to home page
            window.location.href = 'home.html';
        } else {
            errorMessage.textContent = 'Password must be at least 6 characters long';
        }
    } else {
        errorMessage.textContent = 'Please enter both username and password';
    }
});
