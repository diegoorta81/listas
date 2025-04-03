import sqlite3



class Db_SQLITE:

    #__path = "C:\trabajo\python\lista_aplicaciones\datos\aplicaciones.db"
    __path = ".\\datos\\listas.bd"
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
            print('Ha ocurrido un error y se ha revertido la transacción: (1) {tipoError} (2) {valorError}')
        else: 
            self.conexion.commit()
            self.cursor.close()
            self.conexion.close()

    
    
    
    

    