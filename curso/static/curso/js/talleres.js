function recargarpagina() {
    const location = window.location;

    // Reload the page
    location.reload();
}
document.getElementById("submitButton").addEventListener("click", function() {
    const nombre = document.getElementById('nombre').value;
    const categoria = document.getElementById('categoria').value;
    const descrip = document.getElementById('descrip').value;
    const precio = document.getElementById('precio').value;
    const imagen = document.getElementById('imagen').files[0];


    const formData = new FormData();
    formData.append('nombre', nombre);
    formData.append('categoria', categoria);
    formData.append('descrip', descrip);
    formData.append('precio', precio);
    formData.append('imagen', imagen);

    fetch("/cursos/guardar_taller", {
        method: "POST", 
      
        body: formData 
    })
    .then(response => response.json())
    .then(response => {
        // Manejar la respuesta del servidor
        modal = new bootstrap.Modal(
            document.getElementById("success-alert-modal"),
        );
        modal.show();
      }).catch(error => {
        // Manejar los errores
        modal = new bootstrap.Modal(
            document.getElementById("info-alert-modal"),
        );
        modal.show();
      });

    
});
