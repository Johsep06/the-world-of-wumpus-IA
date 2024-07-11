const play = document.getElementById('play');

let isPlaying = false;
let intervalID = null;

function playButton(){
    if (!isPlaying){
        play.querySelector('.bi').classList.remove('bi-play-fill');
        play.querySelector('.bi').classList.add('bi-pause-fill');
        intervalID = setInterval(render_container, 1000, '/board/update');
        isPlaying = true;
    } else {
        play.querySelector('.bi').classList.remove('bi-pause-fill');
        play.querySelector('.bi').classList.add('bi-play-fill');
        clearInterval(intervalID);
        isPlaying = false;
    }
}


function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

function render_container(route, container) {
    fetch(route)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok ' + response.statusText);
            }
            return response.text(); // Retorna a resposta como texto
        })
        .then(data => {
            document.getElementById(container).innerHTML = ''; // Limpa o container
            document.getElementById(container).innerHTML = data; // Insere o HTML retornado no container
        })
        .catch(error => {
            console.error('Erro ao carregar conteúdo:', error);
        });
}

render_container("/board/", 'map');
render_container('/board/status', 'status')
document.getElementById('new-game').addEventListener('click', () => {
    render_container("/board/", 'map');
    render_container('/board/status', 'status')
    // clearInterval(intervalID);
});
