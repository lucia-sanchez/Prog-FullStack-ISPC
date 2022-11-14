import pymysql

try:
    connection = pymysql.connect(host='localhost',
                                user='root',
                                password='root',
                                database='frontline_bdd')

    query = """ALTER TABLE Factura
            ADD estadoPago boolean;"""
 

    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    print("Actualizado correctamente")
    cursor.close()
   
except (pymysql.err.OperationalError, pymysql.err.InternalError) as error:
    print(f"Fallo al tratar de ingresar la columna por el siguiente error: {error}")

finally:
    if connection.open:
        connection.close()
        print("La conexión con MySQL ah concluido exitosamente")