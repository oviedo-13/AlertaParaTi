import pyodbc
server = 'alerta-para-ti.database.windows.net'
database = 'alerta-para-ti'
username = 'alerta-para-ti'
password = '#teamdinamica2022'   
driver= '{ODBC Driver 18 for SQL Server}'

with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM paginas")
        row = cursor.fetchone()
        while row:
            print (row)
            row = cursor.fetchone()