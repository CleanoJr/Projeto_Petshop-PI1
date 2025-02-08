from main import app
from flask import request, render_template, redirect, url_for, session
from models.pet_model import * 
from models.conexao import *

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@app.route("/cliente/inserir", methods=['GET'])
def cliente_return():
    return render_template("/cliente/create_cliente.html")

# Rota para exibir o formulário de cadastro do pet
@app.route("/pet/inserir", methods=['POST'])
def create_pet():
    #recupera o ID do cliente da sessão
    client_id = session.get("cliente_id")
    if not client_id:
        return "Erro: Cliente não encontrado!", 400
    
    name = request.form.getlist("name[]")
    species = request.form.getlist("especie[]")
    breed = request.form.getlist("breed[]")
    birth_date = request.form.getlist("birth_date[]")

    db = SessionLocal()

    for i in range(len(name)):
        new_pet = Pet(
            name=name[i], 
            species=species[i],
            breed=breed[i],
            birth_date=birth_date[i], 
            client_id=client_id
            )
        db.add(new_pet)
           
    db.commit()
    db.refresh(new_pet)
    db.close()

    #Apaga o ID do cliente da sessão
    session.pop("cliente_id", None)

    return redirect(url_for('cliente_return'))


