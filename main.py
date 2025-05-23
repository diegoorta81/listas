#https://www.youtube.com/watch?v=GmDxPFCRf8M
from PyQt5.QtWidgets import QMainWindow, QApplication, QGraphicsDropShadowEffect
from PyQt5.uic import loadUi
from PyQt5.QtCore import QPoint,Qt,QByteArray,QIODevice,QBuffer
from PyQt5 import QtCore,QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QImage,QPixmap,QColor,QIntValidator
import sqlite3
import sys

class Formulario(QMainWindow):
    def __init__(self):
        super(Formulario,self).__init__()
        loadUi('imagenes.ui',self)

        self.conexion = sqlite3.connect('C:/trabajo/python/listas/datos/base_datos.db')
        self.bt_normal.hide()
        self.click_posicion = QPoint()
        self.bt_minimo.clicked.connect(lambda :self.showMinimized())
        self.bt_maximo.clicked.connect(lambda :self.showMaximized())
        self.bt_normal.clicked.connect(self.control_bt_maximize)
        self.bt_close.clicked.connect(lambda :self.close())

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.gripSize = 10
        self.grip = QtWidgets.QSizeGrip(self)
        self.grip.resize(self.gripSize,self.gripSize)

        self.frame_superior.mouseMoveEvent = self.move_ventana

        self.bt_importar_img.clicked.connect(self.load_image)
        self.bt_limpiar.clicked.connect(self.clear_data)
        self.bt_guardar.clicked.connect(self.save_data)
        self.bt_buscar.clicked.connect(self.search_data)

        self.shadow_frame(self.frame_datos)
        self.shadow_frame(self.frame_buscar)
        self.in_telefono.setValidator(QIntValidator())

    def shadow_frame(self,frame):
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(10)
        shadow.setOffset(5,5)
        shadow.setColor(QColor(127,90,240,255))
        frame.setGraphicsEffect(shadow)
    
    def load_image(self,frame):
        filename = QFileDialog.getOpenFileName(
            filter="Image JPG(*.jpg);;Image PNG(*.png)")[0]
        if filename:
            pixmapImagen = QPixmap(filename).scaled(200,200,Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.img_preview.setPixmap(pixmapImagen)

    def clear_data(self):
        self.in_nombre.clear()
        self.in_telefono.clear()
        self.in_correo.clear()
        self.img_preview.clear()

    def save_data(self):
        nombre = self.in_nombre.text()
        telefono = self.in_telefono.text()
        correo = self.in_correo.text()
        foto = self.img_preview.pixmap()
        if foto:
            bArray = QByteArray()
            buff = QBuffer(bArray)
            buff.open(QIODevice.WriteOnly)
            foto.save(buff, "JPG")


        cursor = self.conexion.cursor()
        if cursor.execute("SELECT * FROM datos WHERE NOMBRE = ?", (nombre,)).fetchone():
            self.img_preview.setText("El usuario ya existe")
        elif len(nombre) <= 4:
            self.img_preview.setText("No hay nombre")
        elif len(correo) <= 4:
            self.img_preview.setText("No hay correo")
        elif len(telefono) <= 4:
            self.img_preview.setText("No hay telefono")
        #elif foto:
        try:
            self.conexion = sqlite3.connect('C:/trabajo/python/listas/datos/base_datos.db')
            cursor = self.conexion.cursor()
                #cursor.execute("INSERT INTO base_datos.datos_ VALUES (?,?,?)", (nombre,correo,telefono))
            #LSQL = "INSERT INTO base_datos.datos_ (NOMBRE,CORREO,TELEFONO) VALUES ('NOMBRE','CORREO','TELEFONO')"  
            #
            # 

            
            cursor.execute("INSERT INTO datos (NOMBRE,CORREO,TELEFONO,FOTO) VALUES (?,?,?,?)", (nombre,correo,telefono,bArray))
            self.conexion.commit()
            cursor.close()
            self.conexion.close()
            self.clear_data()
        

    
        except Exception as error: print(f'Ha ocurrido un error: (1) {type(error)} (2) {error}')
        #else:
            #self.img_preview.setText("No hay foto")

    def search_data(self):

        nombre_a_buscar = self.in_buscar_nombre.text()
        self.conexion = sqlite3.connect('C:/trabajo/python/listas/datos/base_datos.db')
        cursor = self.conexion.cursor()
        cursor.execute("SELECT * FROM datos WHERE NOMBRE='{}'".format(nombre_a_buscar))
        nombrex = cursor.fetchall()
        cursor.close()
        if nombrex:
            self.lbl_telefono.setText(f'Telefono: {nombrex[0][2]}')
            self.lbl_correo.setText(f'Correo: {nombrex[0][1]}')
            self.in_buscar_nombre.setText("")
            #foto = QPixmap()
            #foto.loadFromData(nombrex[0][3],"PNG",Qt.AutoColor)
            #self.lbl_imagen.setPixmap(foto)
        else:
            self.lbl_telefono.setText("Telefono: None")
            self.lbl_correo.setText("Correo: None")
            self.in_buscar_nombre.setText("")
            #self.imagen.clear()

    def control_bt_normal(self):
        self.showNormal()
        self.btn_normal.hide()
        self.bt_maximize.show()

    def control_bt_maximize(self):
        self.showMaximized()
        self.btn_normal.show()
        self.bt_maximize.hide()

    def resizeEvent(self, event):
        rect = self.rect()
        self.grip.move(rect.right()-self.gripSize, rect.bottom()-self.gripSize)

    def mousePressEvent(self, event):
        self.click_posicion = event.globalPos()
    
    def move_ventana(self,event):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_app = Formulario()
    my_app.show()
    sys.exit(app.exec_())