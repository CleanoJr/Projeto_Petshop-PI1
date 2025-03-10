function filterTable() {
    // Pegando os valores do filtro
    let nomeFilter = document.getElementById("nome_pet").value.toLowerCase();
    let donoFilter = document.getElementById("nome_dono").value.toLowerCase();
    let especieFilter = document.getElementById("tipo").value.toLowerCase();

    let table = document.getElementById("pets-table");
    let rows = table.getElementsByTagName("tr");

    for (let i = 1; i < rows.length; i++) { // Começa do índice 1 para ignorar o cabeçalho
        let row = rows[i];
        let nameCell = row.getElementsByClassName("pet-name")[0];
        let ownerCell = row.getElementsByClassName("pet-owner")[0];
        let speciesCell = row.getElementsByClassName("pet-species")[0];

        let nameText = nameCell ? nameCell.textContent.toLowerCase() : "";
        let ownerText = ownerCell ? ownerCell.textContent.toLowerCase() : "";
        let speciesText = speciesCell ? speciesCell.textContent.toLowerCase() : "";

        // Verifica se o nome, dono e/ou espécie correspondem aos filtros
        if (
            (nomeFilter === "" || nameText.includes(nomeFilter)) &&
            (donoFilter === "" || ownerText.includes(donoFilter)) &&
            (especieFilter === "" || speciesText.includes(especieFilter))
        ) {
            row.style.display = ""; // Exibe a linha
        } else {
            row.style.display = "none"; // Oculta a linha
        }
    }
}