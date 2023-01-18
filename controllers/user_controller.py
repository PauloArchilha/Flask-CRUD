import json
from flask import request, Response
from models.user import db, User


def index():
    session = db.session()
    users = session.query(User).all()
    users_json = [user.serialize() for user in users]
    session.close()
    return Response(json.dumps(users_json))


def store():
    session = db.session()
    body = request.get_json()
    try:
        user = User(nome=body['nome'], telefone=body['telefone'],
                    endereco=body['endereco'], cpf=body['cpf'], sexo=body['sexo'])
        session.add(user)
        session.commit()
        return Response(json.dumps([user.serialize()]))
    except Exception as e:
        session.rollback()
        return {'Error': str(e)}
    finally:
        session.close()


def update(user_id):
    session = db.session()
    body = request.get_json()
    try:
        user = session.query(User).get(user_id)
        if body and body['nome']:
            user.nome = body['nome']
        if body and body['telefone']:
            user.telefone = body['telefone']
        if body and body['endereco']:
            user.endereco = body['endereco']
        if body and body['cpf']:
            user.cpf = body['cpf']
        if body and body['sexo']:
            user.sexo = body['sexo']
        session.commit()
        return Response(json.dumps([user.serialize()]))
    except Exception as e:
        session.rollback()
        return {'Error': str(e)}
    finally:
        session.close()


def show(user_id):
    session = db.session()
    try:
        user = session.query(User).get(user_id)
        if user is None:
            return {'Error': 'User not found'}
        return Response(json.dumps([user.serialize()]))
    except Exception as e:
        session.rollback()
        return {'Error': str(e)}
    finally:
        session.close()


def delete(user_id):
    session = db.session()
    try:
        user = session.query(User).get(user_id)
        if user is None:
            return {'Error': 'User not found'}
        session.delete(user)
        session.commit()
        return {'Success': 'User deleted'}
    except Exception as e:
        session.rollback()
        return {'Error': str(e)}
    finally:
        session.close()
