function ver_comentario(comentario) {
    const modalComentsOk = new bootstrap.Modal(document.getElementById('vercomm-modal'));
    document.getElementById('coment-zoom').value = comentario;
    modalComentsOk.show();

};
 
document.addEventListener("DOMContentLoaded", function () {
    const tdElements = document.querySelectorAll(".limited-text");

    tdElements.forEach(function (tdElement) {
        const maxCharacters = 50; // Cambia esto al número máximo de caracteres que deseas mostrar
        const originalText = tdElement.textContent;

        if (originalText.length > maxCharacters) {
            const truncatedText = originalText.substring(0, maxCharacters) + " ...";
            tdElement.textContent = truncatedText;
            tdElement.title = originalText; // Agregar el texto completo como atributo de título
        }
    });
});

function aprobar_comm(link) {
    const tr = link.closest('tr');
    const comentarioId = tr.id; // Obtener el id del comentario
    console.log(comentarioId);

    const url = "/comentarios/aprobar_comm";
    const datos = {
        comm_id: comentarioId,
    
    };
    const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
    const fetchOptions = {
        method: 'POST',
        body: JSON.stringify(datos),
        headers: {
            'Content-Type': 'application/json',
            "X-CSRFToken": csrfToken,

        }
    };
    fetch(url, fetchOptions)
        .then(response => {
            if (response.ok) {
            console.log('Datos enviados correctamente');
            window.location.reload();

        } else {
            console.error('Error al enviar los datos');
        }
    })
    .catch(error => {
        console.error('Error en la conexión o en el procesamiento de la respuesta', error);
    });
};
function debegar_comm(link) {
    const tr = link.closest('tr');
    const comentarioId = tr.id; // Obtener el id del comentario
    console.log(comentarioId);
    const url = "/comentarios/denegar_comm";
    const datos = {
        comm_id: comentarioId,
    
    };
    const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
    const fetchOptions = {
        method: 'POST',
        body: JSON.stringify(datos),
        headers: {
            'Content-Type': 'application/json',
            "X-CSRFToken": csrfToken,

        }
    };
    fetch(url, fetchOptions)
        .then(response => {
            if (response.ok) {
            console.log('Datos enviados correctamente');
            window.location.reload();

        } else {
            console.error('Error al enviar los datos');
        }
    })
    .catch(error => {
        console.error('Error en la conexión o en el procesamiento de la respuesta', error);
    });
};
function eliminar_comm(link) {
    const tr = link.closest('tr');
    const comentarioId = tr.id; // Obtener el id del comentario
    console.log(comentarioId);
    const url = "/comentarios/eliminar_comm";
    const datos = {
        comm_id: comentarioId,
    
    };
    const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
    const fetchOptions = {
        method: 'POST',
        body: JSON.stringify(datos),
        headers: {
            'Content-Type': 'application/json',
            "X-CSRFToken": csrfToken,

        }
    };
    fetch(url, fetchOptions)
        .then(response => {
            if (response.ok) {
            console.log('Datos enviados correctamente');
            window.location.reload();

        } else {
            console.error('Error al enviar los datos');
        }
    })
    .catch(error => {
        console.error('Error en la conexión o en el procesamiento de la respuesta', error);
    });
};