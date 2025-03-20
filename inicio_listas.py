import sys, os
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6 import uic
from bd import bd
from PyQt6.QtWidgets import QTreeWidget, QTreeWidgetItem, QFrame, QWidget
from PyQt6.QtGui import QAction

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


    


    def act_articulos(self):
        self.frame_arbol_superior = self.fr_inferior.findChild(QFrame, 'frame_arbol_superior')
        #self.fr_inferior = self.findChild(QFrame, 'fr_inferior')
        
        if (self.frame_arbol_superior is None):
            
            self.fr_inferior = self.findChild(QFrame, 'fr_inferior')

            uic.loadUi('w_arbol.ui',self.fr_inferior)

            self.tree_apuntes = self.findChild(QtWidgets.QTreeWidget, 'tree_cuentas')
            self.apuntes = bd.ejecuta()
            self.bt_articulos.setText("Cerrar Artículos")
            self.act.setText("Cerrar Artículos")
            #self.action_borrararticulo.setEnabled(True)
            #self.action_editararticulo.setEnabled(True)
            #self.action_nuevoarticulo.setEnabled(True)
            #self.bt_borrararticulo.setEnabled(True)
            #self.bt_editararticulo.setEnabled(True)
            #self.bt_nuevoarticulo.setEnabled(True)

            bd.refresca(self.tree_apuntes,self.apuntes)
        else:
            
            if (self.hidden==True):
                self.frame_arbol_superior.hide()
                self.hidden = False
                self.bt_articulos.setText("Artículos")
                self.act.setText("Artículos")
                self.action_borrararticulo.setEnabled(False)
                self.action_editararticulo.setEnabled(False)
                self.action_nuevoarticulo.setEnabled(False)
                self.bt_borrararticulo.setEnabled(False)
                self.bt_editararticulo.setEnabled(False)
                self.bt_nuevoarticulo.setEnabled(False)
            else:
                self.frame_arbol_superior.show()
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