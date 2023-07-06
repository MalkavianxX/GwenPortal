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
function agregarEnlacePP() {
    const url = `http://127.0.0.1:8000/micontenido/crear_preferencia_PP/`;
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
  function agregarEnlacePago() { 
    const url = `http://127.0.0.1:8000/micontenido/crear_preferencia_MP/`;
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

  function initMetodos() {
    agregarEnlacePP();
    agregarEnlacePago();
  }
  window.addEventListener('load', initMetodos);
