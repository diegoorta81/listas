from PyQt5 import QtCore, QtGui, uic, QtWidgets
from db_sqlite import Db_SQLITE

from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItem, QTableWidgetItem



class bd:
    sql = 'select id,nombre from t_articulos where padre is null order by nombre'
    
    def ejecuta():
        
        try:
            with Db_SQLITE() as cursor:
                cursor.execute(bd.sql)
                resultados = cursor.fetchall()
                return resultados
                #for resultado in resultados: print(list(resultado)[0])
        except Exception as error: print(f'Ha ocurrido un error: (1) {type(error)} (2) {error}')

    

    def refresca(tb_datos,datos):
        tb_datos.setHeaderLabels(['Artículos'])
        tb_datos.setColumnCount(1)
        tb_datos.resizeColumnToContents(0)
        
        

        level = 0
        for registro in datos:
            uno = QTreeWidgetItem(tb_datos)
            
            uno.setText(0,str(registro[0])+".- "+str(registro[1]))
            uno.setText(1,str(registro[0]))
            #uno.setEditable(True)

            tb_datos.insertTopLevelItem(level,uno)
            
            bd.tienehijos(tb_datos,level,uno,str(registro[1]))

    def tienehijos(tb_datos,level,uno,nombre):
        bd.sql = 'select id,nombre from t_articulos where padre="'+ nombre + '" order by nombre'
        datos = bd.ejecuta()
        level =+ 1
        for registro in datos:
            dos = QTreeWidgetItem(uno)
            dos.setText(0,str(registro[0])+".- "+str(registro[1]))
            dos.setText(1,str(registro[0]))
            #dos.setText(1,str(registro[1]))
            
            uno.addChild(dos)
            bd.tienehijos(tb_datos,level,dos,str(registro[0]))
        


     
    def onItemClicked(item,tablewidget):
        
        if (tablewidget.rowCount()>0):
            tablewidget.setRowCount(0)

            
        datos = bd.ejecuta_select("select nombre,descripcion,padre,palabras from t_articulos where id="+item.text(1))
        fila = 0
        for registro in datos:
            
            tablewidget.insertRow(fila)
            
            item_nombre = QTableWidgetItem(str(registro[0]))
            item_nombre.setFlags( item_nombre.flags() | QtCore.Qt.ItemIsEditable )
            tablewidget.setItem(fila,1, item_nombre)

            item_descripcion = QTableWidgetItem(registro[1])
            item_descripcion.setFlags( item_nombre.flags() | QtCore.Qt.ItemIsEditable )
            tablewidget.setItem(fila,2, item_descripcion)

            item_padre = QTableWidgetItem(registro[2])
            item_padre.setFlags( item_nombre.flags() | QtCore.Qt.ItemIsEditable )
            tablewidget.setItem(fila,3, item_padre)

            item_palabras = QTableWidgetItem(registro[3])
            item_palabras.setFlags( item_nombre.flags() | QtCore.Qt.ItemIsEditable )
            tablewidget.setItem(fila,4, item_palabras)

            

            fila+=1
           
            tablewidget.resizeColumnsToContents()
            tablewidget.verticalHeader().setVisible(True)

        print(item.text(0))
        print(item.text(1))

        
        

    def act_nuevoarticulo(self):
        print("nuevo articulo")
        print(self.sql)
    
    def act_editararticulo(self):
        print("editar articulo")

    def act_borrararticulo(self):
        print("borrar articulo")

            
            
        
        
        





    def ordena():
        bd.__sql = bd.__sql + " order by id_tipo"
        bd.inicio()


    def ejecuta_select(sql):
        try:
            with Db_SQLITE() as cursor:
                cursor.execute(sql)
                resultados = cursor.fetchall()
                return resultados
        except Exception as error: print(f'Ha ocurrido un error: (1) {type(error)} (2) {error}')

    def tablewidget_on_item_changed():
        pass