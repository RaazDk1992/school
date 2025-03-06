document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.file-input').forEach(input => {
        input.addEventListener('change', function(event) {
            const fileInput = event.target;
            const files = fileInput.files;
            const fileGrid = document.getElementById('fileGrid');
            
            // Clear any existing previews
            fileGrid.innerHTML = '';

            // Loop through selected files and generate preview
            Array.from(files).forEach(file => {
                const reader = new FileReader();
                
                reader.onload = function(e) {
                    const previewContainer = document.createElement('div');
                    previewContainer.classList.add('preview-container');
                    previewContainer.style.position = 'relative';

                    const imagePreview = document.createElement('img');
                    imagePreview.src = e.target.result;
                    imagePreview.classList.add('img-fluid', 'preview-img');
                    previewContainer.appendChild(imagePreview);

                    // Delete button for each file
                    const deleteButton = document.createElement('button');
                    deleteButton.classList.add('btn', 'btn-danger', 'delete-btn');
                    deleteButton.innerText = 'X';
                    deleteButton.onclick = function() {
                        // Remove the preview container
                        previewContainer.remove();
                        
                        // Create a new file list excluding the deleted file
                        const newFileList = Array.from(fileInput.files).filter(f => f !== file);
                        
                        // Reassign the remaining files to the input field
                        const dataTransfer = new DataTransfer();
                        newFileList.forEach(f => dataTransfer.items.add(f));
                        fileInput.files = dataTransfer.files; // Update the file input with the new list
                    };
                    previewContainer.appendChild(deleteButton);

                    // Append the preview to the file grid
                    fileGrid.appendChild(previewContainer);
                };

                reader.readAsDataURL(file);
            });
        });
    });
});
