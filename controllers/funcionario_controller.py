from main import app
from flask import request, flash, render_template, redirect, url_for, session
from sqlalchemy.exc import IntegrityError
from models.cliente_model import *
from models.conexao import *

@app.route("/funcionario/inserir", methods=['GET'])
def funcionario():
    return render_template("/funcionarios/create_funcionario.html")