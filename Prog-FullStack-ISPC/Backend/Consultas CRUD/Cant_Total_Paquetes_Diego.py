import pymysql

try:
    connection=pymysql.connect(host='localhost',database='frontline_bdd',user='root',password='root')

    query_paquete = 'select servicio_cod, count(cod_paquete) as cant_total_paquetes from paquetes group by servicio_cod'

    cursor=connection.cursor()
    cursor.execute(query_paquete)
    Paquetes_cant=cursor.fetchall()
    for Paquete in Paquetes_cant:
        print(Paquete)
    cursor.close()

except (pymysql.err.OperationalError, pymysql.err.InternalError) as error:
    print(f'Mediante la conexión con MySQL ocurrió este error: {error}')

finally:
    if connection.open:
        connection.close()
        print("MySQL: conexión completada exitosamente")