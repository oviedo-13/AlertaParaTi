from ConnectionInfoAzure import server, database, username, password, driver
from dataSyncronizationAzureOracle import AzureDB
import datetime
import pytz
import requests
import json

azure = AzureDB(server, 
                database,
                username,
                password,
                driver)


mexico_timezone = pytz.timezone('America/Mexico_City')
mexico_datetime = datetime.datetime.now(mexico_timezone).strftime('%Y-%m-%d %H:%M:%S')
mexico_date = datetime.datetime.now(mexico_timezone).date()
start_date = f'{mexico_date}'
end_date = f'{mexico_date}'


# def obtener_clima():
    
#     weather_api_url = f"""https://api.open-meteo.com/v1/forecast?latitude=19.60&longitude=-99.22&hourly=temperature_2m,rain&timezone=auto&start_date={start_date}&end_date={end_date}"""

#     weather_response = requests.request("GET", weather_api_url)

#     weather_response_data = json.loads(weather_response.text)['hourly']
#     weather_response_time = weather_response_data['time']
#     weather_response_temperature = weather_response_data['temperature_2m']
#     weather_response_rain = weather_response_data['rain']


#     air_quality_api_url = f"""https://air-quality-api.open-meteo.com/v1/air-quality?latitude=19.60&longitude=-99.22&hourly=carbon_monoxide,uv_index&domains=cams_global&timezone=auto&start_date={start_date}&end_date={end_date}"""
#     air_quality_response = requests.request("GET", air_quality_api_url)
#     air_quality_response_data = json.loads(air_quality_response.text)['hourly']
#     air_quality_response_time = air_quality_response_data['time']
#     air_quality_response_carbon_monoxide = air_quality_response_data['carbon_monoxide']
#     air_quality_response_uv_index = air_quality_response_data['uv_index']


#     for i in range(len(air_quality_response_time)):
#         try:
#             azure.insert_query(f"""INSERT INTO clima VALUES ({weather_response_temperature[i]}, {weather_response_rain[i]}, {air_quality_response_uv_index[i]}, {air_quality_response_carbon_monoxide[i]}, '{air_quality_response_time[i].replace('T', ' ')}')""")
#         except:
#             azure.insert_query(f"""UPDATE clima SET temperatura = {weather_response_temperature[i]}, porcentaje_lluvia = {weather_response_rain[i]}, indice_uv = {air_quality_response_uv_index[i]}, calidad_aire = {air_quality_response_carbon_monoxide[i]} WHERE fecha = '{air_quality_response_time[i].replace('T', ' ')}'""")
      

def obtener_sismo():
# the current date - 7 days
    start_date_sismo = mexico_date - datetime.timedelta(days=1825)
    sismo_api_url = f"""https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime={start_date_sismo}&endtime={end_date}&latitude=19.60&longitude=-99.22&maxradiuskm=1000&minmagnitude=5&orderby=time"""
    sismo_response = requests.request("GET", sismo_api_url)
    sismo_response_data = json.loads(sismo_response.text)['features']
    for i in range(len(sismo_response_data)):
        # obtener id
        sismo_response_data_id = sismo_response_data[i]['id']
        # obtener magnitud
        sismo_response_data_magnitude = sismo_response_data[i]['properties']['mag']
        # conveirtiendo la fecha a formato datetime desde epoch
        sismo_response_data_fecha = datetime.datetime.fromtimestamp(sismo_response_data[i]['properties']['time']/1000).strftime('%Y-%m-%d %H:%M:%S')
        sismo_response_data_update_fecha = datetime.datetime.fromtimestamp(sismo_response_data[i]['properties']['updated']/1000).strftime('%Y-%m-%d %H:%M:%S')
        
        sismo_response_data_lugar = sismo_response_data[i]['properties']['place']
        sismo_response_data_longitud = sismo_response_data[i]['geometry']['coordinates'][0]
        sismo_response_data_latitud = sismo_response_data[i]['geometry']['coordinates'][1]
        
        
        # insertar, si ya existe, actualizar
        try:
            azure.insert_query(f"""INSERT INTO sismo (id, ubicacion, magnitud, longitud, latitud, fecha_actualizacion, fecha) 
                            VALUES (
                                    '{sismo_response_data_id}', 
                                    '{sismo_response_data_lugar}',
                                    {sismo_response_data_magnitude}, 
                                    {sismo_response_data_longitud},
                                    {sismo_response_data_latitud},
                                    '{sismo_response_data_update_fecha}',
                                    '{sismo_response_data_fecha}'
                                    )""")
            print('insertado')
            
        except Exception as e:
            azure.insert_query(f"""UPDATE sismo SET ubicacion = '{sismo_response_data_lugar}',
                                        magnitud = {sismo_response_data_magnitude},
                                        longitud = {sismo_response_data_longitud},
                                        latitud = {sismo_response_data_latitud},
                                        fecha_actualizacion = '{sismo_response_data_update_fecha}',
                                        fecha = '{sismo_response_data_fecha}'
                                    WHERE id = '{sismo_response_data_id}'""")
            print('actualizado')


def obtener_incidente():
    incidente_api_url = """https://api.tomtom.com/traffic/services/5/incidentDetails?key=Vb6ondp3xGc8STqcndUjrqJcoeKIPMxg&bbox=-99.336542,19.522352,-99.213403,19.613057&fields={incidents{type,geometry{type,coordinates},properties{id,iconCategory,lastReportTime,startTime,endTime,from,to,length}}}&language=en-GB&t=1111&timeValidityFilter=present&categoryFilter=1,2,3,4,6,8,9,11,14"""
    incidente_response = requests.request("GET", incidente_api_url)
    incidente_response_data = json.loads(incidente_response.text)['incidents']
    
    for i in range(len(incidente_response_data)):
        incidente_response_data_id = incidente_response_data[i]['properties']['id']
        print(incidente_response_data_id)
        # el tipo de accidente
        incidente_response_data_tipo = incidente_response_data[i]['properties']['iconCategory']
        # convertir de utc a mexico time zone
        incidente_response_data_tiempo_inicio = mexico_timezone.normalize(datetime.datetime.strptime((incidente_response_data[i]['properties']['startTime'].replace('T', ' ')).replace('Z', ''), '%Y-%m-%d %H:%M:%S').replace(tzinfo=pytz.utc).astimezone(mexico_timezone)).strftime('%Y-%m-%d %H:%M:%S')
        # el tiempo puede regresar null entonces si no es null, regresa el tiempo con time zone de mexico
        if incidente_response_data[i]['properties']['endTime'] == None:
            incidente_response_data_tiempo_fin = None
        else:
            incidente_response_data_tiempo_fin = mexico_timezone.normalize(datetime.datetime.strptime((incidente_response_data[i]['properties']['endTime'].replace('T', ' ')).replace('Z', ''), '%Y-%m-%d %H:%M:%S').replace(tzinfo=pytz.utc).astimezone(mexico_timezone)).strftime('%Y-%m-%d %H:%M:%S')
        incidente_response_data_desde_lugar = incidente_response_data[i]['properties']['from']
        incidente_response_data_hasta_lugar = incidente_response_data[i]['properties']['to']
        incidente_response_data_longitud = incidente_response_data[i]['properties']['length']
        
        incidente_response_data_coordenadas = incidente_response_data[i]['geometry']['coordinates']
        
        # obtener las primeras y ultimas coordenadas de la base de datos antes que se actualicen
        try:
            longitud_anterior = azure.return_select(f"""SELECT longitud_metros FROM incidentes WHERE id = '{incidente_response_data_id}'""")[0][0]
        except:
            longitud_anterior = 0
        try:
            primera_coordenada_latitud = azure.return_select(f"""SELECT TOP 1 latitud FROM incidentes_coordenadas WHERE id_incidente = '{incidente_response_data_id}' ORDER BY id ASC""")[0][0]
        except:
            primera_coordenada_latitud = 0
        try:
            primera_coordenada_longitud = azure.return_select(f"""SELECT TOP 1 longitud FROM incidentes_coordenadas WHERE id_incidente = '{incidente_response_data_id}' ORDER BY id ASC""")[0][0]
        except:
            primera_coordenada_longitud = 0
        try:
            ultima_coordenada_latitud = azure.return_select(f"""SELECT TOP 1 latitud FROM incidentes_coordenadas WHERE id_incidente = '{incidente_response_data_id}' ORDER BY id DESC""")[0][0]
        except:
            ultima_coordenada_longitud = 0
        try:
            ultima_coordenada_longitud = azure.return_select(f"""SELECT TOP 1 longitud FROM incidentes_coordenadas WHERE id_incidente = '{incidente_response_data_id}' ORDER BY id DESC""")[0][0]
        except:
            ultima_coordenada_longitud = 0
        try:
            cantidad_coordenadas = azure.return_select(f"""SELECT COUNT(*) FROM incidentes_coordenadas WHERE id_incidente = '{incidente_response_data_id}'""")[0][0]
        except:
            cantidad_coordenadas = 0
            
        # obtener las primeras y ultimas coordenadas de la ultima llamada
        primera_coordenada_latitud_datos = incidente_response_data_coordenadas[0][1]
        primera_coordenada_longitud_datos = incidente_response_data_coordenadas[0][0]
        ultima_coordenada_latitud_datos = incidente_response_data_coordenadas[-1][1]
        ultima_coorednada_longitud_datos = incidente_response_data_coordenadas[-1][0]
        
        if (incidente_response_data_tipo != 6):
            try:
                azure.insert_query(f"""INSERT INTO incidentes (id, tipo_id, tiempo_inicio, tiempo_final, desde_lugar, hasta_lugar, longitud_metros) 
                                VALUES (
                                        '{incidente_response_data_id}',
                                            {incidente_response_data_tipo},
                                            '{incidente_response_data_tiempo_inicio}',
                                            {f"'{incidente_response_data_tiempo_fin}'" if incidente_response_data_tiempo_fin != None else 'NULL'},
                                            '{incidente_response_data_desde_lugar}',
                                            '{incidente_response_data_hasta_lugar}',
                                            {incidente_response_data_longitud})""")
                print('insertado')
            except Exception as e:
                azure.insert_query(f"""UPDATE incidentes SET tipo_id = '{incidente_response_data_tipo}',
                                            tiempo_inicio = '{incidente_response_data_tiempo_inicio}',
                                            tiempo_final = {f"'{incidente_response_data_tiempo_fin}'" if incidente_response_data_tiempo_fin != None else 'NULL'},
                                            desde_lugar = '{incidente_response_data_desde_lugar}',
                                            hasta_lugar = '{incidente_response_data_hasta_lugar}',
                                            longitud_metros = {incidente_response_data_longitud}
                                        WHERE id = '{incidente_response_data_id}'""")
                print('actualizado')
            
            # si las ultimas coordenadas son diferentes a las coordenadas de la base de datos,
            # si la longitud cambia o si la cantidad de coordenadas es diferente
            # entonces se borran y se vuelven a insertan
            if longitud_anterior != incidente_response_data_longitud \
                    or primera_coordenada_latitud != primera_coordenada_latitud_datos \
                    or primera_coordenada_longitud != primera_coordenada_longitud_datos \
                    or ultima_coordenada_latitud != ultima_coordenada_latitud_datos \
                    or ultima_coorednada_longitud_datos != ultima_coordenada_longitud \
                    or cantidad_coordenadas != len(incidente_response_data_coordenadas):
                azure.insert_query(f"""DELETE FROM incidentes_coordenadas WHERE id_incidente = '{incidente_response_data_id}'""")
                print('borrado')
                for j in range(len(incidente_response_data_coordenadas)):
                    incidente_response_data_coordenadas_latitud = incidente_response_data_coordenadas[j][1]
                    incidente_response_data_coordenadas_longitud = incidente_response_data_coordenadas[j][0]
                    
                        
                    azure.insert_query(f"""INSERT INTO incidentes_coordenadas (id_incidente, latitud, longitud, fecha_actualizacion) 
                                        VALUES (
                                                '{incidente_response_data_id}',
                                                    {incidente_response_data_coordenadas_latitud},
                                                    {incidente_response_data_coordenadas_longitud},
                                                    '{mexico_datetime}')""")
                    print('coordenada insertada')
            else:
                print('no hubo cambios de coordenadas')

                
            
obtener_sismo()
# print(f'weather_response_time: {weather_response_time}\n')
# print(f'weather_response_temperature: {weather_response_temperature}\n')
# print(f'weather_response_rain: {weather_response_rain}\n')    