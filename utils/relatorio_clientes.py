from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from models.cliente_model import Cliente
from models.conexao import engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# Funções de formatação
def formatar_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))
    if len(cpf) == 11:
        return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
    return cpf

def formatar_telefone(telefone):
    telefone = ''.join(filter(str.isdigit, telefone))
    if len(telefone) >= 10:
        return f"({telefone[:2]}) {telefone[2:7]}-{telefone[7:]}"
    return telefone

def gerar_relatorio_clientes(nome_arquivo="relatorio_clientes.pdf"):
    # Configura o PDF
    doc = SimpleDocTemplate(nome_arquivo, pagesize=A4, leftMargin=10*mm, rightMargin=10*mm, topMargin=10*mm, bottomMargin=10*mm)
    elementos = []
    styles = getSampleStyleSheet()
    prm_color = colors.HexColor("#D2811E")  # Cor primária

    # Cabeçalho
    logo = Image('static/assets/logo_horizontal.png', width=100, height=30)
    elementos.append(logo)
    elementos.append(Spacer(1, 5*mm))

    # Título "Relatório de Clientes"
    titulo = Paragraph("Relatório de Clientes", styles['Heading1'])
    elementos.append(titulo)
    elementos.append(Spacer(1, 2*mm))

    # Total de clientes e data de geração
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    try:
        clientes = db.query(Cliente).all()
        total_clientes = len(clientes)
        data_geracao = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        info_cabecalho = Paragraph(
            f"Total de Clientes: {total_clientes}<br/>Data de Geração: {data_geracao}",
            styles['Normal']
        )
        elementos.append(info_cabecalho)
        elementos.append(Spacer(1, 5*mm))

        # Linha divisória
        elementos.append(Paragraph("<hr>", styles['Normal']))

        # Tabela de clientes
        dados = [["Nome", "CPF", "Telefone", "Email"]]
        for cliente in clientes:
            dados.append([
                cliente.name,
                formatar_cpf(cliente.cpf),
                formatar_telefone(cliente.phone),
                cliente.email
            ])

        # Tabela estilizada
        tabela = Table(dados, colWidths=[200, 100, 100, 150])
        tabela.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), prm_color),        # Fundo laranja no cabeçalho
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),     # Texto branco no cabeçalho
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Negrito no cabeçalho
            ('FONTSIZE', (0, 0), (-1, -1), 10),               # Tamanho da fonte
            ('GRID', (0, 0), (-1, -1), 0.5, colors.black),    # Bordas pretas
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),              # Alinhamento à esquerda
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),           # Alinhamento vertical
            ('LEFTPADDING', (0, 0), (-1, -1), 5),             # Espaçamento interno
            ('RIGHTPADDING', (0, 0), (-1, -1), 5),
            ('BACKGROUND', (0, 1), (-1, -1), colors.white),   # Fundo branco nas linhas de dados
        ]))
        elementos.append(tabela)

    finally:
        db.close()

    # Rodapé personalizado
    def footer(canvas, doc):
        canvas.saveState()
        canvas.setFont('Helvetica-Oblique', 8)
        y = 15*mm

        # Ícones e texto
        canvas.drawImage('static/assets/icons/whatsapp.png', 10*mm, y, 5*mm, 5*mm)
        canvas.drawString(16*mm, y+1*mm, "WhatsApp: (XX) XXXXX-XXXX")
        canvas.drawImage('static/assets/icons/instagram.png', 60*mm, y, 5*mm, 5*mm)
        canvas.drawString(66*mm, y+1*mm, "Instagram: @clinica_veterinaria")
        canvas.drawImage('static/assets/icons/email.png', 110*mm, y, 5*mm, 5*mm)
        canvas.drawString(116*mm, y+1*mm, "Email: contato@clinicaveterinaria.com")
        canvas.drawImage('static/assets/icons/endereco.png', 10*mm, y-5*mm, 5*mm, 5*mm)
        canvas.drawString(16*mm, y-4*mm, "Endereço: Rua Exemplo, 123, Bairro, Cidade - Estado")

        # Barra inferior
        canvas.setFillColor(prm_color)
        canvas.rect(0, 0, A4[0], 8*mm, fill=1, stroke=0)
        canvas.restoreState()

    # Gera o PDF com rodapé (sem marca d'água)
    doc.build(elementos, onFirstPage=footer, onLaterPages=footer)