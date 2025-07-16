document.getElementById('loginForm').addEventListener('submit', function(e) {
    var username = document.getElementById('username').value.trim();
    var password = document.getElementById('password').value.trim();
    var errorMsg = document.getElementById('errorMsg');
    errorMsg.style.display = 'none';
    if (!username || !password) {
        errorMsg.textContent = 'Both fields are required.';
        errorMsg.style.display = 'block';
        e.preventDefault();
    }
    
});
