function filterTable() {
    // Pegando os valores do filtro
    let nomeFilter = document.getElementById("nome").value.toLowerCase();
    let cpfFilter = document.getElementById("cpf").value.replace(/\D/g, ''); // Remove caracteres não numéricos do CPF

    let table = document.getElementById("clients-table");
    let rows = table.getElementsByTagName("tr");

    for (let i = 1; i < rows.length; i++) { // Começa do índice 1 para ignorar o cabeçalho
        let row = rows[i];
        let nameCell = row.getElementsByClassName("client-name")[0];
        let cpfCell = row.getElementsByClassName("client-cpf")[0];

        let nameText = nameCell ? nameCell.textContent.toLowerCase() : "";
        let cpfText = cpfCell ? cpfCell.textContent.replace(/\D/g, '') : "";

        // Verifica se o nome e/ou CPF correspondem aos filtros
        if (
            (nomeFilter === "" || nameText.includes(nomeFilter)) &&
            (cpfFilter === "" || cpfText.includes(cpfFilter))
        ) {
            row.style.display = ""; // Exibe a linha
        } else {
            row.style.display = "none"; // Oculta a linha
        }
    }
}