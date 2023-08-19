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
function agregarAlCarrito(productoId) {
  const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
  const url = `{% url 'agregar_al_carrito/' ${productoId}/ %}`;

  const fetchOptions = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrfToken,
    },
  };
  fetch(url, fetchOptions)
    .then((response) => response.json())
    .then(() => {
      obtener_carrito();
      
    })
    .catch((error) => {
      console.error("Ocurrió un error en la solicitud:", error);
    });
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

  const url = `{% url 'ver_carrito/' %}`;
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
        document.getElementById('total-carrito').value = formatCurrency(total) + "USD" ;
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
                        <button class="btn btn-outline-danger"  onclick="remover_del_carrito('${idCollection}')" type="button">Eliminar del carrito</button>
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

        cantidadProductosElement.innerHTML ="&nbsp;&nbsp;"+cantidadProductos.toString();
        //MERCADO PAGO SDK       
       
        //PAYPAL LINK
     

      });
    })
    .catch((error) => {
      console.error("Ocurrió un error  obtener el carrito Por favor,:", error);
    });
}
function convertirAFloat(stringValor) {
  // Eliminar el símbolo "$" y las comas ","
  const valorSinSimbolo = stringValor.replace("$", "").replace(",", "");
  
  // Convertir a float
  const floatValor = parseFloat(valorSinSimbolo);
  
  return floatValor;
}

function verificarCupon() {
  // Obtener el valor del cupón del input
  const cuponInput = document.getElementById('cupon-input');
  const cupon = cuponInput.value;

  // Realizar una solicitud al servidor para verificar el cupón
  const url = `/micontenido/verificar_descuento/${cupon}/`;
  const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;

  const fetchOptions = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrfToken,
    },
  };

  fetch(url, fetchOptions)
    .then(response => response.json())
    .then(data => {
      if (data.status === 'success') {
        const valorDescuento = data.valor;
        precio_original = document.getElementById('total-carrito');
        set_precio_original = convertirAFloat(precio_original.value);
        const nuevo_precio = set_precio_original- parseFloat(valorDescuento);
        precio_original.value = formatCurrency(nuevo_precio);
        console.log(`Cupón válido. Valor de descuento: ${valorDescuento}`);
        text_mensaje = document.getElementById('alter-descuento');
        text_mensaje.classList.add('text-success');
        text_mensaje.textContent ="Ahorraste "+formatCurrency(valorDescuento)+"USD";
        text_mensaje.style.display = "block";
        const btn_verificar = document.getElementById('btn-verificar-cupon');
        btn_verificar.disabled  = true;

        // Realizar las acciones adicionales según sea necesario con el valor de descuento obtenido
      } else {
        const mensajeError = data.message;
        console.log(`Error: ${mensajeError}`);
        text_mensaje = document.getElementById('alter-descuento');
        text_mensaje.classList.add('text-danger');
        text_mensaje.textContent ="El cupon no es valido";
        text_mensaje.style.display = "block";
        cuponInput.value = "";
        // Mostrar el mensaje de error al usuario o realizar las acciones adicionales según sea necesario
      }
    })
    .catch(error => {
      console.error('Ocurrió un error en la solicitud:', error);
      // Mostrar un mensaje de error genérico al usuario o realizar las acciones adicionales según sea necesario
    });
}

// Llamar a la función al cargar la página
window.addEventListener('load', obtener_carrito);


//meradopago
function agregarEnlacePago() { 
  const url = `/micontenido/crear_preferencia_MP/`;
  const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;

  const fetchOptions = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrfToken,
    },
  };
  fetch(url,fetchOptions)  // Reemplaza '/ruta/obtener_enlace_pago/' con la ruta correcta de tu vista Django
    .then(response => response.json())
    .then(data => {
      
    const mp = new MercadoPago(data.public_key_mp);
    mp.bricks().create("wallet", "wallet_container", {
      initialization: {
          preferenceId: data.preference_id,
          redirectMode: "modal"

      },

   });
    })
    .catch(error => {
      console.error("Ocurrió un error al obtener el enlace de pago:", error);
      // Manejar el error adecuadamente
    });
}

function agregarEnlacePP() {
  const url = `/micontenido/crear_preferencia_PP/`;
  const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;

  const fetchOptions = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrfToken,
    },
  };
  fetch(url,fetchOptions)
  .then(response => response.json())
  .then(data => {
    const pp_link = data.link;
    const linkElement = document.getElementById("pp-link");
    linkElement.href = pp_link;
  })
  .catch(error => {
    console.error("Ocurrió un error al obtener el enlace de pago:", error);
    // Manejar el error adecuadamente
  });

}
