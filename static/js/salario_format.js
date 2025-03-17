document.addEventListener("DOMContentLoaded", function () {
    // Função para formatar o telefone
    function formatTelefone(value) {
        value = value.replace(/\D/g, "").slice(0, 11);
        if (value.length > 10) {
            return value.replace(/(\d{2})(\d{5})(\d{4})/, "($1) $2-$3");
        } else if (value.length > 6) {
            return value.replace(/(\d{2})(\d{4})(\d{0,4})/, "($1) $2-$3");
        } else if (value.length > 2) {
            return value.replace(/(\d{2})(\d{0,5})/, "($1) $2");
        }
        return value;
    }

    // Função para formatar o salário como R$ 0000,00
    function formatSalario(value) {
        value = value.replace(/\D/g, ""); // Remove tudo que não é dígito
        value = (value / 100).toFixed(2); // Converte para decimal com 2 casas
        value = value.replace(".", ","); // Troca ponto por vírgula
        value = value.replace(/(\d)(?=(\d{3})+(?!\d))/g, "$1."); // Adiciona pontos como separador de milhar
        return "R$ " + value;
    }

    // Evento para Telefone
    document.getElementById("telefone").addEventListener("input", function (e) {
        let cursorPos = e.target.selectionStart;
        let oldLength = e.target.value.length;
        e.target.value = formatTelefone(e.target.value);
        let newLength = e.target.value.length;
        e.target.setSelectionRange(cursorPos + (newLength - oldLength), cursorPos + (newLength - oldLength));
    });

    // Evento para Salário
    document.getElementById("salario").addEventListener("input", function (e) {
        let cursorPos = e.target.selectionStart;
        let oldLength = e.target.value.length;
        e.target.value = formatSalario(e.target.value);
        let newLength = e.target.value.length;
        e.target.setSelectionRange(cursorPos + (newLength - oldLength), cursorPos + (newLength - oldLength));
    });

    // Validação no envio
    document.getElementById("form").addEventListener("submit", function (e) {
        let telefone = document.getElementById("telefone");
        let salario = document.getElementById("salario");

        // Remove caracteres especiais do telefone
        telefone.value = telefone.value.replace(/\D/g, "");
        if (telefone.value.length !== 11) {
            alert("O telefone deve ter exatamente 11 dígitos.");
            telefone.focus();
            e.preventDefault();
            return;
        }

        // Remove "R$ " e formatação do salário, converte para número com ponto
        salario.value = salario.value.replace("R$ ", "").replace(/\./g, "").replace(",", ".");
        if (isNaN(salario.value) || salario.value === "") {
            alert("O salário deve ser um número válido.");
            salario.focus();
            e.preventDefault();
        }
    });
});