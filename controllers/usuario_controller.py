from main import app
from flask import render_template

# Rotas
@app.route('/')
def index():
    return render_template('login.html')