document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.form-check-input').forEach(function(checkbox) {
        checkbox.addEventListener('change', function() {
            const todoId = this.getAttribute('data-id');
            const isChecked = this.checked;

            fetch(`/toggle_status/${todoId}/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
                },
                body: JSON.stringify({ status: isChecked })
            }).then(response => {
                if (!response.ok) {
                    // Handle error
                    console.error('Error toggling status');
                }
            }).catch(error => {
                console.error('Error:', error);
            });
        });
    });
});
