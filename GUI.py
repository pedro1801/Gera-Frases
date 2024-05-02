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
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTextBrowser, QToolBox,
    QVBoxLayout, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(787, 622)
        MainWindow.setStyleSheet(u"background-color: rgb(94, 92, 100);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
"	border:none\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, -1, 0, 0)
        self.esquerdo = QFrame(self.centralwidget)
        self.esquerdo.setObjectName(u"esquerdo")
        self.esquerdo.setMaximumSize(QSize(200, 16777215))
        self.esquerdo.setFrameShape(QFrame.StyledPanel)
        self.esquerdo.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.esquerdo)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, -1, 0, 0)
        self.frame = QFrame(self.esquerdo)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.esquerdo)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QFrame \n"
"{\n"
"	background-color: gray;  /* Cor de fundo padr\u00e3o */\n"
"}\n"
"QPushButton {\n"
"    border-style: solid;\n"
"    border-width: 2px;\n"
"    border-radius: 5px;  /* Arredonda os cantos */\n"
"    border-color: black;\n"
"    background-color: #f0f0f0;  /* Cor de fundo padr\u00e3o */\n"
"    color: black;  /* Cor do texto padr\u00e3o */\n"
"    padding: 5px;  /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #04AA6D;  /* Verde ao passar o mouse */\n"
"    color: white;  /* Cor do texto ao passar o mouse */\n"
"}\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.toolBox = QToolBox(self.frame_2)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setSizeIncrement(QSize(30, 0))
        self.toolBox.setStyleSheet(u"")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 182, 489))
        self.verticalLayout_4 = QVBoxLayout(self.page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.btn_home = QPushButton(self.page)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(30, 0))
        self.btn_home.setStyleSheet(u"")

        self.verticalLayout_4.addWidget(self.btn_home)

        self.btn_Insert = QPushButton(self.page)
        self.btn_Insert.setObjectName(u"btn_Insert")
        self.btn_Insert.setMinimumSize(QSize(30, 0))
        self.btn_Insert.setSizeIncrement(QSize(0, 0))

        self.verticalLayout_4.addWidget(self.btn_Insert)

        self.btn_VerFrases = QPushButton(self.page)
        self.btn_VerFrases.setObjectName(u"btn_VerFrases")
        self.btn_VerFrases.setMinimumSize(QSize(30, 0))
        self.btn_VerFrases.setSizeIncrement(QSize(0, 0))

        self.verticalLayout_4.addWidget(self.btn_VerFrases)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.btn_sobre = QPushButton(self.page)
        self.btn_sobre.setObjectName(u"btn_sobre")
        self.btn_sobre.setMinimumSize(QSize(30, 0))
        self.btn_sobre.setSizeIncrement(QSize(0, 0))

        self.verticalLayout_4.addWidget(self.btn_sobre)

        self.toolBox.addItem(self.page, u"Page 1")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 182, 489))
        self.toolBox.addItem(self.page_2, u"Page 2")

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

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout.addWidget(self.Frame_cima)

        self.Frame_meio = QFrame(self.main_frame)
        self.Frame_meio.setObjectName(u"Frame_meio")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Frame_meio.sizePolicy().hasHeightForWidth())
        self.Frame_meio.setSizePolicy(sizePolicy)
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
"    border-style: solid;\n"
"    border-width: 2px;\n"
"    border-radius: 5px;  /* Arredonda os cantos */\n"
"    border-color: black;\n"
"    background-color: #f0f0f0;  /* Cor de fundo padr\u00e3o */\n"
"    color: black;  /* Cor do texto padr\u00e3o */\n"
"    padding: 5px;  /* Espa\u00e7amento interno */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #04AA6D;  /* Verde ao passar o mouse */\n"
"    color: white;  /* Cor do texto ao passar o mouse */\n"
"}\n"
"")
        self.FrameInsert.setFrameShape(QFrame.StyledPanel)
        self.FrameInsert.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.FrameInsert)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_5 = QLabel(self.FrameInsert)
        self.label_5.setObjectName(u"label_5")

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

        self.verticalLayout_8.addWidget(self.btn_inserir, 0, Qt.AlignHCenter)


        self.verticalLayout_7.addWidget(self.FrameInsert)

        self.stackedPage.addWidget(self.pg_Insert)
        self.pg_verValores = QWidget()
        self.pg_verValores.setObjectName(u"pg_verValores")
        self.verticalLayout_9 = QVBoxLayout(self.pg_verValores)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_3 = QFrame(self.pg_verValores)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

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

        self.Frame_baixo = QFrame(self.main_frame)
        self.Frame_baixo.setObjectName(u"Frame_baixo")
        self.Frame_baixo.setFrameShape(QFrame.StyledPanel)
        self.Frame_baixo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.Frame_baixo)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.Frame_baixo)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)


        self.verticalLayout.addWidget(self.Frame_baixo)


        self.horizontalLayout.addWidget(self.main_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(0)
        self.stackedPage.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"GeraFrases", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_Insert.setText(QCoreApplication.translate("MainWindow", u"Inserir Valores", None))
        self.btn_VerFrases.setText(QCoreApplication.translate("MainWindow", u"Ver Frases", None))
        self.btn_sobre.setText(QCoreApplication.translate("MainWindow", u"Sobre Programa", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("MainWindow", u"Page 1", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"Page 2", None))
        self.pushButton.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/logo4.png\"/></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">INSERIR PALAVRAS</span></p></body></html>", None))
        self.pessoaMasculina.setPlaceholderText(QCoreApplication.translate("MainWindow", u"PESSOA MASCULINO", None))
        self.pessoaFeminino.setPlaceholderText(QCoreApplication.translate("MainWindow", u"PESSOA FEMININO", None))
        self.pessoaPluralMasculino.setPlaceholderText(QCoreApplication.translate("MainWindow", u"PESSOA NO PLURAL MASCULINO", None))
        self.pessoaPluralFeminino.setPlaceholderText(QCoreApplication.translate("MainWindow", u"PESSOA NO PLURAL FEMININO", None))
        self.locaisMasculinos.setPlaceholderText(QCoreApplication.translate("MainWindow", u"LOCAIS MASCULINOS", None))
        self.locaisFemininos.setPlaceholderText(QCoreApplication.translate("MainWindow", u"LOCAIS FEMININOS", None))
        self.verbosPsingular.setPlaceholderText(QCoreApplication.translate("MainWindow", u"VERBOS NA PRIMEIRA PESSOA DO SINGULAR", None))
        self.verboSSIngular.setPlaceholderText(QCoreApplication.translate("MainWindow", u"VERBOS NA SEGUNDA PESSOA DO SINGULAR", None))
        self.verbosPPlural.setPlaceholderText(QCoreApplication.translate("MainWindow", u"VERBOS NA PRIMEIRA PESSOA DO PLURAL", None))
        self.verbosSPlural.setPlaceholderText(QCoreApplication.translate("MainWindow", u"VERBOS NA SEGUNDA PESSOA DO PLURAL", None))
        self.btn_inserir.setText(QCoreApplication.translate("MainWindow", u"Inserir", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Ubuntu'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\"\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Este programa tem como intuito gerar frases aleatoriamente.</li>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\"><br /></p>\n"
"<li style=\"\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Pessoas est\u00e3o se referindo a gente, por exemplo: senhor, senhora, pai, m\u00e3e.."
                        ".</li>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\"><br /></p>\n"
"<li style=\"\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Locais est\u00e3o se referindo a locais reais, por exemplo: mercado, escola, livraria...</li>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\"><br /></p>\n"
"<li style=\"\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Os verbos devem ser conjugados no passado.</li></ol></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"GeraFrases", None))
    # retranslateUi

