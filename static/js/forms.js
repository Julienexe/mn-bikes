document.addEventListener('DOMContentLoaded', function() {
    const uploadButtons = document.querySelectorAll('.upload-button');

    uploadButtons.forEach(button => {
        button.addEventListener('click', function(event) {
            const fileInput = this.previousElementSibling;
            const file = fileInput.files[0];
            const fieldName = this.id;
            if (!file) {
                alert('Please select a file to upload.');
                return;
            }

            const formData = new FormData();
            formData.append('file', file);
            formData.append('field_name', fieldName);

            // Show loader
            this.textContent = 'Uploading...';
            this.classList.add('btn-loading');

            fetch('/update_lease/', {
                method: 'POST',
                body: formData,
                headers: {
                    'X-CSRFToken': getCookie('csrftoken')
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    this.textContent = 'Success';
                    this.className = 'btn btn-success btn-disabled';
                    if (data.missing == false){
                        document.location.reload(true);
                    }
                } else {
                    alert('File upload failed.');
                    console.error(data);
                    this.textContent = 'Upload';
                    this.classList.remove('btn-loading');
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('An error occurred while uploading the file.');
                this.textContent = 'Upload';
                this.classList.remove('btn-loading');
            });
        });
    });

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});