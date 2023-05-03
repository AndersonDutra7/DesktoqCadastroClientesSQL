from infra.configs.connection import DBConnectionHandler
from infra.entities.cliente import Cliente

class ClientesRepository:

    def select(self):
        with DBConnectionHandler() as db:
            data = db.session.query(Cliente).all()
            return data

    def insert(self, cpf, nome_cliente, telefone_fixo, telefone_celular, sexo, cep, logradouro, numero, complemento, bairro, municipio, estado):
        with DBConnectionHandler() as db:
            data_insert = Cliente(cpf = cpf, nome_cliente = nome_cliente, telefone_fixo = telefone_fixo, telefone_celular = telefone_celular,
                                  sexo = sexo, cep = cep, logradouro = logradouro, numero = numero, complemento = complemento,
                                  bairro = bairro, municipio = municipio, estado = estado)
            db.session.add(data_insert)
            db.session.commit()

    def delete(self):
        with DBConnectionHandler() as db:
            db.session.query(Cliente).filter(Cliente.cpf == Cliente.cpf).delete()
            db.session.commit()

    def update(self, cpf, nome_cliente, telefone_fixo, telefone_celular, sexo, cep, logradouro, numero, complemento, bairro, municipio, estado):
        with DBConnectionHandler() as db:
            db.session.query(Cliente).filter(Cliente.cpf == cpf).update({nome_cliente : nome_cliente}, {telefone_fixo : telefone_fixo}, {telefone_celular : telefone_celular},
                                                                        {sexo : sexo}, {cep : cep}, {logradouro : logradouro}, {numero : numero}, {complemento : complemento},
                                                                        {bairro : bairro}, {municipio : municipio}, {estado : estado})
            db.session.commit()