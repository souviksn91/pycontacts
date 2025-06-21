// static/js/auto-dismiss-flash.js

// Automatically dismiss flash messages after 5 seconds
document.addEventListener('DOMContentLoaded', function() {
    let flashMessages = document.querySelectorAll('.flash-message');

    flashMessages.forEach(function(message) {
        // Add the 'show' class to trigger the fade-in animation
        setTimeout(function() {
            message.classList.add('show');
        }, 10); // Small delay to ensure the transition works

        // Automatically dismiss the message after 5 seconds
        setTimeout(function() {
            message.classList.remove('show'); // Trigger fade-out
            setTimeout(function() {
                message.remove(); // Remove the message from the DOM after fading out
            }, 500); // Wait for the fade-out animation to complete
        }, 5000); // 5 seconds delay
    });
});