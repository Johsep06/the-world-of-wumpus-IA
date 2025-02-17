const skinImg = document.getElementById('skin');
var skin = 0;

const skins = [
    '../static/assets/skins/agente_2.png',
    '../static/assets/skins/agente_1.png',
];

function change_skin(val) {
    if (val === '+') {
        skin += 1;
        if (skin === skins.length) {
            skin = 0;
        }
    } else if (val === '-') {
        skin -= 1;
        if (skin === -1) {
            skin = skins.length - 1; // Corrigido para voltar ao último índice
        }
    }

    // Adiciona 'url()' ao caminho da imagem
    skinImg.style.backgroundImage = `url('${skins[skin]}')`;
}

change_skin('')