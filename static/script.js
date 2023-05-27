const form = document.querySelector('form');

// Add an event listener to the form
form.addEventListener('submit', (event) => {
    // Prevent the form from submitting
    event.preventDefault();

    // Create a new FormData object from the form data
    const formData = new FormData(form);

    // Send a POST request to the server with the form data
    fetch('http://localhost:8000/submit', {
        method: 'POST',
        body: formData
    })
        .then(response => {
            if (response.ok) {
                location.replace('/data');
            } else {
                alert('Error occurred while registering!');
            }
        })
        .catch(error => console.error(error));
});
