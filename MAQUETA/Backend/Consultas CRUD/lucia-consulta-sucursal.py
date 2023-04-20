import pymysql

try:
    connection=pymysql.connect(host='localhost',database='frontline_bdd',user='root',password='root')

query_sucursal = "select * from sucursal;"

    cursor=connection.cursor()
    cursor.execute(query_sucursal)
    Sucursal=cursor.fetchall()
    for Sucursal in Sucursales:
        print(Sucursal)

except (pymysql.err.OperationalError, pymysql.err.InternalError) as error:
    print(f"Error al conectarse a la base de datos{error}")
    

finally:
    if connection.open:
        connection.close()
        print("MySQL: conexión completada exitosamente"))
