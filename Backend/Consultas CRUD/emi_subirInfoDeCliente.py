import pymysql

try:
    connection = pymysql.connect(host='localhost',
                                user='root',
                                password='root',
                                database='frontline_bdd')

    query = """INSERT INTO clientes (id_cliente, nombre_cliente, direccion_cliente, tel_cliente, email_cliente) 
            VALUES 
            (13690420, 'Ricardo Ford', 'Córdoba 1500, Córdoba', 08003334444, 'email@ejemplo.com') """
 

    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    print("Datos ingrsados correctamente")
    cursor.close()
   
except (pymysql.err.OperationalError, pymysql.err.InternalError) as error:
    print(f"Fallo al tratar de ingresar los datos por el siguiente error: {error}")

finally:
    if connection.open:
        connection.close()
        print("La conexión con MySQL ah concluido exitosamente")