from main import app
from flask import request, render_template, redirect, url_for, session
from models.pet_model import * 
from models.conexao import *

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Rota para exibir o formulário de cadastro do pet
@app.route("/pet/inserir")
def pet():
    print("Sessão atual:", session)
    client_id = session.get("client_id")
    if not client_id:
        return "Erro: Cliente não encontrado!", 400
    return render_template("/pet/create_pet.html", client_id=client_id)

@app.route("/pet/inserir", methods=['POST'])
def create_pet():
    client_id = session.get("client_id")
    if not client_id:
        return "Erro: Cliente não encontrado!", 400

    name = request.form['name']
    species = request.form['species']
    breed = request.form['breed']
    birth_date = request.form['birth_date']

    new_pet = Pet(name=name, species=species, breed=breed, birth_date=birth_date, client_id=client_id)

    db = SessionLocal()
    db.add(new_pet)
    db.commit()
    db.refresh(new_pet)

    return redirect(url_for('cadastrar_novamente'))


