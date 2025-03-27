# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'w_arbol.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QHBoxLayout,
    QHeaderView, QSizePolicy, QTableWidget, QTableWidgetItem,
    QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(797, 496)
        Form.setLayoutDirection(Qt.LeftToRight)
        self.horizontalLayout_5 = QHBoxLayout(Form)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_arbol_superior = QFrame(Form)
        self.frame_arbol_superior.setObjectName(u"frame_arbol_superior")
        self.frame_arbol_superior.setFrameShape(QFrame.StyledPanel)
        self.frame_arbol_superior.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_arbol_superior)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.fr_tree_cuentas = QFrame(self.frame_arbol_superior)
        self.fr_tree_cuentas.setObjectName(u"fr_tree_cuentas")
        self.fr_tree_cuentas.setMinimumSize(QSize(200, 0))
        self.fr_tree_cuentas.setFrameShape(QFrame.StyledPanel)
        self.fr_tree_cuentas.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.fr_tree_cuentas)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.fr_tree_cuentas)
        self.frame.setObjectName(u"frame")
        self.frame.setLayoutDirection(Qt.LeftToRight)
        self.frame.setStyleSheet(u"background-color: rgb(255, 43, 99);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.tree_cuentas = QTreeWidget(self.frame)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.tree_cuentas.setHeaderItem(__qtreewidgetitem)
        self.tree_cuentas.setObjectName(u"tree_cuentas")
        self.tree_cuentas.setMinimumSize(QSize(0, 0))
        self.tree_cuentas.setMaximumSize(QSize(16777215, 16777215))
        self.tree_cuentas.setSizeIncrement(QSize(0, 0))
        self.tree_cuentas.setBaseSize(QSize(0, 0))
        self.tree_cuentas.setLayoutDirection(Qt.LeftToRight)
        self.tree_cuentas.setStyleSheet(u"background-color: rgb(210, 255, 246);\n"
"alternate-background-color: rgb(170, 0, 255);")
        self.tree_cuentas.setAutoScrollMargin(0)
        self.tree_cuentas.setIndentation(20)
        self.tree_cuentas.setSortingEnabled(True)
        self.tree_cuentas.setAllColumnsShowFocus(True)
        self.tree_cuentas.header().setStretchLastSection(True)

        self.horizontalLayout_4.addWidget(self.tree_cuentas)


        self.horizontalLayout_2.addWidget(self.frame)


        self.horizontalLayout.addWidget(self.fr_tree_cuentas)

        self.fr_table = QFrame(self.frame_arbol_superior)
        self.fr_table.setObjectName(u"fr_table")
        self.fr_table.setLayoutDirection(Qt.LeftToRight)
        self.fr_table.setFrameShape(QFrame.StyledPanel)
        self.fr_table.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.fr_table)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.tablewidget = QTableWidget(self.fr_table)
        if (self.tablewidget.columnCount() < 5):
            self.tablewidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tablewidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        font = QFont()
        font.setPointSize(7)
        font.setBold(True)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font);
        self.tablewidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font);
        self.tablewidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font);
        self.tablewidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font);
        self.tablewidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tablewidget.setObjectName(u"tablewidget")
        self.tablewidget.setLayoutDirection(Qt.LeftToRight)
        self.tablewidget.setStyleSheet(u"background-color: rgb(255, 226, 78);")
        self.tablewidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tablewidget.setTabKeyNavigation(False)
        self.tablewidget.setDragDropOverwriteMode(False)
        self.tablewidget.horizontalHeader().setHighlightSections(True)
        self.tablewidget.verticalHeader().setVisible(False)
        self.tablewidget.verticalHeader().setHighlightSections(False)

        self.verticalLayout.addWidget(self.tablewidget)

        self.tablewidget_img = QTableWidget(self.fr_table)
        if (self.tablewidget_img.columnCount() < 2):
            self.tablewidget_img.setColumnCount(2)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tablewidget_img.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tablewidget_img.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        self.tablewidget_img.setObjectName(u"tablewidget_img")
        self.tablewidget_img.setMaximumSize(QSize(16777215, 16777215))
        self.tablewidget_img.setShowGrid(True)

        self.verticalLayout.addWidget(self.tablewidget_img)


        self.horizontalLayout.addWidget(self.fr_table)


        self.horizontalLayout_5.addWidget(self.frame_arbol_superior)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        ___qtablewidgetitem = self.tablewidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"id", None));
        ___qtablewidgetitem1 = self.tablewidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Nombre", None));
        ___qtablewidgetitem2 = self.tablewidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Descripci\u00f3n", None));
        ___qtablewidgetitem3 = self.tablewidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Categor\u00eda", None));
        ___qtablewidgetitem4 = self.tablewidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Palabras", None));
        ___qtablewidgetitem5 = self.tablewidget_img.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"id", None));
        ___qtablewidgetitem6 = self.tablewidget_img.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"Fichero", None));
    # retranslateUi

