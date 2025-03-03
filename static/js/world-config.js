const radioCarregar = document.getElementById("carregar");
const radioNovo = document.getElementById("novo");
const sectionCarregar = document.getElementById("tela-carregar");
const sectionNovo = document.getElementById("tela-novo");

function atualizarVisibilidade() {
    sectionCarregar.classList.toggle("oculto", !radioCarregar.checked);
    sectionNovo.classList.toggle("oculto", !radioNovo.checked);
}

radioCarregar.addEventListener("change", atualizarVisibilidade);
radioNovo.addEventListener("change", atualizarVisibilidade);

sectionCarregar.classList.toggle("oculto");
radioNovo.checked = true;
radioCarregar.checked = false;