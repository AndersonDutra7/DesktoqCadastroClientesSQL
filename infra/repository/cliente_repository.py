from infra.configs.connection import DBConnectionHandler
from infra.entities.cliente import Cliente
import traceback

class ClientesRepository:

    def select(self, cpf):
        with DBConnectionHandler() as db:
            return db.session.query(Cliente).filter(Cliente.cpf == cpf).first()


    def select_all(self):
        with DBConnectionHandler() as db:
            data = db.session.query(Cliente).all()
            return data

    def insert(self, cliente):
        with DBConnectionHandler() as db:
            try:
                db.session.add(cliente)
                db.session.commit()
                return 'Ok'
            except Exception as e:
                db.session.rollback()
                traceback.print_exc()
                return str(e)

    def delete(self, cpf):
        with DBConnectionHandler() as db:
            try:
                db.session.query(Cliente).filter(Cliente.cpf == cpf).delete()
                db.session.commit()
                return "Ok"
            except Exception as e:
                db.session.rollback()
            return str(e)

    def update(self, cliente):
        with DBConnectionHandler() as db:
            db.session.commit()
            try:
                db.session.query(Cliente).filter(Cliente.cpf == cliente.cpf).update({Cliente.nome_cliente: cliente.nome_cliente, Cliente.telefone_fixo: cliente.telefone_fixo, Cliente.telefone_celular: cliente.telefone_celular,
                                                                            Cliente.sexo: cliente.sexo, Cliente.cep: cliente.cep, Cliente.logradouro: cliente.logradouro, Cliente.numero: cliente.numero, Cliente.bairro: cliente.bairro,
                                                                            Cliente.complemento: cliente.complemento, Cliente.municipio: cliente.municipio, Cliente.estado: cliente.estado})
                db.session.commit()
                return "Ok"
            except Exception as e:
                db.session.rollback()
                return str(e)