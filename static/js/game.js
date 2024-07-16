const play = document.getElementById('play');
const rangeInput = document.getElementById('size');
const rangeValue = document.getElementById('size-value');
const map = document.getElementById('map');

let isPlaying = false;
let intervalID = null;

function load(){
    size = rangeInput.value;
    map.style.gridTemplateRows = `repeat(${size}, 1fr)`;
    map.style.gridTemplateColumns = `repeat(${size}, 1fr)`;
    render_container("/game/load-board", 'map');
    render_container('/game/status', 'status')
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

function update(){
    render_container("/game/update-board", "map")
    render_container('/game/status', 'status')
}

function playButton(){
    if (!isPlaying){
        play.querySelector('.bi').classList.remove('bi-play-fill');
        play.querySelector('.bi').classList.add('bi-pause-fill');
        intervalID = setInterval(update, 1000);
        isPlaying = true;
    } else {
        play.querySelector('.bi').classList.remove('bi-pause-fill');
        play.querySelector('.bi').classList.add('bi-play-fill');
        clearInterval(intervalID);
        isPlaying = false;
    }
}

function updateRangeValue() {
    rangeValue.textContent = rangeInput.value;
}

// rangeInput.addEventListener('input', updateRangeValue);

document.getElementById('new-game').addEventListener('click', () => {
    load();
});




function loadSize() {
    const valor = rangeInput.value;
    
    fetch('/game/set-size', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ value: valor }),
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}