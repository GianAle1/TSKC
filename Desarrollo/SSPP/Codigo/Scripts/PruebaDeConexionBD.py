import pyodbc

try:
    server = 'DESKTOP-NSR7F45\SQLEXPRESS'
    bd = 'SSPP'
    usuario = 'sa'
    contrasena = 'murcielago123'
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; SERVER=' + server + ' ;DATABASE=' + bd + ';UID=' + usuario + ';PWD=' + contrasena)
    print("conexion exitosa")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Crimen")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
except Exception as ex:
    print(ex)