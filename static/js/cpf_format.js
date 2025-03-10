function formatCPF(value) {
    value = value.replace(/\D/g, "").slice(0, 11);

    if (value.length > 9) {
        return value.replace(/(\d{3})(\d{3})(\d{3})(\d{2})/, "$1.$2.$3-$4");
    } else if (value.length > 6) {
        return value.replace(/(\d{3})(\d{3})(\d{0,3})/, "$1.$2.$3");
    } else if (value.length > 3) {
        return value.replace(/(\d{3})(\d{0,3})/, "$1.$2");
    }
    return value;
}

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

document.getElementById("cpf").addEventListener("input", function (e) {
    let cursorPos = e.target.selectionStart;
    let oldLength = e.target.value.length;
    e.target.value = formatCPF(e.target.value);
    let newLength = e.target.value.length;
    e.target.setSelectionRange(cursorPos + (newLength - oldLength), cursorPos + (newLength - oldLength));
});

document.getElementById("telefone").addEventListener("input", function (e) {
    let cursorPos = e.target.selectionStart;
    let oldLength = e.target.value.length;
    e.target.value = formatTelefone(e.target.value);
    let newLength = e.target.value.length;
    e.target.setSelectionRange(cursorPos + (newLength - oldLength), cursorPos + (newLength - oldLength));
});

document.getElementById("form").addEventListener("submit", function (e) {
    let cpf = document.getElementById("cpf");
    let telefone = document.getElementById("telefone");

    // Remove os caracteres especiais antes de enviar
    cpf.value = cpf.value.replace(/\D/g, "");
    telefone.value = telefone.value.replace(/\D/g, "");

    if (cpf.value.length !== 11) {
        alert("O CPF deve ter exatamente 11 dígitos.");
        cpf.focus();
        e.preventDefault();
    }

    if (telefone.value.length !== 11) {
        alert("O telefone deve ter exatamente 11 dígitos.");
        telefone.focus();
        e.preventDefault();
    }
});