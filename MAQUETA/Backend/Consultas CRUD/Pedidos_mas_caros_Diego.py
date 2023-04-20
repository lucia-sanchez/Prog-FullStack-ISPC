import pymysql

try:
    connection=pymysql.connect(host='localhost',database='frontline_bdd',user='root',password='root')

    query_pedido = 'select cod_pedido, max(precio_pedido) as precio_max from pedidos group by cod_pedido order by precio_max desc'

    cursor=connection.cursor()
    cursor.execute(query_pedido)
    Pedidos_max=cursor.fetchall()
    for Pedido in Pedidos_max:
        print(Pedido)
    cursor.close()

except (pymysql.err.OperationalError, pymysql.err.InternalError) as error:
    print(f'Mediante la conexión con MySQL ocurrió este error: {error}')

finally:
    if connection.open:
        connection.close()
        print("MySQL: conexión completada exitosamente")