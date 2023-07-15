function logIn() {
    // Obtener los valores del formulario
    var usuario = document.getElementById("loginEmail").value;
    var contrasena = document.getElementById("loginPassword").value;
  
    // Crear objeto FormData y agregar los valores del formulario
    var formData = new FormData();
    formData.append("usuario", usuario);
    formData.append("contrasena", contrasena);
  
    // Obtener el valor del CSRF token desde la página
    var csrftoken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
  
    // Agregar el CSRF token al objeto FormData
    formData.append("csrfmiddlewaretoken", csrftoken);
  
    // Crear objeto XMLHttpRequest y enviar la petición
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/inicio_sesion/log_in");
    xhr.onreadystatechange = function() {
      if (this.readyState === XMLHttpRequest.DONE && this.status === 200) {

        // Redirigir a la vista en caso de éxito
        window.location.href = "/inicio_sesion/render_dashboard";
      } else if (this.readyState === XMLHttpRequest.DONE && this.status === 400) {
        // Mostrar mensaje de error en caso de error
        alert("Ha ocurrido un error. Inténtelo de nuevo más tarde.");
      }
    };
    xhr.send(formData);
  };


// Obtener referencias a los elementos del formulario
const form = document.getElementById('form-reg');
const nombreInput = document.getElementById('reg_nombre');
const correoInput = document.getElementById('reg_correo');
const pass1Input = document.getElementById('reg_pass1');
const pass2Input = document.getElementById('reg_pass2');
const checkInput = document.getElementById('reg_check');
const submitButton = document.getElementById('reg_submit');

// Deshabilitar el botón de registrar inicialmente
submitButton.disabled = true; 
checkInput.disabled = true;
// Función para validar las contraseñas
function validarContraseñas() {
    if (pass1Input.value === pass2Input.value) {
      checkInput.disabled = false;
    } else {
      checkInput.disabled = true;
    }
}

// Función para habilitar el botón de registrar cuando se marque el checkbox
function habilitarBoton() {
    submitButton.disabled = !checkInput.checked;
}

// Evento de cambio en los campos de contraseña
pass1Input.addEventListener('input', validarContraseñas);
pass2Input.addEventListener('input', validarContraseñas);

// Evento de cambio en el checkbox
checkInput.addEventListener('change', habilitarBoton);

// Función para enviar los datos mediante fetch al endpoint /accion
function enviarDatos() {
    // Obtener los valores de los campos del formulario
    const nombre = nombreInput.value;
    const correo = correoInput.value;
    const pass = pass1Input.value;

    // Crear el objeto de datos a enviar
    const datos = {
        nombre: nombre,
        correo: correo,
        pass: pass
    };
    const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
    const url = "https://gwenluy.com/inicio_sesion/crear_usuario/"
    // Configurar la petición fetch
    const fetchOptions = {
        method: 'POST',
        body: JSON.stringify(datos),
        headers: {
            'Content-Type': 'application/json',
            "X-CSRFToken": csrfToken,

        }
    };

    // Enviar la petición fetch
    fetch(url, fetchOptions)
        .then(response => {
            if (response.ok) {
                // La petición se realizó con éxito
                console.log('Datos enviados correctamente');
                window.location.href = "/inicio_sesion/render_dashboard";

                // Aquí puedes realizar alguna acción adicional después de enviar los datos
            } else {
                // Hubo un error en la petición
                console.error('Error al enviar los datos');
                // Aquí puedes mostrar algún mensaje de error o realizar alguna acción adicional
            }
        })
        .catch(error => {
            // Hubo un error en la conexión o en el procesamiento de la respuesta
            console.error('Error en la conexión o en el procesamiento de la respuesta', error);
            // Aquí puedes mostrar algún mensaje de error o realizar alguna acción adicional
        });
}

// Evento de envío del formulario
form.addEventListener('submit', event => {
    event.preventDefault(); // Evitar el envío del formulario por defecto
    enviarDatos();
});
