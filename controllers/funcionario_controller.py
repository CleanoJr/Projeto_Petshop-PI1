from main import app
from flask import request, flash, render_template, redirect, url_for, session
from models.funcionario_model import *
from models.usuario_model import *
from models.conexao import *

@app.route("/funcionarios", methods=['GET'])
def list_employee():
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    funcionarios = db.query(Funcionario).all()  # Busca todos os funcionarios no banco
    usuario = db.query(Usuario).filter(Usuario.id == session['usuario_id']).first()
    nome_usuario = usuario.nome if usuario else 'Usuário'
    db.close()
    return render_template("/funcionarios/lista_funcionario.html", funcionarios=funcionarios, nome_usuario=nome_usuario)

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

    flash("Funcionário cadastrado com sucesso!", "success")
    return redirect(url_for('list_employee'))

@app.route('/funcionarios/editar/<id>', methods=['GET'])
def edit_employee(id):
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    
    funcionario = db.query(Funcionario).filter(Funcionario.employee_id == id).first()
    
    if not employee:
        flash("Funcionário não encontrado!", "danger")
        return redirect(url_for('list_employee'))

    db.close()
    return render_template('funcionarios/edit_funcionario.html', funcionario=funcionario)

@app.route('/funcionarios/atualizar/<id>', methods=['POST'])
def update_employee(id):
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    
    try:
        funcionario = db.query(Funcionario).filter_by(employee_id = id).first()
        if not funcionario:
            flash("Funcionário não encontrado!", "danger")
            return redirect(url_for('listar_clientes'))
        
        funcionario.name = request.form['nome']
        funcionario.role = request.form['cargo']
        funcionario.phone = request.form['telefone']   
        funcionario.salary = request.form['salario']
    
        db.commit()
        flash("Funcionário atualizado com sucesso!", "success")
        return redirect(url_for('list_employee'))

    except Exception as e:
        db.rollback()
        flash(f"Erro ao atualizar Funcionário: {e}", "danger")
        return redirect(url_for('list_employee'))

    finally:
        db.close()

@app.route('/funcionarios/delete/<id>', methods=['POST'])
def delete_employee(id):
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    try:
        employee = db.query(Funcionario).filter_by(employee_id=id).first()
        if not employee:
            return {"message": "Funcionario não encontrado!"}, 404
        
        db.delete(employee)
        db.commit()

        flash("Funcionario deletado com sucesso!", "success")
        return redirect(url_for('list_employee'))  # Redireciona para a página de listagem

    except Exception as e:
        db.rollback()
        return f"Erro ao excluir o funcionário: {e}", 500
    
    finally:
        db.close()