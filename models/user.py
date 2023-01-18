from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(60))
    telefone = db.Column(db.String(15))
    endereco = db.Column(db.String(100))
    cpf = db.Column(db.String(11))
    sexo = db.Column(db.String(10))

    def serialize(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "telefone": self.telefone,
            "endereco": self.endereco,
            "cpf": self.cpf,
            "sexo": self.sexo,
        }
