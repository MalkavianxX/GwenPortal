function marcar_completado() {
    const guid = document.getElementById('video_presentado').value;
    const idCollection = document.getElementById('id_collection').value;
    const idLibrary = document.getElementById('id_library').value;

    const url = `http://3.144.80.153/micontenido/marcar_completado/${guid}/`;
    const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;

    const fetchOptions = {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrfToken,
        },
        body: JSON.stringify({
            id_library: idLibrary,
            id_collection: idCollection
        }),
    };

    fetch(url, fetchOptions)
        .then(response => response.json())
        .then(() =>{
            location.reload(true);
        })
        .catch(error => {
            console.error('Error:', error);
        });
}
