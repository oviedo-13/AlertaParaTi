
# AlertaParaTi

El objetivo de este proyecto es desarrollar una aplicación que ayude a facilitar y mejorar la comunicación entre el Gobierno de Atizapán y los ciudadanos.

AlertaParaTi es el nombre de la aplicación móvil que desarrollamos para el gobierno de Atizapán de Zaragoza. 

En el repositorio podrán encontrar todos los archivos que generamos para el proyecto.



## Tabla de contenido

- [Aplicación Móvil](/AplicaciónMovil).
- [Codigos de las Bases de Datos](/CodigosABasesDeDatos).
- [Daigrama Entidad Relación](/DiagramaEntidadRelaciónAlertaParati.pdf).
- [Diagrama de Casos de Uso](/DiagramaCasosDeUso.png).
- [Pagina Web](/PaginaWeb.txt).

## Tech Stack
**Aplicación Móvil:** Android Studio

**Aplicación Web:** Oracle APEX

**Base de Datos:** Azure SQL

**Data Warehouse:** Oracle Autonomous

**App Service:** Azure


## Referencia a las API 

### Clima
Página web [Open-Meteo](https://open-meteo.com/en)

Llamada [API clima](https://api.open-meteo.com/v1/forecast?latitude=19.56&longitude=-99.18&hourly=temperature_2m,rain)

Llamada [API calidad del aire](https://air-quality-api.open-meteo.com/v1/air-quality?latitude=19.56&longitude=-99.18&hourly=carbon_monoxide,uv_index&timezone=auto)


### Sismos
Página web [USGS](https://earthquake.usgs.gov/fdsnws/event/1/)

Llamada [API sismos](https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2022-09-01&endtime=2022-10-01&latitude=19.5944359&longitude=-99.2257701&maxradiuskm=1000&minmagnitude=5&orderby=time)

### Tráfico
Página web [TomTom maps](https://developer.tomtom.com/)

Llamada [API incidentes](https://api.tomtom.com/traffic/services/5/incidentDetails?key=Vb6ondp3xGc8STqcndUjrqJcoeKIPMxg&bbox=-99.336542,19.522352,-99.213403,19.613057&fields={incidents{type,geometry{type,coordinates},properties{id,iconCategory,startTime,endTime,from,to}}}&language=en-GB&t=1111&timeValidityFilter=present&categoryFilter=1,2,3,4,6,8,9,11,14)


## Autores

- Erika García [@A01745158](https://github.com/A01745158)
- Gala Flores [@galaflores](https://github.com/galaflores)
- Yunoe Sierra [@YunoeSd](https://github.com/YunoeSd)
- Rodrigo Mendoza [@RodrigoMendoza2000](https://github.com/RodrigoMendoza2000)
- Antonio Oviedo [@oviedo-13](https://github.com/oviedo-13)
- Alan Said [@AlanSaid1](https://github.com/AlanSaid1)


