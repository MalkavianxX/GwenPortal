
document.addEventListener('DOMContentLoaded', () => {
    const fileInput = document.getElementById('creador-archivo-blog');
    const previewImage = document.getElementById('prev-imagen');
  
    fileInput.addEventListener('change', () => {
      // Obtiene el archivo seleccionado
      const file = fileInput.files[0];
  
      if (file) {
        // Crea un objeto URL temporal para mostrar el archivo
        const url = URL.createObjectURL(file);
        // Actualiza el src de la imagen con el URL temporal
        previewImage.src = url;
      }
    });
  });
  // Selección de elementos
const creadorTitulo = document.getElementById('creador-titulo-blog');
const creadorContenido = document.getElementById('creador-contenido-blog');
const prevTitulo = document.getElementById('prev-titulo');
const prevContenido = document.getElementById('prev-contenido');

// Agregar un evento de escucha al botón para actualizar la vista previa
document.addEventListener('DOMContentLoaded', () => {
  const actualizarVistaPrevia = () => {
    // Obtener los valores de entrada
    const titulo = creadorTitulo.value;
    const contenido = creadorContenido.value;

    // Actualizar los elementos de vista previa
    prevTitulo.innerText = titulo;
    prevContenido.innerText = contenido;
  };

  // Agregar eventos de escucha a los campos de entrada
  creadorTitulo.addEventListener('input', actualizarVistaPrevia);
  creadorContenido.addEventListener('input', actualizarVistaPrevia);
});

// Selección de elementos
const creadorColorBg = document.getElementById('creador-color-bg-blog');
const creadorColorFg = document.getElementById('creador-color-fg-blog');
const prevCard = document.getElementById('prev-card');

// Agregar un evento de escucha al botón para actualizar la vista previa
document.addEventListener('DOMContentLoaded', () => {
  const actualizarVistaPrevia = () => {
    // Obtener los valores de entrada
    const colorBg = creadorColorBg.value;
    const colorFg = creadorColorFg.value;

    // Actualizar los elementos de vista previa
    prevCard.style.backgroundColor = colorBg;
    prevCard.style.color = colorFg;
  };

  // Agregar eventos de escucha a los campos de entrada
  creadorColorBg.addEventListener('input', actualizarVistaPrevia);
  creadorColorFg.addEventListener('input', actualizarVistaPrevia);
});


  document.addEventListener("DOMContentLoaded", function() {
    // Seleccionar el input y el div previo
    var input = document.getElementById("exampleDataList");
    var prevTitulo = document.getElementById("prev-titulo");
    var prevContenido = document.getElementById("prev-contenido");

    // Agregar un listener al input para detectar cambios
    input.addEventListener("input", function() {
      // Obtener el valor seleccionado
      var fuente = input.value;

      // Aplicar la fuente seleccionada a los elementos previos
      prevTitulo.style.fontFamily = fuente;
      prevContenido.style.fontFamily = fuente;
    });
  });

  document.addEventListener("DOMContentLoaded", function() {
    const tamanoTituloInput = document.getElementById("tamano-fuente-titulo");
    const tamanoContenidoInput = document.getElementById("tamano-fuente-cuerpo");
    const prevTitulo = document.getElementById("prev-titulo");
    const prevContenido = document.getElementById("prev-contenido");
  
    tamanoTituloInput.addEventListener("input", function() {
      prevTitulo.style.fontSize = this.value + "px";
    });
  
    tamanoContenidoInput.addEventListener("input", function() {
      prevContenido.style.fontSize = this.value + "px";
    });
  });
  




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
  const colorFondo = document.getElementById('creador-color-bg-blog').value;
  const colorLetra = document.getElementById('creador-color-fg-blog').value;
  const fuenteLetra = document.getElementById('creador-fuente-letra').value;
  const tamanoLetraTitulo = document.getElementById('tamano-fuente-titulo').value;
  const tamanoLetraCuerpo = document.getElementById('tamano-fuente-cuerpo').value;
  // Crear un objeto FormData para enviar los valores al servidor
  const formData = new FormData();
  formData.append('titulo', titulo);
  formData.append('categoria', categoria);
  formData.append('contenido', contenido);
  formData.append('archivo', archivo);
  formData.append('estilo_color_fondo', colorFondo);
  formData.append('estilo_color_letra', colorLetra);
  formData.append('estilo_fuente_letra', fuenteLetra);
  formData.append('estilo_tamano_letra_titulo', tamanoLetraTitulo);
  formData.append('estilo_tamano_letra_cuerpo', tamanoLetraCuerpo);

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
    colorFondo.value = "";
    colorLetra.value = "";
    fuenteLetra.value = "";
    tamanoLetraTitulo.value = "";
    tamanoLetraCuerpo.value = "";
    $('#alerta-categoria').fadeIn().delay(2000).fadeOut();

    console.log(response);
  }).catch(error => {
    // Manejar los errores
    console.error(error);
  });
});
