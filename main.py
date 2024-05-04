from PySide6.QtGui import QIcon
from PySide6 import QtCore
from PySide6.QtCore import QCoreApplication, Qt
from PySide6.QtWidgets import (QApplication, QMainWindow, QMessageBox, QTableWidgetItem)
from PySide6.QtGui import QStandardItemModel, QStandardItem
from GUI import Ui_MainWindow
from Gera_Frases import geraFrases
import sys

class mainwindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        self.gerar = geraFrases()
        super(mainwindow,self).__init__()
        self.setupUi(self)
        appincon = QIcon(u"")
        self.setWindowIcon(appincon)
        self.setWindowTitle('Gera Frases')
        self.frases = []
        #############################
        # Configuração do botão do menu
        self.pushButton.clicked.connect(self.abreMenu)
        #############################
        # Configuração dos pagiamentos onde ele troca as paginas
        ########################################################################################
        self.btn_home.clicked.connect(lambda: self.stackedPage.setCurrentWidget(self.pg_Home))
        self.btn_Insert.clicked.connect(lambda: self.stackedPage.setCurrentWidget(self.pg_Insert))
        self.btn_VerFrases.clicked.connect(lambda: self.stackedPage.setCurrentWidget(self.pg_verValores))
        self.btn_sobre.clicked.connect(lambda: self.stackedPage.setCurrentWidget(self.pg_sobre))
        #######################################################################################
        
        # Botão para pegar os valores inseridos
        #######################################################################################
        self.btn_inserir.clicked.connect(self.pegaValor)    
        #######################################################################################
        # Botõa pra add frases no view
        #######################################################################################
        self.btn_Busca.clicked.connect(self.pegaFrase)
        #######################################################################################
        # Botão para limpar o view
        #######################################################################################
        self.btn_limpar.clicked.connect(self.limparFrases)
        #######################################################################################

    # Função paga colocar valores na view
    def pegaFrase(self):
        self.model = QStandardItemModel(self.ListaFrase)
        self.frases.append(self.gerar.gen_random(symbol='Começo'))
        for frase in self.frases:
            standard_item = QStandardItem(frase)
            self.model.appendRow(standard_item)
        self.ListaFrase.setModel(self.model)
    def limparFrases(self):
        self.model.clear()
    ## Função que ira pegar os valores
    def pegaValor(self):
        pessoaMasculina = self.pessoaMasculina.text()
        pessoaFeminino = self.pessoaFeminino.text()
        pessoanoPluralM = self.pessoaPluralMasculino.text()
        pessoanoPluralF = self.pessoaPluralFeminino.text()
        localMasculino = self.locaisMasculinos.text()
        localFeminino = self.locaisFemininos.text()
        verbosPsingular = self.verbosPsingular.text()
        verbosPPlural = self.verbosPPlural.text()
        verboSSIngular = self.verboSSIngular.text()
        verbosSPlural = self.verbosSPlural.text()
        if pessoaMasculina == '' or pessoaFeminino == '' or pessoanoPluralM == '' or pessoanoPluralF == '' or localMasculino == '' or localFeminino == '' or verbosPsingular == '' or verbosPPlural == '' or verboSSIngular == '' or verbosSPlural == '':
            msg = QMessageBox()
            msg.setWindowTitle('Mensagem')
            msg.setText('Faltou Inserir Algo:')
            msg.exec()
        else:
            msg = QMessageBox()
            msg.setWindowTitle('Mensagem')
            msg.setText('Inserido com suceso:')
            msg.exec()
            self.gerar.insertProd(pessoaMasculina,pessoaFeminino,pessoanoPluralM,pessoanoPluralF,localMasculino,localFeminino,verbosPsingular,verboSSIngular,verbosPPlural,verbosSPlural)

    # Função para fazer a animação
    def abreMenu(self):
        largura = self.esquerdo.width()
        if largura == 0:
            novalargura = 200
        else: 
            novalargura = 0
        self.animacao = QtCore.QPropertyAnimation(self.esquerdo,b'maximumWidth')
        self.animacao.setDuration(1000)
        self.animacao.setStartValue(largura)
        self.animacao.setEndValue(novalargura)
        self.animacao.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animacao.start()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = mainwindow()
    window.show()
    app.exec()