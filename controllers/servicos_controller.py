from main import app
from flask import request, render_template, redirect, url_for
from models.conexao import *
from models.servicos_model import *



@app.route("/servicos/inserir", methods=['GET'])
def form_servicos():
    return render_template("/servicos/create_servico.html")

@app.route("/servicos/inserir", methods=['POST'])
def create_servicos():   
    if request.method == 'POST':    
        # Captura os dados do formulário      
        nome = request.form['nome']
        price = request.form['price']
        description = request.form['description']   

        # Cria um novo servico    
        new_servico = Servico(name=nome, price=price, description=description)
        
        # Cria a sessão com o banco de dados
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        db = SessionLocal()
        db.add(new_servico)
        db.commit()
        db.refresh(new_servico)


        db.close()
        

        # Redireciona para o cadastro do servico
        return redirect(url_for('servicos'))