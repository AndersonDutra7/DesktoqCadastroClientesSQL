from infra.configs.connection import DBConnectionHandler
from infra.entities.cliente import Cliente
import traceback

class ClientesRepository:

    def select_all(self):
        with DBConnectionHandler() as db:
            data = db.session.query(Cliente).all()
            return data

    def select(self):
        with DBConnectionHandler() as db:
            data = db.session.query(Cliente).filter(Cliente.cpf == id).first()
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

    def delete(self, cliente):
        with DBConnectionHandler() as db:
            with DBConnectionHandler() as db:
                try:
                    db.session.query(Cliente).filter(Cliente.cpf == id).delete()
                    db.session.commit()
                    return "Ok"
                except Exception as e:
                    db.session.rollback()
                    return e

    def update(self, cpf, nome_cliente, telefone_fixo, telefone_celular, sexo, cep, logradouro, numero, complemento, bairro, municipio, estado):
        with DBConnectionHandler() as db:
            db.session.commit()
        with DBConnectionHandler() as db:
            try:
                db.session.query(Cliente).filter(Cliente.cpf == id).update({Cliente.nome_cliente: nome_cliente, Cliente.telefone_fixo: telefone_fixo, Cliente.telefone_celular: telefone_celular,
                                                                            Cliente.sexo: sexo, Cliente.cep: cep, Cliente.logradouro: logradouro, Cliente.numero: numero, Cliente.bairro: bairro,
                                                                            Cliente.complemento: complemento, Cliente.municipio: municipio, Cliente.estado: estado})
                db.session.commit()
                return "Ok"
            except Exception as e:
                db.session.rollback()
                return e