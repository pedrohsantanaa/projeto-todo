//Função que pergunta ao usuário se ele quer msm excluir a tarefa
document.querySelectorAll(".delete-btn").forEach(btn => {
    btn.addEventListener("click", function(e) {
        e.preventDefault();

        const delLink = this.getAttribute("href");

        if (delLink && confirm("Quer deletar esta tarefa?")) {
            window.location.href = delLink;
        }
    });
});

//Função de Pesquisar
document.getElementById("search-btn").addEventListener("click", function(){
    document.getElementById("search-form").onsubmit();
}, false );

//Função para filtrar a escolha
document.getElementById("filter").addEventListener("change", function() {
    const filtro = this.value;
    const novaURL = window.location.origin + window.location.pathname + '?filter=' + filtro;
    window.location.href = novaURL;
});
