import pymysql

try:
    connection=pymysql.connect(host='localhost',database='frontline_bdd',user='root',password='root')

    query_factura = 'select emisor, avg(precio_total) as prom_precio_total from factura group by emisor'

    cursor=connection.cursor()
    cursor.execute(query_factura)
    Promedios=cursor.fetchall()
    for Promedio in Promedios:
        print(Promedio)
    cursor.close()

except (pymysql.err.OperationalError, pymysql.err.InternalError) as error:
    print(f'Mediante la conexión con MySQL ocurrió este error: {error}')

finally:
    if connection.open:
        connection.close()
        print("MySQL: conexión completada exitosamente")