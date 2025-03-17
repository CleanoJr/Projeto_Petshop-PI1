from main import app
from flask import request, flash, render_template, redirect, url_for, session
from sqlalchemy.exc import IntegrityError
from models.funcionario_model import *
from models.conexao import *

@app.route("/funcionario/inserir", methods=['GET'])
def employee():
    return render_template("/funcionarios/create_funcionario.html")

@app.route("/funcionario/inserir", methods=['POST'])
def create_employee():
    try:
        if request.method == 'POST':    
            # Captura os dados do formulário      
            name = request.form['nome']
            role = request.form['cargo']
            phone = request.form['telefone']   
            salary = request.form['salario']

            new_employee = Funcionario(name=name, role=role, phone=phone, salary=salary)

            SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
            db = SessionLocal()
            db.add(new_employee)
            db.commit()
            db.refresh(new_employee)

    except Exception as e:
        flash("Ocorreu um erro inesperado: {}".format(str(e)), "danger")
        return redirect(url_for("employee"))
    
    finally:
        db.close

    return redirect(url_for('employee'))