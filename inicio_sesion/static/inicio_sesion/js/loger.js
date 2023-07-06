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


function logCreate() {
    var usuario = document.getElementById("usuario_create").value;
    var contrasena = document.getElementById("password_create").value;
    var email = document.getElementById("correo_create").value;
    var nombre = document.getElementById("nombre_create").value;

    var formData = new FormData();
    formData.append("usuario", usuario);
    formData.append("contrsena", contrasena);
    formData.append("email", email);
    formData.append("nombre", nombre);

    var csrftoken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
    formData.append("csrfmiddlewaretoken", csrftoken);
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/inicio_sesion/register");
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
  