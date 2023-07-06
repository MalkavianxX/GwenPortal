
function guardar_curso() {
  // Obtener referencias a los elementos del formulario
  var inputFile = document.getElementById('file_videos');
  var inputTitle = document.getElementById('titulo_video');
  var inputDestino = document.getElementById('id_curso');

  var title = inputTitle.value; // Obtener el título del vídeo
  var collectionId = inputDestino.value; // Obtener el destino del vídeo
  console.log(title, collectionId);
  form = document.getElementById('subir_videos_curso').style.display="none";
  document.getElementById('spin_curso').style.display = "flex";
  // Llamar a la función uploadCursoVideo con los datos obtenidos
  uploadCursoVideo(title, collectionId, inputFile.files[0]);

}


// Función para enviar el vídeo a la API
function uploadCursoVideo(title, collectionId, file) {
  const options = {
    method: 'POST',
    headers: {
      accept: 'application/json',
      'content-type': 'application/*+json',
      AccessKey: '6b2d3de5-8f09-4541-a57fe5df8534-047a-4afd'
    },
    body: JSON.stringify({
      collectionId,
      title,
      file
    })
  };

  fetch(`https://video.bunnycdn.com/library/132990/videos`, options)
    /* 
      .then(response => response.json())
      .then(response => {
        if (response.status === 200) {
          // Get the video library ID and GUID from the response.
          const libraryId = response.videoLibraryId;
          const guid = response.guid;
  
          // Save the video.
          saveCursoVide(libraryId, guid, file);
        } else {
          console.log('Error uploading video: ' + response.message);
        }
      })
      .catch(err => console.error(err));
      */
    .then(response => response.json())
    .then(response => {
      console.log(response);
      console.log(response.videoLibraryId);
      console.log(response.guid);
      saveCursoVide(response.videoLibraryId, response.guid, file);
    }
    )
    .catch(err => console.error(err));
}

function saveCursoVide(libraryId, guid, file) {
  const options = {
    method: 'PUT',
    headers: {
      accept: 'application/json',
      'content-type': 'application/*+json',
      AccessKey: '6b2d3de5-8f09-4541-a57fe5df8534-047a-4afd'
    },
    body: file
  };

  fetch('https://video.bunnycdn.com/library/' + libraryId + '/videos/' + guid, options)
    .then(response => response.json())
    .then(response => {
      console.log(response);
      location.reload();})
    .catch(err => console.error(err));
}
/// TALLERES
function guardar_taller() {
  // Obtener referencias a los elementos del formulario
  var inputFile = document.getElementById('taller_file_videos');
  var inputTitle = document.getElementById('taller_titulo_video');
  var inputDestino = document.getElementById('id_taller');

  var title = inputTitle.value; // Obtener el título del vídeo
  var collectionId = inputDestino.value; // Obtener el destino del vídeo
  console.log(title, collectionId);
  // Llamar a la función uploadTallerVideo con los datos obtenidos
  form = document.getElementById('subir_videos_taller').style.display="none";
  document.getElementById('spin_taller').style.display = "flex";
  uploadTallerVideo(title, collectionId, inputFile.files[0]);

}


// Función para enviar el vídeo a la API
function uploadTallerVideo(title, collectionId, file) {
  const options = {
    method: 'POST',
    headers: {
      accept: 'application/json',
      'content-type': 'application/*+json',
      AccessKey: '1e8f3a9c-0092-464b-96c0336bad00-0a1d-4912'
    },
    body: JSON.stringify({
      collectionId,
      title,
      file
    })
  };

  fetch(`https://video.bunnycdn.com/library/132992/videos`, options)
    /* 
      .then(response => response.json())
      .then(response => {
        if (response.status === 200) {
          // Get the video library ID and GUID from the response.
          const libraryId = response.videoLibraryId;
          const guid = response.guid;
  
          // Save the video.
          saveTallerVideo(libraryId, guid, file);
        } else {
          console.log('Error uploading video: ' + response.message);
        }
      })
      .catch(err => console.error(err));
      */
    .then(response => response.json())
    .then(response => {
      console.log(response);
      console.log(response.videoLibraryId);
      console.log(response.guid);
      saveTallerVideo(response.videoLibraryId, response.guid, file);
    }
    )
    .catch(err => console.error(err));
}

function saveTallerVideo(libraryId, guid, file) {
  const options = {
    method: 'PUT',
    headers: {
      accept: 'application/json',
      'content-type': 'application/*+json',
      AccessKey: '1e8f3a9c-0092-464b-96c0336bad00-0a1d-4912'
    },
    body: file
  };

  fetch('https://video.bunnycdn.com/library/' + libraryId + '/videos/' + guid, options)
    .then(response => response.json())
    .then(response => {console.log(response);location.reload()})
    .catch(err => console.error(err));
}




