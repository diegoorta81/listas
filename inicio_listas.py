import sys, os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QFrame, QHBoxLayout, QSplitter, QLineEdit, QFrame,QTreeWidget, QTreeWidgetItem,QMainWindow, QAction

from PyQt5 import uic
from bd import bd
from PyQt5.QtCore import Qt
#from PyQt6.QtGui import QAction

class Inicio_listas(QtWidgets.QMainWindow):

    def __init__(self):
    
        super(Inicio_listas,self).__init__()
        ui_path = os.path.dirname(os.path.abspath(__file__))

        uic.loadUi(os.path.join(ui_path, "inicio_listas.ui"), self)



        
        self.bt_articulos = self.findChild(QtWidgets.QPushButton, 'bt_articulos')
        self.bt_articulos.setText("Artículos")
        self.bt_articulos.clicked.connect(self.act_articulos)

        self.act = self.findChild(QAction, 'action_articulos')
        self.act.triggered.connect(self.act_articulos)
        self.hidden = True

        self.bt_nuevoarticulo = self.findChild(QtWidgets.QPushButton, 'bt_nuevoarticulo')
        self.bt_nuevoarticulo.clicked.connect(bd.act_nuevoarticulo)
        
        self.action_nuevoarticulo = self.findChild(QAction, 'action_nuevoarticulo')
        self.action_nuevoarticulo.triggered.connect(bd.act_nuevoarticulo)

        self.bt_editararticulo = self.findChild(QtWidgets.QPushButton, 'bt_editararticulo')
        self.bt_editararticulo.clicked.connect(bd.act_editararticulo)
        
        self.action_editararticulo = self.findChild(QAction, 'action_editararticulo')
        self.action_editararticulo.triggered.connect(bd.act_editararticulo)

        self.bt_borrararticulo = self.findChild(QtWidgets.QPushButton, 'bt_borrararticulo')
        self.bt_borrararticulo.clicked.connect(bd.act_borrararticulo)
        
        self.action_borrararticulo = self.findChild(QAction, 'action_borrararticulo')
        self.action_borrararticulo.triggered.connect(bd.act_borrararticulo)

        self.action_borrararticulo.setEnabled(False)
        self.action_editararticulo.setEnabled(False)
        self.action_nuevoarticulo.setEnabled(False)
        self.bt_borrararticulo.setEnabled(False)
        self.bt_editararticulo.setEnabled(False)
        self.bt_nuevoarticulo.setEnabled(False)


    def onItemClicked(self):
        item = self.tree_apuntes.currentItem()
        
        bd.onItemClicked(item,self.tablewidget)


    def act_articulos(self):
        self.frame_arbol_superior = self.fr_inferior.findChild(QFrame, 'frame_arbol_superior')
        #self.fr_inferior = self.findChild(QFrame, 'fr_inferior')
        
        if (self.frame_arbol_superior is None):
                   
            self.fr_inferior = self.findChild(QFrame, 'fr_inferior')

            uic.loadUi('w_arbol.ui',self.fr_inferior)
            self.hbox = self.findChild(QtWidgets.QHBoxLayout, 'horizontalLayout_2')

            self.fr_inferior.setLayout(self.hbox)


            self.tree_apuntes = self.findChild(QtWidgets.QTreeWidget, 'tree_cuentas')
            

            self.tablewidget = self.findChild(QtWidgets.QTableWidget, 'tablewidget')
            
            self.tablewidget.setSortingEnabled(True)
            
            

            self.tablewidget_img = self.findChild(QtWidgets.QTableWidget, 'tablewidget_img')
            self.tablewidget_img.setColumnHidden(0,True)
            self.tablewidget.setColumnHidden(0,True)
            self.fr_tree_cuentas = self.findChild(QtWidgets.QFrame, 'fr_tree_cuentas')
            self.fr_table = self.findChild(QtWidgets.QFrame, 'fr_table')
            
            
            self.apuntes = bd.ejecuta()

            self.splitter2 = QSplitter(Qt.Orientation.Vertical)
            self.splitter2.addWidget(self.tablewidget)
            self.splitter2.addWidget(self.tablewidget_img)
            self.splitter2.setSizes([300,300])
            self.hbox.addWidget(self.splitter2)

            self.splitter1 = QSplitter(Qt.Orientation.Horizontal)
            self.splitter1.addWidget(self.tree_apuntes)
            self.splitter1.addWidget(self.splitter2)

            self.splitter1.setSizes([300,300])
            self.hbox.addWidget(self.splitter1)
            self.tablewidget.itemChanged.connect(self.tablewidget_on_item_changed) 
            
            

            
            

            self.bt_articulos.setText("Cerrar Artículos")
            self.act.setText("Cerrar Artículos")
            self.action_borrararticulo.setEnabled(True)
            self.action_editararticulo.setEnabled(True)
            self.action_nuevoarticulo.setEnabled(True)
            self.bt_borrararticulo.setEnabled(True)
            self.bt_editararticulo.setEnabled(True)
            self.bt_nuevoarticulo.setEnabled(True)

            bd.refresca(self.tree_apuntes,self.apuntes)
            self.tree_apuntes.itemClicked.connect(self.onItemClicked)
        else:
            
            if (self.fr_inferior.isVisible()):
                self.fr_inferior.setVisible(False)
                #self.hidden = False
                self.bt_articulos.setText("Artículos")
                self.act.setText("Artículos")
                self.action_borrararticulo.setEnabled(False)
                self.action_editararticulo.setEnabled(False)
                self.action_nuevoarticulo.setEnabled(False)
                self.bt_borrararticulo.setEnabled(False)
                self.bt_editararticulo.setEnabled(False)
                self.bt_nuevoarticulo.setEnabled(False)
            else:
                self.fr_inferior.setVisible(True)
                #self.frame_arbol_superior.show()
                #self.frame_arbol_superior.hide()
                self.hidden = True
                self.bt_articulos.setText("Cerrar Artículos")
                self.act.setText("Cerrar Artículos")
                self.action_borrararticulo.setEnabled(True)
                self.action_editararticulo.setEnabled(True)
                self.action_nuevoarticulo.setEnabled(True)
                self.bt_borrararticulo.setEnabled(True)
                self.bt_editararticulo.setEnabled(True)
                self.bt_nuevoarticulo.setEnabled(True)


            #self.tree_apuntes.deleteLater()
            #self.tree_apuntes.destroy()
            
            
    @QtCore.pyqtSlot(QtWidgets.QTableWidgetItem)    
    def tablewidget_on_item_changed(self, item: QtWidgets.QTableWidgetItem) -> None:
        #print(f"Se modificó el item en posición ({item.row()}, {item.column()}, {item.text()})") 
        pass
        """if (item == None):
            item = self.tree_tablewidget.currentItem()
            id = self.tree_apuntes.item(item.row(),0).text()
        
            bd.tablewidget_on_item_changed(item,self.tablewidget)
            if item.column()==0:   
                pass
                #tb_datos = self.findChild(QtWidgets.QTableWidget, "tb_aplicaciones")
            
            #bd.update_url(id,item.text())
            if item.column()==1:   
                pass
            #tb_datos = self.findChild(QtWidgets.QTableWidget, "tb_aplicaciones")
            #id = tb_datos.item(item.row(),0).text()
            #bd.update_logo(id,item.text())           """

        
        #self.myframe = self.findChild(QFrame, 'fr_inferior')
        #self.myframe.window(window)

class myWidget(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        uic.loadUi('w_arbol.ui', self)        
        
        

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Inicio_listas()
    
    window.show()
    app.exec()