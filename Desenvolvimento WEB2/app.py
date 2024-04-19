from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from  datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contatos.db'
db = SQLAlchemy(app)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)
    data_criacao = db.Column(db.DateTime, default = datetime.utcnow)
    
    def __repr__(self):
        return f'<Usuario {self.nome}>'

if __name__ == '__main__':
    app.run(debug=True)
    novo_usuario = Usuario(nome='Maxwell', email='maxwellchaves1844@gmail.com')
    db.session.add(novo_usuario)
    db.session.commit()
    