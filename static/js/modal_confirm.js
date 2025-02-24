document.addEventListener("DOMContentLoaded", function () {
    var deleteModal = document.getElementById('confirmDeleteModal');
    
    deleteModal.addEventListener('show.bs.modal', function (event) {
        var button = event.relatedTarget; // Botão que acionou o modal
        var itemId = button.getAttribute('data-item-id'); // Obtém o ID
        var itemType = button.getAttribute('data-item-type'); // Obtém o tipo (cliente ou pet)
        var deleteForm = document.getElementById('deleteForm');

        // Define a URL correta com base no tipo do item
        deleteForm.action = `/${itemType}/delete/${itemId}`;
    });
});
