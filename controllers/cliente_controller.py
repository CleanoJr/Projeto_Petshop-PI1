from main import app
from flask import request, flash, render_template, redirect, url_for, session
from sqlalchemy.exc import IntegrityError
from models.cliente_model import *
from models.conexao import *


@app.route("/cliente", methods=['GET'])
def listar_clientes():
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    clientes = db.query(Cliente).all()  # Busca todos os clientes no banco
    db.close()
    return render_template("/cliente/lista_cliente.html", clientes=clientes)

@app.route("/cliente/inserir", methods=['GET'])
def cliente():
    return render_template("/cliente/create_cliente.html")

@app.route("/pet/inserir", methods=['GET'])
def pet():
    cliente_id = session.get("cliente_id")
    if not cliente_id:
        flash("Cliente não encontrado!", "error")
        return redirect(url_for('listar_clientes'))
    
    return render_template("/pet/create_pet.html", client_id=cliente_id)

@app.route("/cliente/inserir", methods=['POST'])
def create_client():
    try:
        if request.method == 'POST':    
            # Captura os dados do formulário      
            nome = request.form['nome']
            cpf = request.form['cpf']
            email = request.form['email']   
            endereco = request.form['endereco']   
            telefone = request.form['telefone']

            # Cria um novo cliente      
            new_client = Cliente(name=nome, cpf=cpf, email=email, phone=telefone, address=endereco)
            
            # Cria a sessão com o banco de dados
            SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
            db = SessionLocal()
            db.add(new_client)
            db.commit()
            db.refresh(new_client)

            # Salva o ID do cliente na sessão
            session["cliente_id"] = new_client.client_id

            # Redireciona para o cadastro do pet
            return redirect(url_for('pet'))
        
    except IntegrityError as e:
        if "Duplicate entry" in str(e.orig):
            flash("Erro: CPF já cadastrado!", "danger")
        else:
            flash("Erro ao cadastrar cliente. Tente novamente.", "danger")
        return redirect(url_for("cliente"))

    except Exception as e:
        flash("Ocorreu um erro inesperado: {}".format(str(e)), "danger")
        return redirect(url_for("cliente"))
    
    finally:
        db.close()

@app.route('/cliente/editar/<int:id>', methods=['GET'])
def editar_cliente(id):
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    try:
        cliente = db.query(Cliente).filter_by(client_id=id).first()
        if not cliente:
            flash("Cliente não encontrado!", "danger")
            return redirect(url_for('listar_clientes'))

        return render_template('cliente/editar_cliente.html', cliente=cliente)

    finally:
        db.close()

@app.route('/cliente/atualizar/<int:id>', methods=['POST'])
def atualizar_cliente(id):
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    try:
        cliente = db.query(Cliente).filter_by(client_id=id).first()
        if not cliente:
            flash("Cliente não encontrado!", "danger")
            return redirect(url_for('listar_clientes'))

        # Pegando os dados do formulário
        cliente.name = request.form['nome']
        cliente.cpf = request.form['cpf']
        cliente.email = request.form['email']
        cliente.address = request.form['endereco']
        cliente.phone = request.form['telefone']

        db.commit()
        flash("Cliente atualizado com sucesso!", "success")
        return redirect(url_for('listar_clientes'))

    except Exception as e:
        db.rollback()
        flash(f"Erro ao atualizar cliente: {e}", "danger")
        return redirect(url_for('listar_clientes'))

    finally:
        db.close()

@app.route('/cliente/delete/<int:id>', methods=['POST'])
def delete_cliente(id):
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    try:
        cliente = db.query(Cliente).get(id)
        if not cliente:
            return {"message": "Cliente não encontrado!"}, 404
        
        db.delete(cliente)
        db.commit()

        flash("Cliente deletado com sucesso!", "success")
        return redirect(url_for('listar_clientes'))  # Redireciona para a página de listagem

    except Exception as e:
        db.rollback()
        return f"Erro ao excluir o cliente: {e}", 500
    
    finally:
        db.close()