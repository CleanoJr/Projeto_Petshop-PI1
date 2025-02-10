let petCount = 1; // Começa com 1 porque já temos um pet inicial
    
        document.getElementById("addPet").addEventListener("click", function() {
            petCount++; // Incrementa o contador de pets
    
            let petGroup = document.querySelector(".pet-group").cloneNode(true); // Clona o formulário
            petGroup.querySelectorAll("input").forEach(input => input.value = ""); // Limpa os inputs
            
            // Atualiza o título do novo pet
            petGroup.querySelector(".pet-title").textContent = `Pet ${petCount}`;
    
            // Mostra o botão de remover no novo pet
            let removeButton = petGroup.querySelector(".removePet");
            removeButton.style.display = "block";
    
            // Adiciona evento para remover o pet específico
            removeButton.addEventListener("click", function() {
                petGroup.remove();
                updatePetTitles(); // Reorganiza a numeração dos pets
            });
    
            document.getElementById("petForms").appendChild(petGroup);
            updatePetTitles(); // Atualiza a numeração dos pets
        });
    
        function updatePetTitles() {
            let petGroups = document.querySelectorAll(".pet-group");
            petGroups.forEach((group, index) => {
                group.querySelector(".pet-title").textContent = `Pet ${index + 1}`;
            });
            petCount = petGroups.length; // Atualiza a contagem de pets
        }