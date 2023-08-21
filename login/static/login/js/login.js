const swiper = new Swiper('.swiper', {
    // Optional parameters
    direction: 'horizontal',
    loop: true,
  
    // If we need pagination
    pagination: {
      el: '.swiper-pagination',
    },
  
    // Navigation arrows
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },
  
    // And if we need scrollbar
    scrollbar: {
      el: '.swiper-scrollbar',
    },
  });
  document.addEventListener("DOMContentLoaded", function () {
      const form = document.getElementById("form-comment");
      const commentInput = document.getElementById("mycoment");
  
      form.addEventListener("submit", function (event) {
          event.preventDefault();
          const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
  
          const datos = {
            comentario: commentInput.value,
            
          };
          const url = "/comentarios/guardar_comentario";
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
                  // La petición se realizó con éxito
                  console.log('Datos enviados correctamente');
                  commentInput.value = "";
                  const modalComentsOk = new bootstrap.Modal(document.getElementById('modalComentsOk'));
                  modalComentsOk.show();
  
              } else {
                  // Hubo un error en la petición
                  console.error('Error al enviar los datos');
              }
          })
          .catch(error => {
              console.error('Error en la conexión o en el procesamiento de la respuesta', error);
          });
  
      });
  });

  
    window.addEventListener('load', obtener_carrito);

    function formatCurrency(value) {
        const number = parseFloat(value);
        if (isNaN(number)) {
            return value; // Devolver el valor original si no es un número válido
        }

        const formattedNumber = number.toLocaleString("en-US", {
            style: "currency",
            currency: "USD",
        });

        return formattedNumber;
    }
    function remover_del_carrito(productoId) {
      const url = `/micontenido/eliminar_del_carrito/${productoId}/`;
      const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;

      const fetchOptions = {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": csrfToken,
        },
      };

      fetch(url, fetchOptions)
        .then((response) => {
          if (response.ok) {
            // Eliminar el div con el ID correspondiente
            const div = document.getElementById(productoId);
            div.remove();
            obtener_carrito();
          } else {
            console.erro("Ocurrió un error al  eliminar el producto del carrito.");
          }
        })
        .catch((error) => {
          console.error("Ocurrió un error en la solicitud:", error);
        });
      }
    function obtener_carrito() {

      const url = `{% url 'ver_carrito' %}`;
      const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;

      const fetchOptions = {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": csrfToken,
        },
      };

      fetch(url, fetchOptions)
        .then((response) => {
          if (response.ok) {
            return response.json();
          } else {
            throw new Error("Error al recuperar el carrito");
          }
        })
        .then((data) => {
          const carrito = data.productos;
          const total = data.total;

          // Eliminar el contenido actual del contenedor
          const carritoContenedor = document.getElementById('carrito-contenedor');
          carritoContenedor.innerHTML = '';

          // Recorrer la lista de productos en el carrito
          carrito.forEach((producto) => {
            const id = producto.id;
            const nombre = producto.nombre;
            const imagen = producto.imagen;
            const precio = producto.precio;
            const categoria = producto.categoria;
            const idCollection = producto.id_collection;
            document.getElementById('total-carrito').value = formatCurrency(total) + "USD";
            // Crear el elemento HTML para mostrar el producto
            const productoElement = document.createElement('div');
            productoElement.classList.add('col-12');
            productoElement.id = idCollection;
            
            productoElement.innerHTML = `
          <div class="card " style="max-width: 540px;background-color: transparent !important;">
            <div class="row g-0">
              <div class="col-md-4">
                <img src="${imagen}"  class="img-fluid rounded-start align-self-center" alt="...">
              </div>
              <div class="col-md-8">
                <div class="card-body">
                  <div class="w-100 d-flex justify-content-between">
                    <h6 class="card-title fw-bold">${nombre}</h6>
                    <h6 class="text-success fw-bold">${formatCurrency(precio)}</h6>
                  </div>
                  <div class="w-100 lh-1">
                    <p class="card-text"><small>Categoria: ${categoria}</small></p>
                    <p class="card-text"><small>Curso/Taller ${nombre}</small></p>
                  </div>
                  <div class="w-100">
                    <div class="d-grid gap-2">
                      <button class="btn btn-sm  btn-danger"
                          id="${idCollection}" 
                          onclick="remover_del_carrito(this.id)" 
                          type="button">
                          Eliminar
                        </button>                    
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        `;
            // Agregar el elemento al contenedor
            carritoContenedor.appendChild(productoElement);
            const cantidadProductos = carrito.length;
            const cantidadProductosElement = document.getElementById("cantidad-productos");

            cantidadProductosElement.innerHTML = "&nbsp;&nbsp;" + cantidadProductos.toString();
            //MERCADO PAGO SDK       

            //PAYPAL LINK


          });
        })
        .catch((error) => {
          console.error("Ocurrió un error  obtener el carrito Por favor,:", error);
        });
    }