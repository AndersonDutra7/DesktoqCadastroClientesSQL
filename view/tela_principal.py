import json as js
import requests

from PySide6 import QtWidgets
from datetime import datetime
from PySide6.QtWidgets import (QMainWindow, QComboBox, QLabel, QLineEdit, QWidget, QPushButton,
                               QMessageBox, QSizePolicy, QTableWidget, QAbstractItemView, QTableWidgetItem,)

from infra.entities.cliente import Cliente
from infra.entities.widgets import GridLayoutGremio
from infra.repository.cliente_repository import ClientesRepository

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(400, 400)
        self.showMaximized()
        self.setWindowTitle('Cadastro de Clientes')

        self.lbl_cpf = QLabel('CPF')
        self.txt_cpf = QLineEdit()
        self.txt_cpf.setInputMask('000.000.000-00')
        self.lbl_nome = QLabel('NOME COMPLETO')
        self.txt_nome = QLineEdit()
        self.lbl_telefone_fixo = QLabel('TELEFONE FIXO')
        self.txt_telefone_fixo = QLineEdit()
        self.txt_telefone_fixo.setInputMask('(00) 0000-0000')
        self.lbl_telefone_celular = QLabel('TELEFONE CELULAR')
        self.txt_telefone_celular = QLineEdit()
        self.txt_telefone_celular.setInputMask(('(00) 00000-0000'))
        self.lbl_sexo = QLabel('SEXO')
        self.cb_sexo = QComboBox()
        self.cb_sexo.addItems(['Não informado', 'Feminino', 'Masculino'])
        self.lbl_cep = QLabel('CEP')
        self.txt_cep = QLineEdit()
        self.txt_cep.setInputMask('00.000-000')
        self.lbl_logradouro = QLabel('LOGRADOURO')
        self.txt_logradouro = QLineEdit()
        self.lbl_numero = QLabel('NÚMERO')
        self.txt_numero = QLineEdit()
        self.lbl_complemento = QLabel('COMPLEMENTO')
        self.txt_complemento = QLineEdit()
        self.lbl_bairro = QLabel('BAIRRO')
        self.txt_bairro = QLineEdit()
        self.lbl_municipio = QLabel('MUNICÍPIO')
        self.txt_municipio = QLineEdit()
        self.lbl_estado = QLabel('ESTADO')
        self.txt_estado = QLineEdit()
        self.btn_salvar = QPushButton('Salvar')
        self.btn_limpar = QPushButton('Limpar')
        self.btn_remover = QPushButton('Remover')
        self.lbl_clientes = QLabel("QUADRO DE CLIENTE GRÊMIO MANIA")
        self.tabela_clientes = QTableWidget()
        self.lbl_data_cadastro = QLineEdit()

        self.tabela_clientes.setColumnCount(13)
        self.tabela_clientes.setHorizontalHeaderLabels(['CPF', 'Nome', 'Telefone Fixo', 'Telefone Celular', 'Sexo'
                                                        , 'Cep', 'Logradouro', 'Número', 'Complemento', 'Bairro',
                                                        'Município', 'Estado', 'Data Cadastro'])
        self.tabela_clientes.setSelectionMode(QAbstractItemView.NoSelection)
        self.tabela_clientes.setEditTriggers(QAbstractItemView.NoEditTriggers)


        layout = GridLayoutGremio()
        layout.addWidget(self.lbl_cpf, 0, 0)
        layout.addWidget(self.txt_cpf, 1, 0)
        layout.addWidget(self.lbl_nome, 0, 1)
        layout.addWidget(self.txt_nome, 1, 1)
        layout.addWidget(self.lbl_telefone_fixo, 0, 2)
        layout.addWidget(self.txt_telefone_fixo, 1, 2)
        layout.addWidget(self.lbl_telefone_celular, 0, 3)
        layout.addWidget(self.txt_telefone_celular, 1, 3)
        layout.addWidget(self.lbl_sexo, 2, 0)
        layout.addWidget(self.cb_sexo, 3, 0)
        layout.addWidget(self.lbl_cep, 2, 1)
        layout.addWidget(self.txt_cep, 3, 1)
        layout.addWidget(self.lbl_logradouro, 2, 2)
        layout.addWidget(self.txt_logradouro, 3, 2)
        layout.addWidget(self.lbl_numero, 2, 3)
        layout.addWidget(self.txt_numero, 3, 3)
        layout.addWidget(self.lbl_complemento, 4, 0)
        layout.addWidget(self.txt_complemento, 5, 0)
        layout.addWidget(self.lbl_bairro, 4, 1)
        layout.addWidget(self.txt_bairro, 5, 1)
        layout.addWidget(self.lbl_municipio, 4, 2)
        layout.addWidget(self.txt_municipio, 5, 2)
        layout.addWidget(self.lbl_estado, 4, 3)
        layout.addWidget(self.txt_estado, 5, 3)
        layout.addWidget(self.lbl_clientes, 7, 0)
        layout.addWidget(self.tabela_clientes, 9, 0, 1, 4)

        layout.addWidget(self.btn_salvar, 6, 0)
        layout.addWidget(self.btn_limpar, 6, 1)
        layout.addWidget(self.btn_remover, 6, 2)

        self.container = QWidget()
        self.container.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.container.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.setCentralWidget(self.container)
        self.container.setLayout(layout)

        self.btn_remover.setVisible(False)
        self.btn_limpar.setVisible(False)
        self.btn_salvar.clicked.connect(self.salvar_cliente)
        self.txt_cpf.editingFinished.connect(self.consultar_clientes)
        self.txt_cep.editingFinished.connect(self.consultar_enderecos)
        self.btn_remover.clicked.connect(self.remover_cliente)
        self.btn_limpar.clicked.connect(self.limpar_campos)
        self.tabela_clientes.cellDoubleClicked.connect(self.carrega_dados)
        self.popula_tabela_clientes()

    def salvar_cliente(self):
        db = ClientesRepository()

        cliente = Cliente(
            cpf=self.txt_cpf.text(),
            nome_cliente=self.txt_nome.text(),
            telefone_fixo=self.txt_telefone_fixo.text(),
            telefone_celular=self.txt_telefone_celular.text(),
            sexo=self.cb_sexo.currentText(),
            cep=self.txt_cep.text(),
            logradouro=self.txt_logradouro.text(),
            numero=self.txt_numero.text(),
            complemento=self.txt_complemento.text(),
            bairro=self.txt_bairro.text(),
            municipio=self.txt_municipio.text(),
            estado=self.txt_estado.text(),
            data_cadastro = datetime.today()
        )

        if self.btn_salvar.text() == 'Salvar':
            if (self.txt_nome.text().split()) and (self.txt_cpf.text().split()):
                retorno = db.insert(cliente)
                self.btn_limpar.setVisible(True)
                if retorno == 'Ok':
                    msg = QMessageBox()
                    msg.setWindowTitle('Cadastro Realizado ')
                    msg.setText('Cadastro realizado com sucesso')
                    msg.exec()
                    self.limpar_campos()
                elif retorno == 'UNIQUE constraint failed: CLIENTE.CPF':
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Critical)
                    msg.setWindowTitle('Erro ao cadastrar')
                    msg.setText(f'O CPF {self.txt_cpf.text()} já tem cadastro')
                    msg.exec()
                else:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Critical)
                    msg.setWindowTitle('Erro ao cadastrar ')
                    msg.setText('Erro ao cadastrar verifique os dados inseridos')
                    msg.exec()
        elif self.btn_salvar.text() == 'Atualizar':
            retorno = db.update(cliente)
            if retorno == 'Ok':
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle('Erro ao cadastrar ')
                msg.setText('Cliente Atualizado')
                msg.exec()
                self.limpar_campos()
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setWindowTitle('Erro ao atualizar ')
                msg.setText('Erro ao atualziar verifique, os dados inseridos')
                msg.exec()
        self.popula_tabela_clientes()
        self.txt_cpf.setReadOnly(False)


    def consultar_clientes(self):
        if self.txt_cpf.text() != '':
            db = ClientesRepository()
            retorno = db.select(self.txt_cpf.text())

            if retorno is not None:
                self.btn_salvar.setText('Atualizar')
                msg = QMessageBox()
                msg.setWindowTitle('Cliente já cadastrado')
                msg.setText(f'O CPF {self.txt_cpf.text()} já esta cadastrado')
                msg.exec()
                self.txt_nome.setText(retorno.nome_cliente)
                self.txt_telefone_fixo.setText(retorno.telefone_fixo)
                self.txt_telefone_celular.setText(retorno.telefone_celular)
                sexo_map = {'Não Informado': 0, 'Feminimo': 1, 'Masculino': 2}
                self.cb_sexo.setCurrentIndex(sexo_map.get(retorno.sexo))
                self.txt_cep.setText(retorno.cep)
                self.txt_logradouro.setText(retorno.logradouro)
                self.txt_numero.setText(retorno.numero)
                self.txt_complemento.setText(retorno.complemento)
                self.txt_bairro.setText(retorno.bairro)
                self.txt_municipio.setText(retorno.municipio)
                self.txt_estado.setText(retorno.estado)
                self.lbl_data_cadastro.setText(retorno.data_cadastro)


    def remover_cliente(self):
        msg = QMessageBox()
        msg.setWindowTitle('Remover Cliente')
        msg.setText('Este cliente será removido.')
        msg.setInformativeText(f'Voce deseja remover o cliente de CPF {self.txt_cpf.text()} ?')
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.button(QMessageBox.Yes).setText('Sim')
        msg.button(QMessageBox.No).setText('Não')
        resposta = msg.exec()

        if resposta == QMessageBox.Yes:
            db = ClientesRepository()
            if db.delete(self.txt_cpf.text()) == 'Ok':
                nv_msg = QMessageBox()
                nv_msg.setWindowTitle('Remover Cliente')
                nv_msg.setText('Cliente removido com sucesso.')
                nv_msg.exec()
                self.limpar_campos()
            else:
                nv_msg = QMessageBox()
                nv_msg.setWindowTitle('Remover Cliente')
                nv_msg.setText('Erro ao remover cliente.')
                nv_msg.exec()
        self.popula_tabela_clientes()
        self.txt_cpf.setReadOnly(False)

    def limpar_campos(self):
        for widget in self.container.children():
            if isinstance(widget, QLineEdit):
                widget.clear()
            elif isinstance(widget, QComboBox):
                widget.setCurrentIndex(0)
        self.btn_remover.setVisible(False)
        self.btn_limpar.setVisible(False)
        self.btn_salvar.setText('Salvar')
        self.txt_cpf.setReadOnly(False)

    def consultar_enderecos(self):
        cep = str(self.txt_cep.text().replace(".","").replace("-",""))
        url = f'https://viacep.com.br/ws/{cep}/json/'
        response = requests.get(url)
        endereco = js.loads(response.text)
        #teste = js.loads(response)

        if response.status_code == 200 and 'erro' not in endereco:
            self.txt_logradouro.setText(endereco['logradouro'])
            self.txt_bairro.setText(endereco['bairro'])
            self.txt_municipio.setText(endereco['localidade'])
            self.txt_estado.setText(endereco['uf'])
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle('Consultar CEP')
            msg.setText('Erro ao consultar CEP, verifique os dados inseridos.')
            msg.exec()

    def popula_tabela_clientes(self):
        self.tabela_clientes.setRowCount(0)
        db = ClientesRepository()
        lista_clientes = db.select_all()
        self.tabela_clientes.setRowCount(len(lista_clientes))

        linha = 0

        for cliente in lista_clientes:
            valores = [cliente.cpf, cliente.nome_cliente, cliente.telefone_fixo, cliente.telefone_celular,
                       cliente.sexo, cliente.cep, cliente.logradouro, cliente.numero, cliente.complemento,
                       cliente.bairro, cliente.municipio, cliente.estado, cliente.data_cadastro]
            for valor in valores:
                item = QTableWidgetItem(str(valor))
                self.tabela_clientes.setItem(linha, valores.index(valor), item)
                self.tabela_clientes.item(linha, valores.index(valor))
            linha += 1

    def carrega_dados(self, row, column):
        self.txt_cpf.setText(
            self.tabela_clientes.item(row, 0).text() if self.tabela_clientes.item(row, 0) is not None else "")
        self.txt_nome.setText(
            self.tabela_clientes.item(row, 1).text() if self.tabela_clientes.item(row, 1) is not None else "")
        self.txt_telefone_fixo.setText(
            self.tabela_clientes.item(row, 2).text() if self.tabela_clientes.item(row, 2) is not None else "")
        self.txt_telefone_celular.setText(
            self.tabela_clientes.item(row, 3).text() if self.tabela_clientes.item(row, 3) is not None else "")
        sexo_map = {'Não Informado': 0, 'Feminino': 1, 'Masculino': 2}
        self.cb_sexo.setCurrentIndex(
            sexo_map.get(self.tabela_clientes.item(row, 4).text(), 0) if self.tabela_clientes.item(row,
                                                                                                   4) is not None else 0)
        self.txt_cep.setText(
            self.tabela_clientes.item(row, 5).text() if self.tabela_clientes.item(row, 5) is not None else "")
        self.txt_logradouro.setText(
            self.tabela_clientes.item(row, 6).text() if self.tabela_clientes.item(row, 6) is not None else "")
        self.txt_numero.setText(
            self.tabela_clientes.item(row, 7).text() if self.tabela_clientes.item(row, 7) is not None else "")
        self.txt_complemento.setText(
            self.tabela_clientes.item(row, 8).text() if self.tabela_clientes.item(row, 8) is not None else "")
        self.txt_bairro.setText(
            self.tabela_clientes.item(row, 9).text() if self.tabela_clientes.item(row, 9) is not None else "")
        self.txt_municipio.setText(
            self.tabela_clientes.item(row, 10).text() if self.tabela_clientes.item(row, 10) is not None else "")
        self.txt_estado.setText(
            self.tabela_clientes.item(row, 11).text() if self.tabela_clientes.item(row, 11) is not None else "")
        self.lbl_data_cadastro.setText(
             self.tabela_clientes.item(row, 12).text() if self.tabela_clientes.item(row, 12) is not None else "")
        self.btn_salvar.setText('Atualizar')
        self.btn_remover.setVisible(True)
        self.btn_limpar.setVisible(True)
        self.txt_cpf.setReadOnly(True)
