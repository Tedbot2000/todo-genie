// Auto-hide messages after 5 seconds
setTimeout(function() {
    var messages = document.querySelector('.messages');
    if (messages) {
        messages.style.display = 'none';
    }
}, 5000); // milliseconds



// Confirm the user wishes to delete the record.
// If not - do nothing.
let deleteUrl = ''; // used to redirect the user after they confirm deletion (in case of multiple pages)

function confirmDeleteAndRedirect(url) {
    deleteUrl = url;
    $('#confirmModal').modal('show');
}

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('confirmDeleteBtn').onclick = function() {
        window.location.href = deleteUrl;
    };
});

// Toggle status buttons
function toggleStatus(url) {
    window.location.href = url;
}