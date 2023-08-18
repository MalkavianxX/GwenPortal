
function validarCampos(titulo, categoria, contenido, archivo) {
  if (titulo.trim() === '') {
    return 'El campo de título es obligatorio.';
  }

  if (categoria.trim() === '') {
    return 'El campo de categoría es obligatorio.';
  }

  if (contenido.trim() === '') {
    return 'El campo de contenido es obligatorio.';
  }



  return ''; // Si todos los campos son válidos, no hay mensaje de error
}
//publicar blog
// Obtener referencia al botón "publicar-blog"
const botonPublicar = document.getElementById('publicar-blog');

// Agregar un evento "click" al botón "publicar-blog"
botonPublicar.addEventListener('click', () => {
  // Obtener los valores de los campos de entrada de formulario
  const titulo = document.getElementById('creador-titulo-blog').value;
  const categoria = document.getElementById('creador-blog-categoria').value;
  const contenido = document.getElementById('creador-contenido-blog').value;
  const archivo = document.getElementById('creador-archivo-blog').files[0];
  const mensajeError = validarCampos(titulo, categoria, contenido, archivo);

  if (mensajeError) {
    alert(mensajeError);
  } else {
    // Crear un objeto FormData para enviar los valores al servidor
    const formData = new FormData();
    formData.append('titulo', titulo);
    formData.append('categoria', categoria);
    formData.append('contenido', contenido);
    formData.append('archivo', archivo);


    // Enviar los datos al servidor utilizando AJAX
    fetch('/blog/publicar_post', {
      method: 'POST',
      body: formData
    }).then(response => {
      // Manejar la respuesta del servidor
 
      

      const location = window.location;

      // Reload the page
      location.reload();

      console.log(response);
    }).catch(error => {
      // Manejar los errores
      console.error(error);
    });
  }

});
