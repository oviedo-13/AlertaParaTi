from ConnectionInfoAzure import server, database, username, password, driver
from dataSyncronizationAzureOracle import AzureDB
import numpy
import random
import datetime

fechas = ['2022-10-03', '2022-10-04', '2022-10-05', '2022-10-06', '2022-10-07', '2022-10-08', '2022-10-09']

azure = AzureDB(server, database, username, password, driver)

normal_dist_seconds = numpy.random.normal(size=400)
normal_dist_seconds += -1 * normal_dist_seconds.min()
normal_dist_seconds *= 60

for x in normal_dist_seconds:
    random_fecha_inicio = random.choices(fechas, weights=[0.18, 0.2, 0.25, 0.15, 0.15, 0.05, 0.02])
    random_hora_inicio = random.choices([x for x in range(0, 24)], weights=[0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.1, 0.1, 
                                                 0.1, 0.03, 0.04, 0.05, 0.01, 0.01, 0.1, 0.1, 0.01, 0.1, 
                                                 0.06, 0.05, 0.04, 0.1, 0.01])
    random_minuto_inicio = random.choice(['00', '01', '02', '03', '04', '05', '06', '07', '08', '09'] + [x for x in range(10, 60)])
    random_segundo_inicio = random.choice(['00', '01', '02', '03', '04', '05', '06', '07', '08', '09'] + [x for x in range(10, 60)])
    
    date_inicio = datetime.datetime.strptime(f"{random_fecha_inicio[0]} {random_hora_inicio[0]}:{random_minuto_inicio}:{random_segundo_inicio}", "%Y-%m-%d %H:%M:%S")
    date_final = date_inicio + datetime.timedelta(seconds=x)
    date_inicio = date_inicio.strftime("%Y-%m-%d %H:%M:%S")
    date_final = date_final.strftime("%Y-%m-%d %H:%M:%S")
    
    azure.insert_query(f"INSERT INTO Sesiones (tiempo_inicio, tiempo_fin) VALUES ('{date_inicio}', '{date_final}')")
    


