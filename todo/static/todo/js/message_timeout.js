// Auto-hide messages after 105 seconds
setTimeout(function() {
    var messages = document.querySelector('.messages');
    if (messages) {
        messages.style.display = 'none';
    }
}, 10000); // milliseconds
