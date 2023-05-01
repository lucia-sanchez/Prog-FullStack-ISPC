import pymysql

try:
    connection = pymysql.connect(host='localhost',
                                         user='root',
                                         password='root',
                                         database='frontline_bdd')
    

    mySql_query = "select * from paquetes where peso<=10;"
 

    cursor = connection.cursor()
    cursor.execute(mySql_query)
   
    rows=cursor.fetchall()
    for dato in rows:
        print(dato)
    cursor.close()

except (pymysql.err.OperationalError, pymysql.err.InternalError) as error:
    print(f"Failed to connect to the database{error}")

finally:
    if connection.open:
        connection.close()
        print("MySQL connection is closed")
