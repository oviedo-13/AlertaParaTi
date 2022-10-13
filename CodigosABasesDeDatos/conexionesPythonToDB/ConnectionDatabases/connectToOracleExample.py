import ConnectionInfoOracle
import cx_Oracle

print('connecting...')
conn = cx_Oracle.connect(ConnectionInfoOracle.usernm, ConnectionInfoOracle.psswd, ConnectionInfoOracle.dsn)
print('connected')

c = conn.cursor()
c.execute('Select * from WKSP_ALERTAPARATIATIZAPAN.TEST')
rows = c.fetchall()
for row in rows:
    print(row)