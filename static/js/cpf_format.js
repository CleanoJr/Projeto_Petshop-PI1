// Formatação dinâmica do CPF
document.getElementById("cpf").addEventListener("input", function (e) {
    let value = e.target.value.replace(/\D/g, ""); // Remove tudo que não for número
    value = value.slice(0, 11); // Limita a 11 dígitos

    let formattedValue = value;
    if (value.length > 3 && value.length <= 6) {
        formattedValue = value.slice(0, 3) + "." + value.slice(3);
    } else if (value.length > 6 && value.length <= 9) {
        formattedValue = value.slice(0, 3) + "." + value.slice(3, 6) + "." + value.slice(6);
    } else if (value.length > 9) {
        formattedValue =
            value.slice(0, 3) +
            "." +
            value.slice(3, 6) +
            "." +
            value.slice(6, 9) +
            "-" +
            value.slice(9, 11);
    }

    e.target.value = formattedValue;
});

// Formatação dinâmica do telefone
document.getElementById("telefone").addEventListener("input", function (e) {
    let value = e.target.value.replace(/\D/g, ""); // Remove tudo que não for número
    value = value.slice(0, 11); // Limita a 11 dígitos

    let formattedValue = value;
    if (value.length > 2 && value.length <= 6) {
        formattedValue = `(${value.slice(0, 2)}) ${value.slice(2)}`;
    } else if (value.length > 6) {
        formattedValue = `(${value.slice(0, 2)}) ${value.slice(2, 3)} ${value.slice(3, 7)}-${value.slice(7)}`;
    }

    e.target.value = formattedValue;
});

// Remover formatação antes de enviar
document.getElementById("form").addEventListener("submit", function (e) {
    const cpfInput = document.getElementById("cpf");
    const telefoneInput = document.getElementById("telefone");

    // Remove a formatação do CPF (deixa apenas números)
    cpfInput.value = cpfInput.value.replace(/\D/g, "");

    // Remove a formatação do telefone (deixa apenas números)
    telefoneInput.value = telefoneInput.value.replace(/\D/g, "");
});