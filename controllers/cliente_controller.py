from main import app
from flask import request, render_template, redirect, url_for, session
from models.cliente_model import *
from models.conexao import *
from models.usuario_model import Usuario


@app.route("/cliente", methods=['GET'])
def listar_clientes():
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    
    # Coleta do nome de usuaro da sessão	
    if 'usuario_id' not in session:
        return redirect(url_for('login'))

    db = SessionLocal()
    usuario = db.query(Usuario).filter(Usuario.id == session['usuario_id']).first()
    nome_usuario = usuario.nome if usuario else 'Usuário'
    
    clientes = db.query(Cliente).all()  # Busca todos os clientes no banco
    db.close()
    return render_template("/cliente/lista_cliente.html", clientes=clientes, nome_usuario=nome_usuario)

@app.route("/cliente/inserir", methods=['GET'])
def cliente():
    return render_template("/cliente/create_cliente.html")

@app.route("/pet/inserir", methods=['GET'])
def pet():
    cliente_id = session.get("cliente_id")
    if not cliente_id:
        return "Erro: Cliente não encontrado!", 400
    return render_template("/pet/create_pet.html", client_id=cliente_id)

@app.route("/cliente/inserir", methods=['POST'])
def create_client():   
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

        db.close()
        

        # Redireciona para o cadastro do pet
        return redirect(url_for('pet'))