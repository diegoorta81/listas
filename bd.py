#23/04/25
from PyQt5 import QtCore, QtGui, uic, QtWidgets
from db_sqlite import Db_SQLITE
from PyQt5.QtGui import QImage,QPixmap,QColor
from PyQt5.QtCore import QPoint,Qt,QByteArray,QIODevice,QBuffer
from PyQt5.QtWidgets import QTreeWidget,QTableWidget, QTreeWidgetItem, QTableWidgetItem
from tkinter import messagebox


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

    def ejecuta_insert(sql):
        
        try:
            with Db_SQLITE() as cursor:
                cur = cursor.execute(sql)
                return cur.lastrowid
            #for resultado in resultados: print(list(resultado)[0])
        except Exception as error:
            #print(messagebox.askyesno(message="¿Desea continuar?", title="Título"))
            raise Exception(error,"Error")

    def ejecuta_delete(id):
        try:
            with Db_SQLITE() as cursor:
                sql = "delete from t_articulos where id=?"
                cursor.execute(sql,[id,])
        except Exception as error:
            #print(messagebox.askyesno(message="¿Desea continuar?", title="Título"))
            raise Exception(error,"Error")

    def ejecuta_update(id,campo,valor):            
        try:
            with Db_SQLITE() as cursor:
                sql = "update from t_articulos set ?=? where id=?"
                data = (campo, valor, id)
                cursor.execute(sql,data)
        except Exception as error:
            #print(messagebox.askyesno(message="¿Desea continuar?", title="Título"))
            raise Exception(error,"Error")

    def refresca(tb_datos,datos):
        tb_datos.setHeaderLabels(['Artículos'])
        tb_datos.setColumnCount(1)
        tb_datos.resizeColumnToContents(0)
        
        

        level = 0
        for registro in datos:
            uno = QTreeWidgetItem(tb_datos)
            
            uno.setText(0,str(registro[1]))
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
            dos.setText(0,str(registro[1]))
            dos.setText(1,str(registro[0]))
            #dos.setText(1,str(registro[1]))
            
            uno.addChild(dos)
            bd.tienehijos(tb_datos,level,dos,str(registro[1]))
        


     
    def tree_articulos_onItemClicked(self):
            #item,tablewidget):
                
        item = self.findChild(QtWidgets.QTreeWidget, 'tree_articulos').currentItem()
        tablewidget = self.findChild(QtWidgets.QTableWidget, 'tablewidget')
        
        if (tablewidget.rowCount()>0):
            tablewidget.setRowCount(0)

            
        datos = bd.ejecuta_select("select id,nombre,padre,descripcion,palabras from t_articulos where id="+item.text(1)+ " or padre='"+item.text(0)+"' order by padre,nombre")
        fila = 0
        for registro in datos:
            
            tablewidget.insertRow(fila)
            
            item_id = QTableWidgetItem(str(registro[0]))
            item_id.setFlags( item_id.flags() | QtCore.Qt.ItemIsEditable )
            tablewidget.setItem(fila,0, item_id)

            item_nombre = QTableWidgetItem(registro[1])
            item_nombre.setFlags( item_nombre.flags() | QtCore.Qt.ItemIsEditable )
            tablewidget.setItem(fila,1, item_nombre)

            item_descripcion = QTableWidgetItem(registro[2])
            item_descripcion.setFlags( item_nombre.flags() | QtCore.Qt.ItemIsEditable )
            tablewidget.setItem(fila,2, item_descripcion)

            item_padre = QTableWidgetItem(registro[3])
            item_padre.setFlags( item_nombre.flags() | QtCore.Qt.ItemIsEditable )
            tablewidget.setItem(fila,3, item_padre)

            item_palabras = QTableWidgetItem(registro[4])
            item_palabras.setFlags( item_nombre.flags() | QtCore.Qt.ItemIsEditable )
            tablewidget.setItem(fila,4, item_palabras)

            

            fila+=1
           
            tablewidget.resizeColumnsToContents()
            tablewidget.verticalHeader().setVisible(True)

        

        #print(item.text(0))
        #print(item.text(1))

        
    
    def act_nuevoarticulo(self):        
        tree_articulos = self.findChild(QtWidgets.QTreeWidget, 'tree_articulos')
        item = tree_articulos.currentItem()
        
        sql = "select count(*) from t_articulos where nombre=?"
        nombre = item.text(0)
        cursor = bd.ejecuta_select_(sql,(nombre,))
        i=0
        while cursor[0][0]>0:
            i = i + 1
            nombre1 = nombre+"_"+str(i)
            cursor = bd.ejecuta_select_(sql,(nombre1,))

        
        if not(item):
            padre = 'Null'
            sql = "insert into t_articulos (nombre,padre) values ('"+nombre1+"',"+padre+")"
        else:
            padre = item.text(0)
            sql = "insert into t_articulos (nombre,padre) values ('"+nombre1+"','"+padre+"')"
        
        try:
            id = bd.ejecuta_insert(sql)
            uno = QTreeWidgetItem(item)
            uno.setText(0,nombre1)
            uno.setText(1,str(id))
            if padre == 'Null':
                self.findChild(QtWidgets.QTreeWidget, 'tree_articulos').insertTopLevelItem(0,uno)
            else:
                self.findChild(QtWidgets.QTreeWidget, 'tree_articulos').currentItem().addChild(uno)
            #uno.setEditable(True)
            #my_tree.setCurrentItem(my_tree.topLevelItem(0))
        except Exception as error:
            messagebox.showinfo(message=error, title="Error")
        
        
        ##
        
        
        #tablewidget = self.findChild(QtWidgets.QTableWidget, 'tablewidget')
        #tablewidget_img = self.findChild(QtWidgets.QTableWidget, 'tablewidget_img')
        
        
        
    
    def act_editararticulo(item, tablewidget):
        columna = item.column()
        fila = item.row()
        id = tablewidget.item(fila,0).text()
        if columna==1:
            bd.ejecuta_update(id,"nombre",item.text())
        

        
        
        print("editar articulo: "+ item.text()+ " - columna: "+str(columna)+ " - fila: "+str(fila) )

    def act_borrararticulo(self):

        tree_articulos = self.findChild(QtWidgets.QTreeWidget, 'tree_articulos')
        item = tree_articulos.currentItem()

        sql = "select count(*) from t_articulos where padre=?"
        cursor = bd.ejecuta_select_(sql,(item.text(0),))
        if cursor[0][0]>0:
            messagebox.showinfo(message="Este artículo incluye subartículos ", title="Artículo con hijos")
            return
        resultado = messagebox.askokcancel("Salir", 
            "¿Borrar el artículo actual, "+item.text(0)+"?")
        if not resultado:
            return

        id = item.text(1)
        #bd.tienehijos
        try:
            bd.ejecuta_delete(id)
            parent = item.parent()
            if parent:
                parent.removeChild(item)
            else:
                tree_articulos.takeTopLevelItem(tree_articulos.indexOfTopLevelItem(item))
            
        except Exception as error:
            messagebox.showinfo(message=error, title="Error")




            
            
        
        
        





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


    def ejecuta_select_(sql,tupla):
        try:
            with Db_SQLITE() as cursor:
                cursor.execute(sql,tupla)
                resultados = cursor.fetchall()
                return resultados
        except Exception as error: print(f'Ha ocurrido un error: (1) {type(error)} (2) {error}')    

    def tablewidget_on_item_clicked(self,id_articulo):
        sql = "select archivo,descripcion from t_archivos where id_padre=?"
        cursor = bd.ejecuta_select_(sql,(id_articulo,))
        tablewidget_img = self.findChild(QtWidgets.QTableWidget, 'tablewidget_img')
        tablewidget_img.setSortingEnabled(True)
        tablewidget_img.setRowCount(0)

        fila = 0
        for registro in cursor:
            tablewidget_img.insertRow(fila)
            
            foto = QPixmap()
            bandera = foto.loadFromData(registro[0],"JPG",Qt.AutoColor)
            if bandera is True:
                label = QtWidgets.QLabel()
                label.setPixmap(foto)
                tablewidget_img.setCellWidget(fila,0, label)
            if bandera is False:
                bandera = foto.loadFromData(registro[0],"PNG",Qt.AutoColor)
                if bandera is True:
                    label = QtWidgets.QLabel()
                    label.setPixmap(foto)
                    tablewidget_img.setCellWidget(fila,0, label)
            
            
            if bandera is False:
                
                text = registro[0].decode()
                item_archivo = QTableWidgetItem(text)
                tablewidget_img.setItem(fila,0, item_archivo)
            
            #self.lbl_imagen.setPixmap(foto)
            #item_imagen = QTableWidgetItem(str(registro[0]))
            #item_imagen.setPixmap(foto)
            #item_id.setFlags( item_id.flags() | QtCore.Qt.ItemIsEditable )
            

            item_descripcion = QTableWidgetItem(registro[1])
            #item_id.setFlags( item_id.flags() | QtCore.Qt.ItemIsEditable )
            tablewidget_img.setItem(fila,1, item_descripcion)
            
            fila+=1
           
            tablewidget_img.resizeColumnsToContents()
            tablewidget_img.resizeRowsToContents()
            tablewidget_img.verticalHeader().setVisible(True)
