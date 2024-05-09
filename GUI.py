# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GUI.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QListView, QMainWindow, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTextBrowser, QToolBox, QVBoxLayout, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(728, 622)
        MainWindow.setStyleSheet(u"background-color: rgb(94, 92, 100);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{border:none;}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, -1, 0, 0)
        self.esquerdo = QFrame(self.centralwidget)
        self.esquerdo.setObjectName(u"esquerdo")
        self.esquerdo.setMinimumSize(QSize(0, 0))
        self.esquerdo.setMaximumSize(QSize(0, 16777215))
        self.esquerdo.setSizeIncrement(QSize(0, 0))
        self.esquerdo.setFrameShape(QFrame.StyledPanel)
        self.esquerdo.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.esquerdo)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, -1, 0, 0)
        self.frame_2 = QFrame(self.esquerdo)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QSize(0, 0))
        self.frame_2.setSizeIncrement(QSize(0, 0))
        self.frame_2.setStyleSheet(u"QFrame \n"
"{\n"
"	background-color: gray;  /* Cor de fundo padr\u00e3o */\n"
"}\n"
"QPushButton {\n"
"  	border: 2px;\n"
"	border-top-left-radius: 10px;\n"
"	border-style: solid;\n"
"    background-color: #f0f0f0;  /* Cor de fundo padr\u00e3o */\n"
"    color: black;  /* Cor do texto padr\u00e3o */\n"
"    padding: 5px;  /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #4F4F4F;  /* Verde ao passar o mouse */\n"
"	color: black;\n"
"}\n"
"QToolBox\n"
"{\n"
"	border:none;\n"
"\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.toolBox = QToolBox(self.frame_2)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setSizeIncrement(QSize(30, 0))
        self.toolBox.setStyleSheet(u"")
        self.Home = QWidget()
        self.Home.setObjectName(u"Home")
        self.Home.setGeometry(QRect(0, 0, 48, 510))
        self.Home.setAcceptDrops(False)
        self.verticalLayout_4 = QVBoxLayout(self.Home)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.btn_home = QPushButton(self.Home)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(30, 0))
        self.btn_home.setStyleSheet(u"")

        self.verticalLayout_4.addWidget(self.btn_home)

        self.btn_Insert = QPushButton(self.Home)
        self.btn_Insert.setObjectName(u"btn_Insert")
        self.btn_Insert.setMinimumSize(QSize(30, 0))
        self.btn_Insert.setSizeIncrement(QSize(0, 0))

        self.verticalLayout_4.addWidget(self.btn_Insert)

        self.btn_VerFrases = QPushButton(self.Home)
        self.btn_VerFrases.setObjectName(u"btn_VerFrases")
        self.btn_VerFrases.setMinimumSize(QSize(30, 0))
        self.btn_VerFrases.setSizeIncrement(QSize(0, 0))

        self.verticalLayout_4.addWidget(self.btn_VerFrases)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.btn_sobre = QPushButton(self.Home)
        self.btn_sobre.setObjectName(u"btn_sobre")
        self.btn_sobre.setMinimumSize(QSize(30, 0))
        self.btn_sobre.setSizeIncrement(QSize(0, 0))

        self.verticalLayout_4.addWidget(self.btn_sobre)

        self.toolBox.addItem(self.Home, u"Home")
        self.Informaoes = QWidget()
        self.Informaoes.setObjectName(u"Informaoes")
        self.Informaoes.setGeometry(QRect(0, 0, 182, 524))
        self.verticalLayout_11 = QVBoxLayout(self.Informaoes)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.plainTextEdit = QPlainTextEdit(self.Informaoes)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.verticalLayout_11.addWidget(self.plainTextEdit)

        self.toolBox.addItem(self.Informaoes, u"Informa\u00e7oes")

        self.verticalLayout_3.addWidget(self.toolBox)


        self.verticalLayout_2.addWidget(self.frame_2)


        self.horizontalLayout.addWidget(self.esquerdo)

        self.main_frame = QFrame(self.centralwidget)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.main_frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Frame_cima = QFrame(self.main_frame)
        self.Frame_cima.setObjectName(u"Frame_cima")
        self.Frame_cima.setSizeIncrement(QSize(0, 0))
        self.Frame_cima.setStyleSheet(u"QFrame\n"
"{\n"
"	border: 5px;\n"
"    border-color: #272626;\n"
"    border-style: solid;\n"
"    border-right-color: #4F4F4F;\n"
"	border-bottom-color: #4F4F4F;\n"
"    background-color : gray;\n"
"}\n"
"QLabel\n"
"{\n"
"border:none;\n"
"}\n"
"QPushButton\n"
"{\n"
"	background-color : gray;\n"
"}\n"
"")
        self.Frame_cima.setFrameShape(QFrame.StyledPanel)
        self.Frame_cima.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Frame_cima)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton = QPushButton(self.Frame_cima)
        self.pushButton.setObjectName(u"pushButton")
        icon = QIcon()
        icon.addFile(u":/icons/menu1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.pushButton, 0, Qt.AlignLeft)

        self.label = QLabel(self.Frame_cima)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout.addWidget(self.Frame_cima)

        self.Frame_meio = QFrame(self.main_frame)
        self.Frame_meio.setObjectName(u"Frame_meio")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Frame_meio.sizePolicy().hasHeightForWidth())
        self.Frame_meio.setSizePolicy(sizePolicy1)
        self.Frame_meio.setMaximumSize(QSize(16777215, 16777100))
        self.Frame_meio.setFrameShape(QFrame.StyledPanel)
        self.Frame_meio.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.Frame_meio)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.stackedPage = QStackedWidget(self.Frame_meio)
        self.stackedPage.setObjectName(u"stackedPage")
        self.pg_Home = QWidget()
        self.pg_Home.setObjectName(u"pg_Home")
        self.verticalLayout_6 = QVBoxLayout(self.pg_Home)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_4 = QLabel(self.pg_Home)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_6.addWidget(self.label_4)

        self.stackedPage.addWidget(self.pg_Home)
        self.pg_Insert = QWidget()
        self.pg_Insert.setObjectName(u"pg_Insert")
        self.verticalLayout_7 = QVBoxLayout(self.pg_Insert)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.FrameInsert = QFrame(self.pg_Insert)
        self.FrameInsert.setObjectName(u"FrameInsert")
        self.FrameInsert.setStyleSheet(u"QLabel \n"
"{\n"
"	 background-color: #696969; \n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"    border-style: solid;\n"
"    border-width: 2px;\n"
"    border-radius: 5px;  /* Arredonda os cantos */\n"
"    border-color: black;\n"
"    background-color: #f0f0f0;  /* Cor de fundo padr\u00e3o */\n"
"    color: black;  /* Cor do texto padr\u00e3o */\n"
"    padding: 5px;  /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QPushButton {\n"
"  border: 2px;\n"
"  border-top-left-radius: 5px;\n"
"  border-style: solid;\n"
"  background-color: #f0f0f0;  /* Cor de fundo padr\u00e3o */\n"
"  color: black;  /* Cor do texto padr\u00e3o */\n"
"  padding: 5px;  /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #4F4F4F;  /* Verde ao passar o mouse */\n"
"	color: black;\n"
"}\n"
"")
        self.FrameInsert.setFrameShape(QFrame.StyledPanel)
        self.FrameInsert.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.FrameInsert)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_5 = QLabel(self.FrameInsert)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout_8.addWidget(self.label_5)

        self.pessoaMasculina = QLineEdit(self.FrameInsert)
        self.pessoaMasculina.setObjectName(u"pessoaMasculina")
        self.pessoaMasculina.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.pessoaMasculina)

        self.pessoaFeminino = QLineEdit(self.FrameInsert)
        self.pessoaFeminino.setObjectName(u"pessoaFeminino")
        self.pessoaFeminino.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.pessoaFeminino)

        self.pessoaPluralMasculino = QLineEdit(self.FrameInsert)
        self.pessoaPluralMasculino.setObjectName(u"pessoaPluralMasculino")
        self.pessoaPluralMasculino.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.pessoaPluralMasculino)

        self.pessoaPluralFeminino = QLineEdit(self.FrameInsert)
        self.pessoaPluralFeminino.setObjectName(u"pessoaPluralFeminino")
        self.pessoaPluralFeminino.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.pessoaPluralFeminino)

        self.locaisMasculinos = QLineEdit(self.FrameInsert)
        self.locaisMasculinos.setObjectName(u"locaisMasculinos")
        self.locaisMasculinos.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.locaisMasculinos)

        self.locaisFemininos = QLineEdit(self.FrameInsert)
        self.locaisFemininos.setObjectName(u"locaisFemininos")
        self.locaisFemininos.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.locaisFemininos)

        self.verbosPsingular = QLineEdit(self.FrameInsert)
        self.verbosPsingular.setObjectName(u"verbosPsingular")
        self.verbosPsingular.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.verbosPsingular)

        self.verboSSIngular = QLineEdit(self.FrameInsert)
        self.verboSSIngular.setObjectName(u"verboSSIngular")
        self.verboSSIngular.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.verboSSIngular)

        self.verbosPPlural = QLineEdit(self.FrameInsert)
        self.verbosPPlural.setObjectName(u"verbosPPlural")
        self.verbosPPlural.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.verbosPPlural)

        self.verbosSPlural = QLineEdit(self.FrameInsert)
        self.verbosSPlural.setObjectName(u"verbosSPlural")
        self.verbosSPlural.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.verbosSPlural)

        self.btn_inserir = QPushButton(self.FrameInsert)
        self.btn_inserir.setObjectName(u"btn_inserir")
        self.btn_inserir.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_8.addWidget(self.btn_inserir, 0, Qt.AlignHCenter)


        self.verticalLayout_7.addWidget(self.FrameInsert)

        self.stackedPage.addWidget(self.pg_Insert)
        self.pg_verValores = QWidget()
        self.pg_verValores.setObjectName(u"pg_verValores")
        self.verticalLayout_9 = QVBoxLayout(self.pg_verValores)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_3 = QFrame(self.pg_verValores)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"QListView\n"
"{\n"
"	border: 5px;\n"
"    border-color: #272626;\n"
"    border-style: solid;\n"
"    background-color : #d6d1d1;\n"
"    color: black;\n"
"}\n"
"\n"
"\n"
"QPushButton {\n"
"   border: 2px;\n"
"  border-top-left-radius: 10px;\n"
"  border-bottom-right-radius: 10px;\n"
"  border-style: solid;\n"
"  background-color: #f0f0f0;  /* Cor de fundo padr\u00e3o */\n"
"  color: black;  /* Cor do texto padr\u00e3o */\n"
"  padding: 5px;  /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #4F4F4F;  /* Verde ao passar o mouse */\n"
"	color: black;\n"
"}\n"
"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_3)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.ListaFrase = QListView(self.frame_3)
        self.ListaFrase.setObjectName(u"ListaFrase")

        self.verticalLayout_12.addWidget(self.ListaFrase)

        self.btn_Busca = QPushButton(self.frame_3)
        self.btn_Busca.setObjectName(u"btn_Busca")

        self.verticalLayout_12.addWidget(self.btn_Busca)

        self.btn_limpar = QPushButton(self.frame_3)
        self.btn_limpar.setObjectName(u"btn_limpar")

        self.verticalLayout_12.addWidget(self.btn_limpar)


        self.verticalLayout_9.addWidget(self.frame_3)

        self.stackedPage.addWidget(self.pg_verValores)
        self.pg_sobre = QWidget()
        self.pg_sobre.setObjectName(u"pg_sobre")
        self.verticalLayout_10 = QVBoxLayout(self.pg_sobre)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_4 = QFrame(self.pg_sobre)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.textBrowser = QTextBrowser(self.frame_4)
        self.textBrowser.setObjectName(u"textBrowser")

        self.horizontalLayout_5.addWidget(self.textBrowser)


        self.verticalLayout_10.addWidget(self.frame_4)

        self.stackedPage.addWidget(self.pg_sobre)

        self.verticalLayout_5.addWidget(self.stackedPage)


        self.verticalLayout.addWidget(self.Frame_meio)


        self.horizontalLayout.addWidget(self.main_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(0)
        self.stackedPage.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.Home.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.Home.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.Home.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_Insert.setText(QCoreApplication.translate("MainWindow", u"Inserir Frases", None))
        self.btn_VerFrases.setText(QCoreApplication.translate("MainWindow", u"Ver Frases", None))
        self.btn_sobre.setText(QCoreApplication.translate("MainWindow", u"Sobre Programa", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.Home), QCoreApplication.translate("MainWindow", u"Home", None))
        self.plainTextEdit.setPlainText(QCoreApplication.translate("MainWindow", u"Trabalho desenvolvido\n"
"                 por\n"
"\n"
"      Pedro Eduardo\n"
"\n"
"      Thierry Vinicius\n"
"\n"
"      Leonardo Lescano\n"
"\n"
"      Leonardo Ramos\n"
"", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.Informaoes), QCoreApplication.translate("MainWindow", u"Informa\u00e7oes", None))
        self.pushButton.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Gera Frases", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/logoino.png\"/></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">INSERIR PALAVRAS</span></p></body></html>", None))
        self.pessoaMasculina.setPlaceholderText(QCoreApplication.translate("MainWindow", u"PESSOA MASCULINO (EX:Pedro,Joao..)", None))
        self.pessoaFeminino.setPlaceholderText(QCoreApplication.translate("MainWindow", u"PESSOA FEMININO (EX:Maria,Ana..)", None))
        self.pessoaPluralMasculino.setPlaceholderText(QCoreApplication.translate("MainWindow", u"PESSOA NO PLURAL MASCULINO (EX:Garotos,Meninos..)", None))
        self.pessoaPluralFeminino.setPlaceholderText(QCoreApplication.translate("MainWindow", u"PESSOA NO PLURAL FEMININO (EX:Garotas,Meninas..)", None))
        self.locaisMasculinos.setPlaceholderText(QCoreApplication.translate("MainWindow", u"LOCAIS MASCULINOS (EX:Bracos,Restaurante..)", None))
        self.locaisFemininos.setPlaceholderText(QCoreApplication.translate("MainWindow", u"LOCAIS FEMININOS (EX:Casa,Pra\u00e7a..)", None))
        self.verbosPsingular.setPlaceholderText(QCoreApplication.translate("MainWindow", u"VERBOS NA PRIMEIRA PESSOA DO SINGULAR (EX:Estudei,Comprei..)", None))
        self.verboSSIngular.setPlaceholderText(QCoreApplication.translate("MainWindow", u"VERBOS NA SEGUNDA PESSOA DO SINGULAR (EX:Estudou,Comprou..)", None))
        self.verbosPPlural.setPlaceholderText(QCoreApplication.translate("MainWindow", u"VERBOS NA PRIMEIRA PESSOA DO PLURAL (EX:Estudamos,Compramos..)", None))
        self.verbosSPlural.setPlaceholderText(QCoreApplication.translate("MainWindow", u"VERBOS NA SEGUNDA PESSOA DO PLURAL (EX:Estudaram,Compraram..)", None))
        self.btn_inserir.setText(QCoreApplication.translate("MainWindow", u"Inserir", None))
        self.btn_Busca.setText(QCoreApplication.translate("MainWindow", u"Gerar Frases", None))
        self.btn_limpar.setText(QCoreApplication.translate("MainWindow", u"Limpar Lista de Frases", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Ubuntu'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Roboto','Helvetica','Arial','sans-serif'; font-size:16pt; color:rgba(0,0,0,0.866667);\">Implementar um software que seja capaz de gerar INFINITOS textos aleat\u00f3rios em um subconjunto da l\u00edngua Portuguesa atrav\u00e9s de uma gram\u00e1tica livre de contexto. </span></p></body></html>", None))
    # retranslateUi

