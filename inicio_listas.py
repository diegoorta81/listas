# 21/04/25
import sys, os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QFrame, QHBoxLayout, QSplitter, QLineEdit, QFrame,QTreeWidget, QTreeWidgetItem,QMainWindow, QAction, QMenu

from PyQt5 import uic
from bd import bd
from PyQt5.QtCore import Qt
#from PyQt6.QtGui import QAction

class Inicio_listas(QtWidgets.QMainWindow):

    def __init__(self):
    
        super(Inicio_listas,self).__init__()
        ui_path = os.path.dirname(os.path.abspath(__file__))

        uic.loadUi(os.path.join(ui_path, "inicio_listas.ui"), self)


        self.context_menu = QMenu(self)
        action1 = self.context_menu.addAction("Action 1")
        action2 = self.context_menu.addAction("Action 2")
        action3 = self.context_menu.addAction("Action 3")

        action1.triggered.connect(self.handle_action1)
        action2.triggered.connect(self.handle_action2)
        action3.triggered.connect(self.handle_action3)

        
        self.bt_articulos = self.findChild(QtWidgets.QPushButton, 'bt_articulos')
        self.bt_articulos.setText("Artículos")
        self.bt_articulos.clicked.connect(self.act_articulos)

        self.act = self.findChild(QAction, 'action_articulos')
        self.act.triggered.connect(self.act_articulos)
        self.hidden = True

        

        self.bt_nuevoarticulo = self.findChild(QtWidgets.QPushButton, 'bt_nuevoarticulo')
        self.bt_nuevoarticulo.clicked.connect( lambda state, btn=self : bd.act_nuevoarticulo(btn))
        
        self.action_nuevoarticulo = self.findChild(QAction, 'action_nuevoarticulo')
        self.action_nuevoarticulo.triggered.connect( lambda state, btn=self : bd.act_nuevoarticulo(btn))

        self.bt_editararticulo = self.findChild(QtWidgets.QPushButton, 'bt_editararticulo')
        self.bt_editararticulo.clicked.connect(bd.act_editararticulo)
        
        self.action_editararticulo = self.findChild(QAction, 'action_editararticulo')
        self.action_editararticulo.triggered.connect(bd.act_editararticulo)

        self.bt_borrararticulo = self.findChild(QtWidgets.QPushButton, 'bt_borrararticulo')
        self.bt_borrararticulo.clicked.connect( lambda state, btn=self : bd.act_borrararticulo(btn))
        
        self.action_borrararticulo = self.findChild(QAction, 'action_borrararticulo')
        self.action_borrararticulo.triggered.connect( lambda state, btn=self : bd.act_borrararticulo(btn))
        

        self.action_borrararticulo.setEnabled(False)
        self.action_editararticulo.setEnabled(False)
        self.action_nuevoarticulo.setEnabled(False)
        self.bt_borrararticulo.setEnabled(False)
        self.bt_editararticulo.setEnabled(False)
        self.bt_nuevoarticulo.setEnabled(False)


    #def tree_articulos_onItemClicked(self):
        #item = self.tree_articulos.currentItem()
        
#        bd.tree_articulos_onItemClicked(item,self.tablewidget)
        #bd.tree_articulos_onItemClicked(self,item.text(1))
        


    def act_articulos(self):
        self.frame_arbol_superior = self.fr_inferior.findChild(QFrame, 'frame_arbol_superior')
        #self.fr_inferior = self.findChild(QFrame, 'fr_inferior')
        
        if (self.frame_arbol_superior is None):
                   
            self.fr_inferior = self.findChild(QFrame, 'fr_inferior')
            mod_path = __file__

            uic.loadUi( os.path.dirname(__file__)+  '\\w_arbol.ui',self.fr_inferior)
            
            self.hbox = self.findChild(QtWidgets.QHBoxLayout, 'horizontalLayout_2')

            self.fr_inferior.setLayout(self.hbox)


            self.tree_articulos = self.findChild(QtWidgets.QTreeWidget, 'tree_articulos')
            

            self.tablewidget = self.findChild(QtWidgets.QTableWidget, 'tablewidget')
            
            self.tablewidget.setSortingEnabled(True)
            
            

            self.tablewidget_img = self.findChild(QtWidgets.QTableWidget, 'tablewidget_img')
            #self.tablewidget_img.setColumnHidden(0,True)
            self.tablewidget.setColumnHidden(0,True)
            self.fr_tree_articulos = self.findChild(QtWidgets.QFrame, 'fr_tree_articulos')
            self.fr_table = self.findChild(QtWidgets.QFrame, 'fr_table')
            
            
            self.articulos = bd.ejecuta()

            self.splitter2 = QSplitter(Qt.Orientation.Vertical)
            self.splitter2.addWidget(self.tablewidget)
            self.splitter2.addWidget(self.tablewidget_img)
            self.splitter2.setSizes([300,300])
            self.hbox.addWidget(self.splitter2)

            self.splitter1 = QSplitter(Qt.Orientation.Horizontal)
            self.splitter1.addWidget(self.tree_articulos)
            self.splitter1.addWidget(self.splitter2)

            self.splitter1.setSizes([300,300])
            self.hbox.addWidget(self.splitter1)
            self.tablewidget.itemChanged.connect(self.tablewidget_on_item_changed) 
            self.tablewidget.itemClicked.connect(self.tablewidget_on_item_clicked) 

            
            
            

            
            

            self.bt_articulos.setText("Cerrar Artículos")
            self.act.setText("Cerrar Artículos")
            self.action_borrararticulo.setEnabled(True)
            self.action_editararticulo.setEnabled(True)
            self.action_nuevoarticulo.setEnabled(True)
            self.bt_borrararticulo.setEnabled(True)
            self.bt_editararticulo.setEnabled(True)
            self.bt_nuevoarticulo.setEnabled(True)
            #self.tree_articulos.itemClicked.connect(self.tree_articulos_onItemClicked)
            self.tree_articulos.itemClicked.connect(self.tree_articulos_onItemClicked)
                
            bd.refresca(self.tree_articulos,self.articulos)
            
            
            
            #self.bt_nuevoarticulo.clicked.connect( lambda state, btn=self : bd.act_nuevoarticulo(btn))
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
            
    def tree_articulos_onItemClicked(self):
        bd.tree_articulos_onItemClicked(self)
    
            
    @QtCore.pyqtSlot(QtWidgets.QTableWidgetItem)    
    def tablewidget_on_item_changed(self, item: QtWidgets.QTableWidgetItem) -> None:
        #print(f"Se modificó el item en posición ({item.row()}, {item.column()}, {item.text()})") 
        #print("Tree clicados")
        #pass
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

    @QtCore.pyqtSlot(QtWidgets.QTableWidgetItem)    
    def tablewidget_on_item_clicked(self, item: QtWidgets.QTableWidgetItem) -> None:
        #print(f"Se modificó el item en posición ({item.row()}, {item.column()}, {item.text()})") 
        #print("Articulos clicados")
        tablewidget = self.findChild(QtWidgets.QTableWidget, 'tablewidget')
        row = tablewidget.currentRow()
        print(tablewidget.item(row,0).text())
            #tablewidget.currentRow()
             # currentItem().row())
        bd.tablewidget_on_item_clicked(self,tablewidget.item(row,0).text())

    def contextMenuEvent(self, event):
        print(event.globalPos())
        self.context_menu.exec(event.globalPos())
    
    def handle_action1(self):
        print("Action 1 ejecutada")
        
    def handle_action2(self):
        print("Action 2 ejecutada")        
    
    def handle_action3(self):
        print("Action 3 ejecutada")
        

class myWidget(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        uic.loadUi('w_arbol.ui', self)        
        
        

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Inicio_listas()
    
    window.show()
    app.exec()