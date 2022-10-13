from sqlite3 import Cursor
import cx_Oracle
import pyodbc
    

# Generic class for both databases
class database:
    def print_select(self, query):
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)
            
    def return_select(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()
            
            
    # return the last date of the table
    def get_most_recent_date(self, table_name, column_name):
        self.cursor.execute(f'Select max({column_name}) from {self.workspace+table_name}')
        return self.cursor.fetchone()[0]
    
    
    # truncate the table provided
    def truncate(self, table_name):
        self.cursor.execute(f'Truncate table {self.workspace+table_name}')
        self.cursor.execute('commit')
        
        
    # print all the data from a singular query
    def print_select(self, query):
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)
            
    
    def insert_query(self, query):
        self.cursor.execute(query)
        self.cursor.execute('commit')
                
    
    # return a cursor with all the data from the table from the date provided until today
    def get_data_between_dates(self, table_name, date, column_name):
        self.cursor.execute(f"SELECT * FROM {self.workspace+table_name} WHERE {column_name} > '{date}'")
        return self.cursor.fetchall()

class OracleDB(database):
    # Connect into the Oracle database
    def __init__(self, username, password, dsn, workspace):
        print('Connecting to Oracle...')
        self.connOracle = cx_Oracle.connect(username, password, dsn)
        print('Connected to Oracle')
        self.cursor = self.connOracle.cursor()
        self.workspace = workspace
        
    
    def insert_into_paginas(self, id, pagina, fecha):
        try:
            self.cursor.execute(
                f"""INSERT INTO {self.workspace}PAGINAS 
                    VALUES (
                            {id}, 
                            '{pagina}', 
                            TO_DATE('{fecha}', 
                            'YYYY-MM-DD HH24:MI:SS')
                            )""")
            print('successful insert')
            self.cursor.execute('commit')
        except Exception as e:
            print(e)
            print('failed insert')
            
    
    # Insert multiple values into paginas from a cursor or iteration
    def bulk_insert_into_paginas(self, cursor):
        for row in cursor:
            self.insert_into_paginas(row[0], row[1], row[2])
            
    def insert_into_sesiones(self, id, tiempo_inicio, tiempo_fin):
        try:
            self.cursor.execute(
                f"""INSERT INTO {self.workspace}SESIONES
                    VALUES (
                            {id}, 
                            TO_DATE('{tiempo_inicio}', 'YYYY-MM-DD HH24:MI:SS'), 
                            TO_DATE('{tiempo_fin}', 'YYYY-MM-DD HH24:MI:SS')
                            )""")
            self.cursor.execute('commit')
            print('successful insert')
        except Exception as e:
            print(e)
            print('failed insert')
            
    
    # Insert multiple values into sesiones from a cursor or iteration
    def bulk_insert_into_sesiones(self, cursor):
        for row in cursor:
            self.insert_into_sesiones(row[0], row[1], row[2])
            
    
    def insert_into_clima(self, id, temperatura, porcentaje_lluvia, indice_uv, calidad_aire, fecha):
        try:
            self.cursor.execute(
                f"""INSERT INTO {self.workspace}CLIMA
                    VALUES (
                            {id},
                            {temperatura},
                            {porcentaje_lluvia},
                            {indice_uv},
                            {calidad_aire},
                            TO_DATE('{fecha}', 'YYYY-MM-DD HH24:MI:SS'))"""
            )
            self.cursor.execute('commit')
            print('successful insert')
        except Exception as e:
            print(e)
            print('failed insert')	
            
    
    def bulk_insert_into_clima(self, cursor):
        for row in cursor:
            self.insert_into_clima(row[0], row[1], row[2], row[3], row[4], row[5])
            
            
    def insert_into_sismo(self, id, ubicacion, magnitud, longitud, latitud, fecha_actualizacion, fecha):
        try:
            self.cursor.execute(
                f"""INSERT INTO {self.workspace}SISMO
                    VALUES (
                        '{id}',
                        '{ubicacion}',
                        {magnitud},
                        {longitud},
                        {latitud},
                        TO_DATE('{fecha_actualizacion}', 'YYYY-MM-DD HH24:MI:SS'),
                        TO_DATE('{fecha}', 'YYYY-MM-DD HH24:MI:SS'))"""
            )
            self.cursor.execute('commit')
            print('successful insert')
            
        except Exception as e:
            print(e)
            self.cursor.execute(
                f"""UPDATE {self.workspace}SISMO
                    SET ubicacion = '{ubicacion}',
                        magnitud = {magnitud},
                        longitud = {longitud},
                        latitud = {latitud},
                        fecha_actualizacion = TO_DATE('{fecha_actualizacion}', 'YYYY-MM-DD HH24:MI:SS'),
                        fecha = TO_DATE('{fecha}', 'YYYY-MM-DD HH24:MI:SS')
                     WHERE id = '{id}'"""
            )
            print('updated')
            

    def bulk_insert_into_sismo(self, cursor):
        for row in cursor:
            self.insert_into_sismo(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
            
    
    def insert_into_incidentes(self, id, tipo_id, tiempo_inicio, tiempo_final, desde_lugar, hasta_lugar, longitud_metros):
        try:
            self.cursor.execute(
                f"""INSERT INTO {self.workspace}INCIDENTES
                    VALUES (
                            '{id}',
                            {tipo_id},
                            TO_DATE('{tiempo_inicio}', 'YYYY-MM-DD HH24:MI:SS'),
                            {f"TO_DATE('{tiempo_final}', 'YYYY-MM-DD HH24:MI:SS')" if tiempo_final != None else 'NULL'},
                            '{desde_lugar}',
                            '{hasta_lugar}',
                            {longitud_metros})""")
            self.cursor.execute('commit')
            print('successful insert')
        except Exception as e:
            print(e)
            print('failed insert')
            
    def bulk_insert_into_incidentes(self, cursor):
        for row in cursor:
            self.insert_into_incidentes(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
            
    
    def insert_into_incidentes_coordenadas(self, id, id_incidente, longitud, latitud, fecha_actualizacion):
        try:
            self.cursor.execute(
                f"""INSERT INTO {self.workspace}INCIDENTES_COORDENADAS
                    VALUES (
                            '{id}',
                            '{id_incidente}',
                            {longitud},
                            {latitud},
                            TO_DATE('{fecha_actualizacion}', 'YYYY-MM-DD HH24:MI:SS'))""")
            self.cursor.execute('commit')
            print('successful insert')
        except:
            print('failed insert')
            
            
    def bulk_insert_into_incidentes_coordenadas(self, cursor):
        for row in cursor:
            self.insert_into_incidentes_coordenadas(row[0], row[1], row[2], row[3], row[4])
    
    
    # se le pasa un cursor con los datos de la tabla y se borran de la tabla
    def delete_from_incidentes_coordenadas(self, id_incidente_tuple):
        try:
            for id_incidente in id_incidente_tuple:
                self.cursor.execute(
                    f"""DELETE FROM {self.workspace}INCIDENTES_COORDENADAS
                        WHERE ID_INCIDENTE = '{id_incidente}'""")
                self.cursor.execute('commit')
                print('successful delete')
        except:
            print('failed delete')
            
            
class AzureDB(database):
    # Connect into the Azure database
    def __init__(self, server, database, username, password, driver) -> None:
        print('Connecting to Azure...')
        self.connAzure = pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+
                                        server+';PORT=1433;DATABASE='+database+';UID='+
                                        username+';PWD='+ password)
        print('Connected to Azure')
        self.cursor = self.connAzure.cursor()
        self.workspace = ''
                
    
def main():
    import ConnectionInfoOracle
    import ConnectionInfoAzure

    azure = AzureDB(ConnectionInfoAzure.server, 
                    ConnectionInfoAzure.database, 
                    ConnectionInfoAzure.username, 
                    ConnectionInfoAzure.password, 
                    ConnectionInfoAzure.driver)
    
    oracle = OracleDB(ConnectionInfoOracle.usernm, 
                      ConnectionInfoOracle.psswd, 
                      ConnectionInfoOracle.dsn, 
                      ConnectionInfoOracle.workspace)
    
    
    # función para obtener los datos de azure y meterlos en oracle, 
    # solo mete los valores que ya no existan utilizando la fecha
    def sync_tabla(tabla, columna):
        print(f'Syncing {tabla}...')
        # get the most recent date from the oracle database
        most_recent_date = oracle.get_most_recent_date(tabla, columna)
        print('Most recent date in Oracle: ', most_recent_date)
        # get the data from the azure database
        if most_recent_date == None:
            print('No data in oracle')
            data = azure.get_data_between_dates(tabla, '2020-01-01', columna)
        else:
            data = azure.get_data_between_dates(tabla, most_recent_date, columna)
        # data = azure.get_data_between_dates('PAGINAS', most_recent_date)
        print('Data to be inserted: ', data)
        # insert the data into the oracle database
        if tabla == 'paginas':
            oracle.bulk_insert_into_paginas(data)
        elif tabla == 'sesiones':
            oracle.bulk_insert_into_sesiones(data)
        # elif tabla == 'clima':
        #    oracle.bulk_insert_into_clima(data)
        elif tabla == 'sismo':
            oracle.bulk_insert_into_sismo(data)
        elif tabla == 'incidentes':
            oracle.bulk_insert_into_incidentes(data)
        elif tabla == 'incidentes_coordenadas':
            all_ids = (row[1] for row in data)
            # borra todos los datos para poner los actualizados
            oracle.delete_from_incidentes_coordenadas(all_ids)
            oracle.bulk_insert_into_incidentes_coordenadas(data)
                
                
        print('----------------------------------------\n')
        
        
    sync_tabla('paginas', 'fecha')
    sync_tabla('sesiones', 'tiempo_fin')
    # sync_tabla('clima', 'fecha')
    sync_tabla('sismo', 'fecha_actualizacion')
    sync_tabla('incidentes', 'tiempo_inicio')
    sync_tabla('incidentes_coordenadas', 'fecha_actualizacion')
        
        
if __name__ == '__main__':
    main()
    
