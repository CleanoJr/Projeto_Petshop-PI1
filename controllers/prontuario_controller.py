from flask import Blueprint, render_template, request, redirect, url_for, send_file, Response
from models.prontuario_model import Prontuario
from models.conexao import *
from utils.prontuario_PDF import PDF
from datetime import datetime

prontuario_bp = Blueprint('prontuario', __name__)

@prontuario_bp.route('/', methods=['GET'])
def form_prontuario():
    # Renderiza o template do formulário
    return render_template('prontuarios/novo_prontuario.html')

@prontuario_bp.route('/prontuario/novo', methods=['GET', 'POST'])
def novo_prontuario():
    if request.method == 'POST':
        # Captura os dados do formulário
        paciente = request.form['paciente']
        tutor = request.form['tutor']
        raca = request.form['raca']
        especie = request.form['especie']
        peso = request.form['peso']
        sexo = request.form['sexo']
        
        # Converte as datas do formato ISO para objetos datetime
        nascimento = datetime.strptime(request.form['nascimento'], '%Y-%m-%d')
        data_consulta = datetime.strptime(request.form['data_consulta'], '%Y-%m-%d')
        
        conteudo = request.form['conteudo']

        # Salva os dados no banco de dados
        novo_prontuario = Prontuario(
            paciente=paciente,
            tutor=tutor,
            raca=raca,
            especie=especie,
            peso=peso,
            sexo=sexo,
            nascimento=nascimento,
            data_consulta=data_consulta,
            conteudo=conteudo
        )
        
        db = SessionLocal()
        db.add(novo_prontuario)
        db.commit()
            
        
        # Gera o PDF com os dados do formulário
        pdf = PDF()
        pdf.paciente = paciente
        pdf.tutor = tutor
        pdf.raca = raca
        pdf.especie = especie
        pdf.peso = peso
        pdf.sexo = sexo
        pdf.nascimento = nascimento.strftime('%d/%m/%Y')  # Formata para o PDF
        pdf.data_consulta = data_consulta.strftime('%d/%m/%Y')  # Formata para o PDF
        pdf.conteudo = conteudo
                
        pdf.add_page()
        pdf.add_body()
        pdf.output("Prontuario.pdf")

        # Retorna o PDF para download
        # return send_file("Prontuario.pdf", as_attachment=True)
    
        # Salva o PDF em memória
        pdf_output = bytes(pdf.output(dest='S'))  # Gera o PDF como string em memória

        # Retorna o PDF para exibição no navegador
        response = Response(pdf_output, mimetype='application/pdf')
        response.headers['Content-Disposition'] = 'inline; filename=Prontuario.pdf'
        return response

    return redirect(url_for('prontuario.form_prontuario'))    