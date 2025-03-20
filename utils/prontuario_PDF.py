import csv
from fpdf import FPDF, XPos, YPos
from fpdf.fonts import FontFace
from fpdf.enums import TableCellFillMode
from datetime import datetime

class PDF(FPDF):
    def __init__(self):
        super().__init__()
        self.paciente = ""
        self.tutor = ""
        self.raca = ""
        self.especie = ""
        self.peso = ""
        self.sexo = ""
        self.nascimento = ""
        self.data_consulta = ""
        self.conteudo = ""
        self.prm_color = "#FFD300"

    def add_watermark(self):
        # Caminho para a logo
        logo_path = 'static/assets/logo_watermark.png'
        
        # Dimensões da página
        page_width = self.w
        page_height = self.h
        
        # Tamanho da marca d'água (ajuste conforme necessário)
        watermark_width = 100  # Largura da imagem
        watermark_height = 100  # Altura da imagem
        
        # Calcula a posição central
        x_position = (page_width - watermark_width) / 2
        y_position = (page_height - watermark_height) / 2
        
        # Adiciona a imagem ao centro da página
        self.image(logo_path, x=x_position, y=y_position, w=watermark_width, h=watermark_height)

    def header(self):       
        
        self.add_watermark()
        
        # Váriaveis de altura e largura
        h_label = 10
        h_conteudo = h_label - 1
        h_linhas = h_label - 3
        h_logo = 30
        
        # Logo
        self.image('static/assets/logo.jpg', 10, 8, 0, h_logo)
        
        # Titulo
        self.set_font('Helvetica', 'B', 16)
        self.set_text_color(self.prm_color)
        self.cell(80)        
        title = "Ficha de Prontuário"
        width = self.get_string_width(title) + 6
        self.set_y(h_logo / 2)
        self.set_x((self.w - width) / 2)
        self.cell(width, 10, title, border=0, align='C', new_x=XPos.LMARGIN)
        self.set_y(h_logo + 10)
        self.cell(0, 1, '', border='B')
        self.ln(2)
        
        
        def add_label(texto: str):
            self.set_font('', 'B', 14)
            self.set_text_color(self.prm_color)
            width = self.get_string_width(texto)
            return self.cell(width, h_label, f"{texto}: ", new_x=XPos.END)
        
        def add_texto(texto: str, complemento: str = ''):
            self.set_font('', '', 12)
            self.set_text_color(0)
            return self.cell(None, h_conteudo, f"{texto} {complemento}", new_x=XPos.START)
        
        # Calcular idade do animal
        def calcular_idade():
            data_nasc = datetime.strptime(self.nascimento, "%d/%m/%Y")
            data_cons = datetime.strptime(self.data_consulta, "%d/%m/%Y")
            idade = data_cons - data_nasc
            idade = int(idade.days / 365.25)
            return idade
        
        # Adiciona informações adicionais no cabeçalho
        
        # Nome do Paciente
        add_label('Paciente')
        add_texto(self.paciente)
        self.cell(85 - self.get_string_width("Paciente :"), h_linhas, '', border='B', new_x=XPos.RIGHT)
        self.cell(5)
        
        # Espécie
        add_label('Espécie')
        add_texto(self.especie)
        self.cell(40 - self.get_string_width("Especie :"), h_linhas, '', border='B', new_x=XPos.RIGHT)
        self.cell(5)
        
        # Sexo
        add_label('Sexo')
        add_texto(self.sexo)
        self.cell(30 - self.get_string_width("Sexo :"), h_linhas, '', border='B', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        
        # Raça
        add_label('Raça')
        add_texto(self.raca)
        self.cell(87 - self.get_string_width("Raça :"), h_linhas, '', border='B', new_x=XPos.RIGHT)
        self.cell(5)
        
        # Peso
        add_label('Peso')
        add_texto(self.peso, "kg")
        self.cell(15, h_linhas, '', border='B', new_x=XPos.RIGHT)
        self.cell(5)
        
        # Idade
        add_label('Idade')
        add_texto(calcular_idade(), "anos")
        self.cell(15, h_linhas, '', border='B', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        
        # Tutor
        add_label('Tutor')
        add_texto(self.tutor)
        self.cell(0, h_linhas, '', border='B', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        
        self.cell(0, 4, border='B')
        self.ln(10)

    def add_body(self):
        
        self.set_font('', '', 14)
        
        self.set_x(30)
        self.multi_cell(self.w - 35, 10,  self.conteudo, padding=(2, 3, 3), center=True, align='')
        self.ln(10)                    

    def footer(self):
        self.set_y(-22)  # Ajusta a posição vertical do footer
        self.set_font('Helvetica', 'I', 8)
        
        # Função para adicionar espaço entre as células
        def space(size:int = 5):
            return self.cell(size)
        
        # Caminho para os ícones
        whatsapp_icon = 'static/assets/icons/whatsapp.png'
        instagram_icon = 'static/assets/icons/instagram.png'
        email_icon = 'static/assets/icons/email.png'
        address_icon = 'static/assets/icons/endereco.png'
        
        # WhatsApp
        self.image(whatsapp_icon, x=10, y=self.get_y(), w=5)  # Adiciona o ícone
        space()  # Espaço após o ícone
        self.cell(None, 5, 'WhatsApp: (XX) XXXXX-XXXX', align='L', new_x=XPos.RIGHT)
        space()  # Espaço após o texto
        
        # Instagram
        self.image(instagram_icon, y=self.get_y(), w=5)
        space()
        self.cell(None, 5, 'Instagram: @clinica_veterinaria', align='L', new_x=XPos.RIGHT)
        space()
        
        # Email
        
        self.image(email_icon, y=self.get_y(), w=5)
        space()
        self.cell(0, 5, 'Email: contato@clinicaveterinaria.com', align='L', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        
        self.ln(2)
        
        # Endereço
        self.image(address_icon, x=10, y=self.get_y(), w=5)
        space()
        self.cell(0, 5, 'Endereço: Rua Exemplo, 123, Bairro, Cidade - Estado', align='L', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            
        # Barra inferior
        h_barra = 8
        self.set_y(0 - h_barra)
        self.set_fill_color(self.prm_color) 
        self.set_x(0)
        self.cell(self.w, h_barra, '', fill=True)