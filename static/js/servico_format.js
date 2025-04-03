document.addEventListener("DOMContentLoaded", function () {
    // Função para formatar o preço como R$ 0000,00
    function formatPreco(value) {
        value = value.replace(/\D/g, ""); // Remove tudo que não é dígito
        value = (value / 100).toFixed(2); // Converte para decimal com 2 casas
        value = value.replace(".", ","); // Troca ponto por vírgula
        value = value.replace(/(\d)(?=(\d{3})+(?!\d))/g, "$1."); // Adiciona pontos como separador de milhar
        return "R$ " + value;
    }

    // Aplica máscara ao input de preço
    const priceInput = document.getElementById("price");
    priceInput.addEventListener("input", function (e) {
        let cursorPos = e.target.selectionStart;
        let oldLength = e.target.value.length;
        e.target.value = formatPreco(e.target.value);
        let newLength = e.target.value.length;
        e.target.setSelectionRange(cursorPos + (newLength - oldLength), cursorPos + (newLength - oldLength));
    });

    // Limpa a formatação antes de submeter o formulário
    document.querySelector("form").addEventListener("submit", function (e) {
        let preco = document.getElementById("price");
        
        // Remove "R$ " e formatação, converte para número com ponto
        preco.value = preco.value.replace("R$ ", "").replace(/\./g, "").replace(",", ".");
        
        // Validação opcional: verifica se é um número válido
        if (isNaN(preco.value) || preco.value === "") {
            alert("O preço deve ser um número válido.");
            preco.focus();
            e.preventDefault(); // Impede o envio do formulário
        }
    });
});