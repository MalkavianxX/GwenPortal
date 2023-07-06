//CATEGORIAS
document.getElementById('GuardarCategoria').addEventListener('click', function() {
  const nombre = document.getElementById('categoria-blog-nombre').value;
  const descripcion = document.getElementById('categoria-blog-descripcion').value;
  const csrftoken = document.getElementsByName('csrfmiddlewaretoken')[0].value;
  const xhr = new XMLHttpRequest();
  xhr.open('POST', 'crear_categoria', true);
  xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
  xhr.setRequestHeader('X-CSRFToken', csrftoken);
  xhr.onreadystatechange = function() {
      if (xhr.readyState === 4 && xhr.status === 200) {
          const data = JSON.parse(xhr.responseText);
          const categorias = data.categorias;
          const options = document.getElementById('categoriaOptions');
          options.innerHTML = '';
          for (const categoria of categorias) {
              const option = document.createElement('option');
              option.value = categoria.nombre;
              options.appendChild(option);
          }
          // Cierra el modal
          $('#modal-categoria-agregar').modal('hide');
          $(document).ready(function() {
            $('#alerta-categoria').fadeIn().delay(2000).fadeOut();
          });

      }
  };
  const params = 'categoria-blog-nombre=' + encodeURIComponent(nombre) +
                 '&categoria-blog-descripcion=' + encodeURIComponent(descripcion);
  xhr.send(params);
});


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
    titulo.value = "";
    categoria.value = "";
    contenido.value = "";
    archivo.value = "";

    $('#alerta-categoria').fadeIn().delay(2000).fadeOut();

    console.log(response);
  }).catch(error => {
    // Manejar los errores
    console.error(error);
  });
});
