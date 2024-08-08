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

render_container('/result//table', 'table')