document.addEventListener('DOMContentLoaded', function() {
    // Select all links on the page
    const links = document.querySelectorAll('a');
    links.forEach(function(link) {
        link.addEventListener('click', function(event) {
            alert('Link clicked!');
        });
    });
});