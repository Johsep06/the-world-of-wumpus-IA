const play = document.getElementById('play');
const rangeInput = document.getElementById('size');
const rangeValue = document.getElementById('size-value');
const map = document.getElementById('map');

let isPlaying = false;
let intervalID = null;
let statusGame = null;

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

function removePlayButton(){
    play.classList.add('none');
}

function retornPlayButton(){
    try {
        play.classList.remove('none');
    } catch (error) {
        console.log(error);
    }
}

async function getStatus() {
    try {
        const response = await fetch('/game/status-game');
        
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const data = await response.json();
        statusGame = data.status;
    } catch (error) {
        console.error('Error fetching variable:', error);
    }
}

function load(){
    size = rangeInput.value;
    map.style.gridTemplateRows = `repeat(${size}, 1fr)`;
    map.style.gridTemplateColumns = `repeat(${size}, 1fr)`;
    render_container("/game/load-board", 'map');
    render_container('/game/relatorio', 'status')
}

function playGame(){
    play.querySelector('.bi').classList.remove('bi-play-fill');
    play.querySelector('.bi').classList.add('bi-pause-fill');
    intervalID = setInterval(update, 1000);
    isPlaying = true;
}

function pauseGame(){
    play.querySelector('.bi').classList.remove('bi-pause-fill');
    play.querySelector('.bi').classList.add('bi-play-fill');
    clearInterval(intervalID);
    isPlaying = false;
}

function playButton(){
    if (!isPlaying){
        playGame();
    } else {
        pauseGame();
    }
}

function endGame(){
    if(statusGame == 'w' || statusGame == 'p' || statusGame == 'v'){
        console.log(statusGame);
        pauseGame();
        removePlayButton();
    }
}

function newGame(){
    pauseGame();
    load();
    retornPlayButton()
}

function update(){
    setTimeout(render_container, 200, "/game/update-board", "map")
    setTimeout(render_container, 400, '/game/relatorio', 'status')
    setTimeout(getStatus, 600);
    setTimeout(endGame, 800);
}

function updateRangeValue() {
    rangeValue.textContent = rangeInput.value;
}

load();