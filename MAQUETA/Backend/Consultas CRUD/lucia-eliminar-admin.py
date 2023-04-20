import pymysql

try:
    connection=pymysql.connect(host='localhost',database='frontline_bdd',user='root',password='root')

query_delete_admin = "DELETE from administrador WHERE id_administrador = '2';"


       cursor = connection.cursor()
       cursor.execute(query_delete_admin)
       connection.commit()
       print(cursor.rowcount, "registro(s) borrado") 
       
    

except (pymysql.err.OperationalError, pymysql.err.InternalError) as error:
    print(f"Error al eliminar administrador en la base de datos{error}")
    
    cursor.close()
    connection.close()
