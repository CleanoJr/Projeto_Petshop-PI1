from main import app
from flask import request, flash, render_template, redirect, url_for, session
from models.pet_model import *
from models.cliente_model import *
from models.conexao import *

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@app.route("/pets", methods=["GET"])
def listar_pets():
    db = SessionLocal()
    
    # Faz um JOIN entre Pet e Cliente para buscar o nome do dono
    pets = db.query(Pet, Cliente.name).join(Cliente, Pet.client_id == Cliente.client_id).all()
    
    db.close()
    
    return render_template("/pet/lista_pet.html", pets=pets)

@app.route("/cliente", methods=['GET'])
def cliente_return():
    return render_template("/cliente/lista.cliente.html")

# Rota para exibir o formulário de cadastro do pet
@app.route("/pet/inserir", methods=['POST'])
def create_pet():
    
    #recupera o ID do cliente da sessão
    client_id = session.get("cliente_id")
    if not client_id:
        flash("Cliente não encontrado!", "error")
        return redirect(url_for('cliente_return'))
    
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

    flash("Cliente e pets cadastrados com sucesso!", "success")
    return redirect(url_for('cliente_return'))

@app.route('/pet/editar/<int:id>', methods=['GET'])
def editar_pet(id):
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    
    pet = db.query(Pet).filter(Pet.pet_id == id).first()
    clients = db.query(Cliente).all()  # Buscar todos os clientes
    
    if not pet:
        flash("Pet não encontrado!", "danger")
        return redirect(url_for('listar_pets'))

    db.close()
    return render_template('pet/editar_pet.html', pet=pet, clients=clients)

@app.route('/pet/atualizar/<int:id>', methods=['POST'])
def atualizar_pet(id):
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()

    pet = db.query(Pet).filter(Pet.pet_id == id).first()
    if not pet:
        flash("Pet não encontrado!", "danger")
        return redirect(url_for('listar_pets'))

    # Atualizar os dados do pet
    pet.name = request.form['name']
    pet.species = request.form['species']
    pet.breed = request.form['breed']
    pet.birth_date = request.form['birth_date']
    pet.client_id = request.form['client_id']  # ou outro campo de cliente, se necessário.

    try:
        db.commit()
        flash("Pet atualizado com sucesso!", "success")
        return redirect(url_for('listar_pets'))
    except Exception as e:
        db.rollback()
        flash(f"Erro ao atualizar o pet: {e}", "danger")
        return redirect(url_for('listar_pets'))
    finally:
        db.close()

@app.route('/pet/delete/<int:id>', methods=['POST'])
def delete_pet(id):
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    try:
        pet = db.query(Pet).filter_by(pet_id=id).first()
        if not pet:
            return {"message": "Pet não encontrado!"}, 404
        
        db.delete(pet)
        db.commit()

        flash("Pet deletado com sucesso!", "success")
        return redirect(url_for('listar_pets'))  # Redireciona para a página de listagem

    except Exception as e:
        db.rollback()
        return f"Erro ao excluir o pet: {e}", 500
    
    finally:
        db.close()


