import pymysql

try:
    connection=pymysql.connect(host='localhost',database='frontline_bdd',user='root',password='root')

query_update_horario = "UPDATE administrador SET horarios_admn= '08:00 a 14:00' WHERE id_administrador = '2'; "
        

       cursor = connection.cursor()
       cursor.execute(query_update_horario)
       connection.commit()
       print(cursor.rowcount, "registro(s) actualizado")

except mysql.connector.Error as error:
    print("Error al actualizar los datos {}".format(error))

finally:
    if connection.open:
        connection.close()
        print("MySQL: conexión completada exitosamente")
