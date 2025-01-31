document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Impede o envio padrão do formulário

    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    // Aqui você pode adicionar a lógica para autenticação
    if (email === "usuario@example.com" && password === "senha") {
        alert("Login bem-sucedido!");
        // Redirecionar ou carregar a página principal
        window.location.href = "home.html";
    } else {
        alert("Email ou senha incorretos. Tente novamente.");
    }
});
