import pymysql

try:
    connection=pymysql.connect(host='localhost',database='frontline_bdd',user='root',password='root')

    query = 'select precio_kg_km from servicios'

    cursor=connection.cursor()
    cursor.execute(query)
    rows=cursor.fetchall()
    for r in rows:
        print(r)
    cursor.close()

except (pymysql.err.OperationalError, pymysql.err.InternalError) as error:
    print(f'Al tratar de conectarse con MySQL ocurrió este error: {error}')

finally:
    if connection.open:
        connection.close()
        print("MySQL se cerró exitosamente")