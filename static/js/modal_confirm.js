// Guardar referência ao formulário
const deleteForm = document.getElementById('deleteForm');

// Quando o botão "Sim, excluir" for clicado
document.getElementById('confirmDeleteBtn').addEventListener('click', function() {
    // Envia o formulário
    deleteForm.submit();
});
// Caso o usuário cancele ou feche o modal, não faça nada
document.getElementById('deleteBtn').addEventListener('click', function() {
    // Exibe o modal de confirmação
    $('#confirmDeleteModal').modal('show');
});
