function getCssVariable(variableName) {
    return getComputedStyle(document.documentElement).getPropertyValue(variableName).trim();
}

function submit(form, path, redirect) {
    const formData = new FormData(form);
    const encType = form.enctype;
    const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;

    axios.post(path, formData, {
        headers: { 
            "Content-Type": encType,
            "X-CSRFToken": csrfToken
        },
        withCredentials: true
    })
    .then(response => {
        console.log(response);
        const message = response.data?.message || "Task successful!";
        iziToast.success({
            title: 'Success',
            message: message,
            position: 'bottomCenter',
            backgroundColor: getCssVariable('--primary-color-2'),
            timeout: 3000
        });

        setTimeout(() => {
            form.reset();
            if (redirect) {
                window.location.href = redirect; // Redirect after success
            }
        }, 2000);
    })
    .catch(error => {
        console.log(error);
        iziToast.error({
            title: 'Error',
            message: error.response?.data?.message || 'Failed. Please try again!',
            position: 'bottomCenter',
            backgroundColor: '#FF4C4C',  // Custom red background
            titleColor: '#FFF',          // White title text
            messageColor: '#FFF',        // White message text
            iconColor: '#FFF',           // White icon color
            timeout: 4000,
            progressBarColor: '#FFA07A', // Custom progress bar color
            closeOnEscape: true,
            close: true,                 // Show close button
            transitionIn: 'fadeInDown',  
            transitionOut: 'fadeOutUp',
            theme: 'dark'
        });
    });
}
