// Debug message
console.log("javascript.js loaded");

// Auto-hide messages after 5 seconds
setTimeout(function() {
    var messages = document.querySelector('.messages');
    if (messages) {
        messages.style.display = 'none';
    }
}, 5000); // milliseconds

// Confirm the user wishes to delete the record.
// If not - do nothing.
function confirmDeleteAndRedirect(url) {
    if (confirm("Are you sure you want to delete this task?")) {
        window.location.href = url;
    }
}

function toggleStatus(url) {
    window.location.href = url;
}