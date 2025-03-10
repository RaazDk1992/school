function getCssVariable(variableName) {
    return getComputedStyle(document.documentElement).getPropertyValue(variableName).trim();
}

function submit(form, path, contentType) {
    const formData = new FormData(form);
    const encType = form.enctype;

    axios.post(path, formData, {
        headers: { 
            "Content-Type": encType,
            "X-CSRFToken": getCsrfToken() 
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
            window.location.href = "/back/dashboard"; // Redirect after success
        }, 2000);
    })
    .catch(error => {
        console.log(error);
        iziToast.error({
            title: 'Error',
            message: error.response?.data?.message || 'failed. Please try again!',
            position: 'bottomCenter',
            backgroundColor: '#900C3F',
            timeout: 4000
        });
    });
}
