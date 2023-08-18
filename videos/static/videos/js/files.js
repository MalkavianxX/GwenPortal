document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("guardar-file-curso").addEventListener("click", function () {
        var cursoId = document.getElementById("curso-curso").value;
        var nombreArchivo = document.getElementById("nombre-curso").value;
        var tipoArchivo = document.getElementById("tipo-curso").value;
        var archivoInput = document.getElementById("file-curso");

        var formData = new FormData();
        formData.append("curso_id", cursoId);
        formData.append("nombre_archivo", nombreArchivo);
        formData.append("tipo_archivo", tipoArchivo);
        formData.append("archivo", archivoInput.files[0]);

        fetch("/videos/guardar_archivo_curso", {
            method: "POST",
            body: formData,
            headers: {
                "X-Requested-With": "XMLHttpRequest"
            }
        })
        .then(response => response.json())
        .then(data => {
            // Procesar respuesta exitosa si es necesario
            console.log(data);
        })
        .catch(error => {
            // Manejar error si es necesario
            console.error("Error en la solicitud fetch:", error);
        });
    });
    document.getElementById("guardar-file-taller").addEventListener("click", function () {
        var cursoId = document.getElementById("taller-taller").value;
        var nombreArchivo = document.getElementById("nombre-taller").value;
        var tipoArchivo = document.getElementById("tipo-taller").value;
        var archivoInput = document.getElementById("file-taller");

        var formData = new FormData();
        formData.append("taller_id", cursoId);
        formData.append("nombre_archivo", nombreArchivo);
        formData.append("tipo_archivo", tipoArchivo);
        formData.append("archivo", archivoInput.files[0]);

        fetch("/videos/guardar_archivo_taller", {
            method: "POST",
            body: formData,
            headers: {
                "X-Requested-With": "XMLHttpRequest"
            }
        })
        .then(response => response.json())
        .then(data => {
            // Procesar respuesta exitosa si es necesario
            console.log(data);
        })
        .catch(error => {
            // Manejar error si es necesario
            console.error("Error en la solicitud fetch:", error);
        });
    });
});