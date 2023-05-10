from infra.configs.base import Base
from sqlalchemy import Column, String


class Cliente(Base):
    __tablename__ = 'cliente'

    # id = Column(Integer, autoincrement=True, primary_key=True)
    cpf = Column(String(100), primary_key=True)
    nome_cliente = Column(String(100), nullable=False)
    telefone_fixo = Column(String(100), nullable=False)
    telefone_celular = Column(String(100), nullable=False)
    sexo = Column(String(100), nullable=False)
    cep = Column(String(100), nullable=False)
    logradouro = Column(String(100), nullable=False)
    numero = Column(String(100), nullable=False)
    complemento = Column(String(100), nullable=False)
    bairro = Column(String(100), nullable=False)
    municipio = Column(String(100), nullable=False)
    estado = Column(String(100), nullable=False)

    def __repr__(self):
        return  f'Cliente: {self.nome_cliente}, CPF: {self.cpf}, Tefelone Fixo: {self.telefone_fixo}, Telefone Celular: {self.telefone_celular}' \
                f', Sexo: {self.sexo}, CEP: {self.cep}, Logradouro: {self.logradouro}, , Número: {self.numero}, , Comp: {self.complemento}' \
                f', Bairro: {self.bairro}, , Município: {self.municipio}, , UF: {self.estado}'
