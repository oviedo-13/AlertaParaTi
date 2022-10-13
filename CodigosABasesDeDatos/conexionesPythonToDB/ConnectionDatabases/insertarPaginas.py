from ConnectionInfoAzure import server, database, username, password, driver
from dataSyncronizationAzureOracle import AzureDB
import random

paginas = ['Home', 'Noticias', 'Notificaciones', 'Clima', 
           'Tráfico', 'Estaciones', 'Alarmas', 'SOS', 'Bot']

fechas = ['2022-10-03', '2022-10-04', '2022-10-05', '2022-10-06', '2022-10-07', '2022-10-08', '2022-10-09']


azure = AzureDB(server, database, username, password, driver)

for x in range(1000):
    random_fecha = random.choices(fechas, weights=[0.18, 0.2, 0.25, 0.15, 0.15, 0.05, 0.02])
    random_pagina = random.choices(paginas, weights=[0.25, 0.1, 0.08, 0.1, 0.2, 0.02, 0.05, 0.15, 0.05])
    random_hora = random.choices([x for x in range(0, 24)], weights=[0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.1, 0.1, 
                                                 0.1, 0.03, 0.04, 0.05, 0.01, 0.01, 0.1, 0.1, 0.01, 0.1, 
                                                 0.06, 0.05, 0.04, 0.1, 0.01])
    random_minuto = random.choice(['00', '01', '02', '03', '04', '05', '06', '07', '08', '09'] + [x for x in range(10, 60)])
    random_segundo = random.choice(['00', '01', '02', '03', '04', '05', '06', '07', '08', '09'] + [x for x in range(10, 60)])
    
    azure.insert_query(f"INSERT INTO Paginas (pagina, fecha) VALUES ('{random_pagina[0]}', '{random_fecha[0]} {random_hora[0]}:{random_minuto}:{random_segundo}')")
    
    print(random_fecha[0], random_pagina[0], random_hora[0], random_minuto, random_segundo)
