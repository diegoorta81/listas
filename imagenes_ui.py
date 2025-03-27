# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'imagenes.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
    QSpacerItem, QVBoxLayout, QWidget)
import iconos_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(577, 504)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(245, 131, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_superior = QFrame(self.frame)
        self.frame_superior.setObjectName(u"frame_superior")
        self.frame_superior.setMinimumSize(QSize(60, 60))
        self.frame_superior.setMaximumSize(QSize(16777215, 40))
        self.frame_superior.setStyleSheet(u"QPushButton{\n"
"border-radius:18px;\n"
"	background-color: rgb(44, 25, 255);\n"
"}\n"
"\n"
"QPushButton-hover{\n"
"background-color: rgb(255, 227, 156);\n"
"}\n"
"\n"
"QLabel{\n"
"rgb(90, 14, 255)\n"
"font:12pt \"SanSerif\";\n"
"}")
        self.frame_superior.setFrameShape(QFrame.StyledPanel)
        self.frame_superior.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_superior)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.frame_superior)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(184, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.bt_minimo = QPushButton(self.frame_superior)
        self.bt_minimo.setObjectName(u"bt_minimo")
        self.bt_minimo.setMinimumSize(QSize(38, 38))
        self.bt_minimo.setMaximumSize(QSize(38, 38))
        icon = QIcon()
        icon.addFile(u"../../../Users/ortadiegoa07y/.designer/backup/minus.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_minimo.setIcon(icon)
        self.bt_minimo.setIconSize(QSize(38, 38))

        self.horizontalLayout_2.addWidget(self.bt_minimo)

        self.bt_maximo = QPushButton(self.frame_superior)
        self.bt_maximo.setObjectName(u"bt_maximo")
        self.bt_maximo.setMinimumSize(QSize(38, 38))
        self.bt_maximo.setMaximumSize(QSize(38, 38))
        icon1 = QIcon()
        icon1.addFile(u"../../../Users/ortadiegoa07y/.designer/backup/chevron-up.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_maximo.setIcon(icon1)
        self.bt_maximo.setIconSize(QSize(38, 38))

        self.horizontalLayout_2.addWidget(self.bt_maximo)

        self.bt_normal = QPushButton(self.frame_superior)
        self.bt_normal.setObjectName(u"bt_normal")
        self.bt_normal.setMinimumSize(QSize(38, 38))
        self.bt_normal.setMaximumSize(QSize(38, 38))
        icon2 = QIcon()
        icon2.addFile(u"../../../Users/ortadiegoa07y/.designer/backup/chevron-down.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_normal.setIcon(icon2)
        self.bt_normal.setIconSize(QSize(38, 38))

        self.horizontalLayout_2.addWidget(self.bt_normal)

        self.bt_close = QPushButton(self.frame_superior)
        self.bt_close.setObjectName(u"bt_close")
        self.bt_close.setMinimumSize(QSize(38, 38))
        self.bt_close.setMaximumSize(QSize(38, 38))
        icon3 = QIcon()
        icon3.addFile(u"../../../Users/ortadiegoa07y/.designer/backup/x.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_close.setIcon(icon3)
        self.bt_close.setIconSize(QSize(38, 38))

        self.horizontalLayout_2.addWidget(self.bt_close)


        self.verticalLayout_2.addWidget(self.frame_superior)

        self.frame_contenido = QFrame(self.frame)
        self.frame_contenido.setObjectName(u"frame_contenido")
        self.frame_contenido.setStyleSheet(u"QLabel{\n"
"color: rgb(255, 255, 254);\n"
"font: 12pt \"Sans Serif Collection\";\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 	255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
"border-radius:10px;\n"
"color: rgb(255, 255, 254);\n"
"font: 12pt \"Sans Serif Collection\";\n"
"}\n"
"\n"
"QLineEdit{\n"
"background-color:rgb(22,22,26);\n"
"border-radius:10px;\n"
"color: rgb(255, 255, 254);\n"
"font: 12pt \"Sans Serif Collection\";\n"
"border:2px solid rgb(114,117,126);\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"background-color:rgb(22,22,26);\n"
"border-radius:10px;\n"
"font: 12pt \"Sans Serif Collection\";\n"
"border:2px solid rgb(44,182,125);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"background-color:rgb(1,1,1);\n"
"border-radius:10px;\n"
"font: 12pt \"Sans Serif Collection\";\n"
"border:2px solid rgb(127,90,240);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.frame_contenido.setFrameShape(QFrame.StyledPanel)
        self.frame_contenido.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_contenido)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_datos = QFrame(self.frame_contenido)
        self.frame_datos.setObjectName(u"frame_datos")
        self.frame_datos.setMaximumSize(QSize(300, 16777215))
        self.frame_datos.setStyleSheet(u"QFrame{\n"
"border:2px solid #7f5af0;\n"
"}\n"
"\n"
"\n"
"QLabel{\n"
"border:None;\n"
"}")
        self.frame_datos.setFrameShape(QFrame.StyledPanel)
        self.frame_datos.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_datos)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(40, 40, 40, 40)
        self.label_2 = QLabel(self.frame_datos)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout.addWidget(self.label_2)

        self.in_nombre = QLineEdit(self.frame_datos)
        self.in_nombre.setObjectName(u"in_nombre")
        self.in_nombre.setMinimumSize(QSize(0, 30))
        self.in_nombre.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.in_nombre)

        self.in_correo = QLineEdit(self.frame_datos)
        self.in_correo.setObjectName(u"in_correo")
        self.in_correo.setMinimumSize(QSize(0, 30))
        self.in_correo.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.in_correo)

        self.in_telefono = QLineEdit(self.frame_datos)
        self.in_telefono.setObjectName(u"in_telefono")
        self.in_telefono.setMinimumSize(QSize(0, 30))
        self.in_telefono.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.in_telefono)

        self.bt_importar_img = QPushButton(self.frame_datos)
        self.bt_importar_img.setObjectName(u"bt_importar_img")
        self.bt_importar_img.setMinimumSize(QSize(0, 30))

        self.verticalLayout.addWidget(self.bt_importar_img)

        self.img_preview = QLabel(self.frame_datos)
        self.img_preview.setObjectName(u"img_preview")

        self.verticalLayout.addWidget(self.img_preview)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.bt_limpiar = QPushButton(self.frame_datos)
        self.bt_limpiar.setObjectName(u"bt_limpiar")
        self.bt_limpiar.setMinimumSize(QSize(0, 30))
        self.bt_limpiar.setStyleSheet(u"QPushButton{\n"
"border-top-left-radius:0px;\n"
"border-bottom-left-radius:30px;\n"
"border-top-right-radius:30px;\n"
"border-bottom-right-radius:0px;\n"
"}\n"
"QPushButton:hover{\n"
"border-top-left-radius:0px;\n"
"border-bottom-left-radius:30px;\n"
"border-top-right-radius:30px;\n"
"border-bottom-right-radius:0px;\n"
"}")

        self.horizontalLayout_4.addWidget(self.bt_limpiar)

        self.bt_guardar = QPushButton(self.frame_datos)
        self.bt_guardar.setObjectName(u"bt_guardar")
        self.bt_guardar.setMinimumSize(QSize(0, 30))
        self.bt_guardar.setStyleSheet(u"QPushButton{\n"
"border-top-left-radius:0px;\n"
"border-bottom-left-radius:30px;\n"
"border-top-right-radius:30px;\n"
"border-bottom-right-radius:0px;\n"
"}\n"
"QPushButton:hover{\n"
"border-top-left-radius:0px;\n"
"border-bottom-left-radius:30px;\n"
"border-top-right-radius:30px;\n"
"border-bottom-right-radius:0px;\n"
"}\n"
"")

        self.horizontalLayout_4.addWidget(self.bt_guardar)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(4, 1)
        self.verticalLayout.setStretch(5, 1)
        self.verticalLayout.setStretch(6, 1)

        self.horizontalLayout_3.addWidget(self.frame_datos)

        self.frame_buscar = QFrame(self.frame_contenido)
        self.frame_buscar.setObjectName(u"frame_buscar")
        self.frame_buscar.setStyleSheet(u"QFrame{\n"
"border:2px solid #7f5af0;\n"
"}\n"
"\n"
"\n"
"QLabel{\n"
"border:None;\n"
"}")
        self.frame_buscar.setFrameShape(QFrame.StyledPanel)
        self.frame_buscar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_buscar)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(40, 40, 40, 40)
        self.label_7 = QLabel(self.frame_buscar)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_3.addWidget(self.label_7)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.in_buscar_nombre = QLineEdit(self.frame_buscar)
        self.in_buscar_nombre.setObjectName(u"in_buscar_nombre")
        self.in_buscar_nombre.setMinimumSize(QSize(0, 30))
        self.in_buscar_nombre.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.in_buscar_nombre)

        self.bt_buscar = QPushButton(self.frame_buscar)
        self.bt_buscar.setObjectName(u"bt_buscar")
        self.bt_buscar.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_5.addWidget(self.bt_buscar)

        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.lbl_correo = QLabel(self.frame_buscar)
        self.lbl_correo.setObjectName(u"lbl_correo")
        self.lbl_correo.setMinimumSize(QSize(0, 50))
        self.lbl_correo.setMaximumSize(QSize(16777215, 50))
        self.lbl_correo.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.lbl_correo)

        self.lbl_telefono = QLabel(self.frame_buscar)
        self.lbl_telefono.setObjectName(u"lbl_telefono")
        self.lbl_telefono.setMinimumSize(QSize(0, 50))
        self.lbl_telefono.setMaximumSize(QSize(16777215, 50))
        self.lbl_telefono.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.lbl_telefono)

        self.lbl_imagen = QLabel(self.frame_buscar)
        self.lbl_imagen.setObjectName(u"lbl_imagen")
        self.lbl_imagen.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.lbl_imagen)

        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 1)
        self.verticalLayout_3.setStretch(2, 1)
        self.verticalLayout_3.setStretch(3, 1)
        self.verticalLayout_3.setStretch(4, 3)

        self.horizontalLayout_3.addWidget(self.frame_buscar)


        self.verticalLayout_2.addWidget(self.frame_contenido)


        self.horizontalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"FORMULARIOS CON BD EN SQLITE", None))
        self.bt_minimo.setText("")
        self.bt_maximo.setText("")
        self.bt_normal.setText("")
        self.bt_close.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.in_nombre.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.in_correo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Correo", None))
        self.in_telefono.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Telefono", None))
        self.bt_importar_img.setText(QCoreApplication.translate("MainWindow", u"IMPORTAR FORTO", None))
        self.img_preview.setText(QCoreApplication.translate("MainWindow", u"Foto", None))
        self.bt_limpiar.setText(QCoreApplication.translate("MainWindow", u"LIMPIAR", None))
        self.bt_guardar.setText(QCoreApplication.translate("MainWindow", u"GUARDAR", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.in_buscar_nombre.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.bt_buscar.setText(QCoreApplication.translate("MainWindow", u"BUSCAR", None))
        self.lbl_correo.setText(QCoreApplication.translate("MainWindow", u"Correo", None))
        self.lbl_telefono.setText(QCoreApplication.translate("MainWindow", u"Tel\u00e9fono", None))
        self.lbl_imagen.setText(QCoreApplication.translate("MainWindow", u"Foto", None))
    # retranslateUi

