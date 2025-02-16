// Seleciona elementos do DOM
const btnEdit = document.getElementById("btnEdit");
const editProfileModal = new bootstrap.Modal(document.getElementById("editProfileModal"));
const formEditProfile = document.getElementById("formEditProfile");

const profileName = document.getElementById("profileName");
const profileBio = document.getElementById("profileBio");
const profileEmail = document.getElementById("profileEmail");
const profilePhone = document.getElementById("profilePhone");
const profileAddress = document.getElementById("profileAddress");

const editName = document.getElementById("editName");
const editBio = document.getElementById("editBio");
const editEmail = document.getElementById("editEmail");
const editPhone = document.getElementById("editPhone");
const editAddress = document.getElementById("editAddress");

// Mostra o modal de edição de perfil
btnEdit.addEventListener("click", () => {
    // Preenche o formulário com os valores atuais
    editName.value = profileName.textContent;
    editBio.value = profileBio.textContent;
    editEmail.value = profileEmail.textContent;
    editPhone.value = profilePhone.textContent;
    editAddress.value = profileAddress.textContent;

    editProfileModal.show();
});

// Salva as alterações do perfil
formEditProfile.addEventListener("submit", (e) => {
    e.preventDefault();

    // Atualiza os valores do perfil
    profileName.textContent = editName.value;
    profileBio.textContent = editBio.value;
    profileEmail.textContent = editEmail.value;
    profilePhone.textContent = editPhone.value;
    profileAddress.textContent = editAddress.value;

    editProfileModal.hide();
});

// Lógica para editar pets
const petsList = document.getElementById("petsList");
const btnAddPet = document.getElementById("btnAddPet");
const editPetModal = new bootstrap.Modal(document.getElementById("editPetModal"));
const formEditPet = document.getElementById("formEditPet");

const editPetName = document.getElementById("editPetName");
const editPetType = document.getElementById("editPetType");
const editPetAge = document.getElementById("editPetAge");

let currentPet = null;




// Função para adicionar ou editar um pet
function savePet(e) {
    e.preventDefault();

    const pet = {
        name: editPetName.value,
        type: editPetType.value,
        age: editPetAge.value,
        image: editPetImage.files[0] ? URL.createObjectURL(editPetImage.files[0]) : "cachorro.jpg", // Imagem padrão caso não seja selecionada
    };

    if (currentPet) {
        // Edita o pet existente
        currentPet.querySelector("h3").textContent = pet.name;
        currentPet.querySelector("p:nth-child(2)").textContent = `Raça: ${pet.type}`;
        currentPet.querySelector("p:nth-child(3)").textContent = `Idade: ${pet.age} anos`;
        currentPet.querySelector(".pet-avatar").src = pet.image;
    } else {
        // Adiciona um novo pet
        const petCard = document.createElement("div");
        petCard.className = "col-md-4 mb-3";
        petCard.innerHTML = `
            <div class="card">
                <img src="${pet.image}" alt="${pet.name}" class="pet-avatar">
                <div class="card-body">
                    <h3>${pet.name}</h3>
                    <p><strong>Raça:</strong> ${pet.type}</p>
                    <p><strong>Idade:</strong> ${pet.age} anos</p>
                    <button class="btn btn-sm btn-warning me-2 btn-edit-pet">Editar</button>
                    <button class="btn btn-sm btn-danger btn-delete-pet">Excluir</button>
                </div>
            </div>
        `;
        petsList.appendChild(petCard);
    }

    editPetModal.hide();
    formEditPet.reset();
    currentPet = null;
}

// Adiciona um novo pet
btnAddPet.addEventListener("click", () => {
    currentPet = null;
    editPetModal.show();
});

// Edita ou exclui um pet
petsList.addEventListener("click", (e) => {
    if (e.target.classList.contains("btn-edit-pet")) {
        currentPet = e.target.closest(".col-md-4");
        const petName = currentPet.querySelector("h3").textContent;
        const petType = currentPet.querySelector("p:nth-child(2)").textContent.replace("Raça: ", "");
        const petAge = currentPet.querySelector("p:nth-child(3)").textContent.replace("Idade: ", "").replace(" anos", "");
        const petImage = currentPet.querySelector(".pet-avatar").src;

        editPetName.value = petName;
        editPetType.value = petType;
        editPetAge.value = petAge;
        editPetImage.value = ""; // Limpa o input de arquivo

        editPetModal.show();
    }

    if (e.target.classList.contains("btn-delete-pet")) {
        e.target.closest(".col-md-4").remove();
    }
});

// Salva as alterações do pet
formEditPet.addEventListener("submit", savePet);