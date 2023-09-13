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

