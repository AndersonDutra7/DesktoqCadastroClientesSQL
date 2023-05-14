from PySide6 import QtWidgets
from PySide6.QtWidgets import QWidget, QSizePolicy, QTableWidget, QAbstractItemView, QVBoxLayout

from view.tela_principal import QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(400, 400)
        self.showMaximized()
        self.setWindowTitle('Cadastro de Clientes')

        self.tabela_clientes = QTableWidget()

        self.tabela_clientes.setColumnCount(12)
        self.tabela_clientes.setHorizontalHeaderLabels(['CPF', 'Nome', 'Telefone Fixo', 'Telefone Celular', 'Sexo'
                                                        , 'Cep', 'Logradouro', 'Número', 'Complemento', 'Bairro',
                                                        'Município', 'Estado'])
        self.tabela_clientes.setSelectionMode(QAbstractItemView.NoSelection)
        self.tabela_clientes.setEditTriggers(QAbstractItemView.NoEditTriggers)


        layout_tabela = QVBoxLayout()

        self.container = QWidget()
        self.container.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.container.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.setCentralWidget(self.container)
        self.container.setLayout(layout_tabela)

        self.btn_remover.setVisible(False)
        self.btn_limpar.setVisible(False)
        self.btn_salvar.clicked.connect(self.salvar_cliente)
        self.txt_cpf.editingFinished.connect(self.consultar_cliente)
        self.txt_cep.editingFinished.connect(self.consultar_enderecos)
        self.btn_remover.clicked.connect(self.remover_cliente)
        self.btn_limpar.clicked.connect(self.limpar_campos)
        self.tabela_clientes.cellDoubleClicked.connect(self.carrega_dados)
        self.popula_tabela_clientes()
