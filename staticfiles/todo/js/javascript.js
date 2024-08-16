/*jshint esversion: 6, laxlet: true */
/*global setTimeout, document, $, window */

// Confirm the user wishes to delete the record.
var deleteUrl = ""; // used to redirect the user

function confirmDeleteAndRedirect(url) {
    deleteUrl = url;
    $("#confirmModal").modal("show");
}

document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("confirmDeleteBtn").onclick = function () {
        window.location.href = deleteUrl;
    };
});

// Auto-hide messages after 5 seconds
setTimeout(function () {
    var messages = document.querySelector(".messages");
    if (messages) {
        messages.style.display = "none";
    }
}, 5000); // milliseconds

// Toggle status buttons
function toggleStatus(url) {
    window.location.href = url;
}