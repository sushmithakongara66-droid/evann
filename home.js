// Check if user is logged in
const isLoggedIn = sessionStorage.getItem('isLoggedIn');
const username = sessionStorage.getItem('username');

if (!isLoggedIn || isLoggedIn !== 'true') {
    // Redirect to login page if not logged in
    window.location.href = 'index.html';
} else {
    // Display welcome message with username
    document.getElementById('welcomeUser').textContent = username;
}

// Logout functionality
document.getElementById('logoutBtn').addEventListener('click', function() {
    // Clear session
    sessionStorage.clear();
    
    // Redirect to login page
    window.location.href = 'index.html';
});
