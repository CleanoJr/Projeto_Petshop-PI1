from main import app
from flask import request, render_template, redirect, url_for, session
from models.pet_model import *
from models.cliente_model import *
from models.conexao import *
from models.usuario_model import Usuario


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@app.route("/pets", methods=["GET"])
def listar_pets():
    db = SessionLocal()
    
    # Faz um JOIN entre Pet e Cliente para buscar o nome do dono
    pets = db.query(Pet, Cliente.name).join(Cliente, Pet.client_id == Cliente.client_id).all()
    
    db.close()
    
    return render_template("/pet/pet.html", pets=pets)

@app.route("/pet", methods=['GET'])
def pet_list():
    
    # Coleta do nome de usuaro da sessão	
    if 'usuario_id' not in session:
        return redirect(url_for('login'))

    db = SessionLocal()
    usuario = db.query(Usuario).filter(Usuario.id == session['usuario_id']).first()
    nome_usuario = usuario.nome if usuario else 'Usuário'
    
    
    return render_template("/pet/pet.html", nome_usuario=nome_usuario)

@app.route("/cliente", methods=['GET'])
def cliente_return():
    return render_template("/cliente/lista.cliente.html")

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


