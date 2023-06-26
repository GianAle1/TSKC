import pyodbc
from ConfigurarConexionBD import DB_DRIVER, DB_SERVER, DB_DATABASE, DB_USERNAME, DB_PASSWORD

class Reo:

    def __init__(self):
        server='MSI\SQLEXPRESS'
        bd='SSPP'
        usuario='sa'
        contrasena='72792766'
        self.cnn=pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; SERVER='+server+' ;DATABASE='+bd+';UID='+usuario+';PWD='+contrasena)

    def __str__(self):
        datos=self.consulta_preso()        
        aux=""
        for row in datos:#contatenamos
             aux=aux + str(row) + "\n"
        return aux

    def consulta_preso(self):
        cur = self.cnn.cursor()
        cur.execute("SELECT *FROM dbo.ObtenerDatosRecluso()")
        datos = cur.fetchall()
        cur.close()    
        return datos
   
    def buscar_preso(self, Id):
            cur = self.cnn.cursor()
            sql= "SELECT * FROM countries WHERE Id = {}".format(Id)
            cur.execute(sql)
            datos = cur.fetchone()
            cur.close()    
            return datos

    def inserta_preso(self, Nombre, Apellido,Crimen):
        cur = self.cnn.cursor()
        sql='''INSERT INTO preso (Nombre,Apellido,Crimen) VALUES('{}', '{}','{}')'''.format( Nombre, Apellido,Crimen)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n    

    def elimina_preso(self,Id):
        cur = self.cnn.cursor()
        sql='''DELETE FROM countries WHERE Id = {}'''.format(Id)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n   

    def modifica_preso(self,Id, ISO3, CountryName, Capital, CurrencyCode):
        cur = self.cnn.cursor()
        sql='''UPDATE countries SET ISO3='{}', CountryName='{}', Capital='{}',
        CurrencyCode='{}' WHERE Id={}'''.format(ISO3, CountryName, Capital, CurrencyCode,Id)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n   
