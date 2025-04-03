from main import app
from flask import request, flash, render_template, redirect, url_for
from models.conexao import *
from models.servicos_model import *

@app.route("/servicos", methods=['GET'])
def servicos():
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    servicos = db.query(Servico).all()
    db.close()
    return render_template("/servicos/servicos.html", servicos=servicos)

@app.route("/servicos/inserir", methods=['GET'])
def form_servicos():
    return render_template("/servicos/create_servico.html")

@app.route("/servicos/inserir", methods=['POST'])
def create_servicos():   
    try:
        if request.method == 'POST':
                  
            nome = request.form['name']
            price = request.form['price']
            description = request.form['description']   

            # Cria um novo servico    
            new_service = Servico(name=nome, price=price, description=description)
            
            SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
            db = SessionLocal()
            db.add(new_service)
            db.commit()
            db.refresh(new_service)

    except Exception as e:
        flash("Ocorreu um erro inesperado: {}".format(str(e)), "danger")
        return redirect(url_for("form_servicos"))
    
    finally:
        db.close
        

    flash("Serviço cadastrado com sucesso!", "success")
    return redirect(url_for('form_servicos'))