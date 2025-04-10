import sqlite3
import os
from tkinter import Toplevel, messagebox


class Db_SQLITE:

    ui_path = os.path.dirname(os.path.abspath(__file__))

       
    #__path = "C:\trabajo\python\lista_aplicaciones\datos\aplicaciones.db"
    __path = ui_path +"\\datos\\listas.bd"
    __BASE_DATOS = "listas.bd"
    
    
    def __init__(self):
        self.instancia = {
            'database': Db_SQLITE.__BASE_DATOS
        }    

    def __enter__(self):
        self.conexion = sqlite3.connect(self.__path)
        self.cursor = self.conexion.cursor()
        return self.cursor

    def __exit__(self, tipoError, valorError, trazaError):
        if tipoError:
            self.conexion.rollback()
            self.cursor.close()
            self.conexion.close()
            #messagebox.showerror("Error", tipoError + " // "+ valorError)
            
            #print('Ha ocurrido un error y se ha revertido la transacción: (1) {tipoError} (2) {valorError}')
        else: 
            self.conexion.commit()
            self.cursor.close()
            self.conexion.close()

    
    
    
    

    