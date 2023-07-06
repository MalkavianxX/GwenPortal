
function obtenerCursosVideos(num_videos) {
        //listar cursos
        const options_talleres = {
            method: 'GET',
            headers: {
              accept: 'application/json',
              AccessKey: '6b2d3de5-8f09-4541-a57fe5df8534-047a-4afd'
            }
          };
          
          fetch('https://video.bunnycdn.com/library/132990/collections?page=1&itemsPerPage=5&orderBy=date', options_talleres)
            .then(response => response.json())
            .then(response => {
                const cursos = response.items;
                cursos.forEach(curso => {
                    agregar_cursos(curso.guid,num_videos)
                })
            })
            .catch(err => console.error(err));    
        
        //
}

function obtenerTalleresVideos(num_videos) {
    //listar talleres
    const options_talleres = {
        method: 'GET',
        headers: {
          accept: 'application/json',
          AccessKey: '1e8f3a9c-0092-464b-96c0336bad00-0a1d-4912'
        }
      };
      
      fetch('https://video.bunnycdn.com/library/132992/collections?page=1&itemsPerPage=5&orderBy=date', options_talleres)
        .then(response => response.json())
        .then(response => {
            const talleres = response.items;
            talleres.forEach(taller => {
                agregar_talleres(taller.guid,num_videos)
            })
        })
        .catch(err => console.error(err));    
    
    //

}

function listar_todos_videos(){
    obtenerCursosVideos(5);
    obtenerTalleresVideos(5);
}

function agregar_talleres(collection_id,num_videos) {
    const options = {
        method: 'GET',
        headers: {
            accept: 'application/json',
            AccessKey: '1e8f3a9c-0092-464b-96c0336bad00-0a1d-4912'
        }
    };

    fetch(`https://video.bunnycdn.com/library/132992/videos?page=1&itemsPerPage=${num_videos}&collection=${collection_id}&orderBy=date`, options)
        .then(response => response.json())
        .then(response => {
            const videos = response.items;
            const container = document.getElementById('video-container-talleres');

            videos.forEach(video => {
                const colDiv = document.createElement('div');
                colDiv.classList.add('col-lg-4', 'col-12');

                const cardDiv = document.createElement('div');
                cardDiv.classList.add('card', 'overflow-y-hidden');
                cardDiv.style.height = '350px !important;';

                const iframeDiv = document.createElement('div');
                iframeDiv.style.position = 'relative';
                iframeDiv.style.paddingTop = '56.25%';

                const iframe = document.createElement('iframe');
                iframe.src = `https://iframe.mediadelivery.net/embed/132992/${video.guid}?autoplay=false&preload=false`;
                iframe.loading = 'lazy';
                iframe.style.border = 'none';
                iframe.style.position = 'absolute';
                iframe.style.top = '0';
                iframe.style.height = '100%';
                iframe.style.width = '100%';
                iframe.allow = 'accelerometer; gyroscope; autoplay; encrypted-media; picture-in-picture;';
                iframe.allowFullscreen = 'true';

                const cardBodyDiv = document.createElement('div');
                cardBodyDiv.classList.add('card-body');
                cardBodyDiv.style.height = '10rem !important;';

                const titleH5 = document.createElement('p');
                titleH5.classList.add('card-text', 'fw-bold');
                titleH5.textContent = video.title;

                container.appendChild(colDiv);
                colDiv.appendChild(cardDiv);
                cardDiv.appendChild(iframeDiv);
                iframeDiv.appendChild(iframe);
                cardDiv.appendChild(cardBodyDiv);
                cardBodyDiv.appendChild(titleH5);
            });
        })
        .catch(err => console.error(err));
}

function agregar_cursos(collection_id,num_videos) {
    const options = {
        method: 'GET',
        headers: {
            accept: 'application/json',
            AccessKey: '6b2d3de5-8f09-4541-a57fe5df8534-047a-4afd'
        }
    };

    fetch(`https://video.bunnycdn.com/library/132990/videos?page=1&itemsPerPage=${num_videos}&collection=${collection_id}&orderBy=date`, options)
        .then(response => response.json())
        .then(response => {
            const videos = response.items;
            const container = document.getElementById('video-container-cursos');

            videos.forEach(video => {
                const colDiv = document.createElement('div');
                colDiv.classList.add('col-lg-4', 'col-12');

                const cardDiv = document.createElement('div');
                cardDiv.classList.add('card', 'overflow-y-hidden');
                cardDiv.style.height = '350px !important;';

                const iframeDiv = document.createElement('div');
                iframeDiv.style.position = 'relative';
                iframeDiv.style.paddingTop = '56.25%';

                const iframe = document.createElement('iframe');
                iframe.src = `https://iframe.mediadelivery.net/embed/132990/${video.guid}?autoplay=false&preload=false`;
                iframe.loading = 'lazy';
                iframe.style.border = 'none';
                iframe.style.position = 'absolute';
                iframe.style.top = '0';
                iframe.style.height = '100%';
                iframe.style.width = '100%';
                iframe.allow = 'accelerometer; gyroscope; autoplay; encrypted-media; picture-in-picture;';
                iframe.allowFullscreen = 'true';

                const cardBodyDiv = document.createElement('div');
                cardBodyDiv.classList.add('card-body');
                cardBodyDiv.style.height = '10rem !important;';

                const titleH5 = document.createElement('p');
                titleH5.classList.add('card-text', 'fw-bold');
                titleH5.textContent = video.title;

                container.appendChild(colDiv);
                colDiv.appendChild(cardDiv);
                cardDiv.appendChild(iframeDiv);
                iframeDiv.appendChild(iframe);
                cardDiv.appendChild(cardBodyDiv);
                cardBodyDiv.appendChild(titleH5);
            });
        })
        .catch(err => console.error(err)); 
}
// Llama a la función obtenerVideos al cargar la página
window.addEventListener('load', listar_todos_videos);
