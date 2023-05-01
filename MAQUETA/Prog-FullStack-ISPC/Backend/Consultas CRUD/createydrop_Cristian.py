import pymysql

try:
    connection = pymysql.connect(host='localhost',
                                         database='frontline_bdd',
                                         user='root',
                                         password='root')

    mySql_DROP_query = "ALTER TABLE Factura DROP CONSTRAINT factura_ibfk_1;"

    cursor = connection.cursor()
    cursor.execute(mySql_DROP_query)
    connection.commit()
    print("Constraint borrada") 
    

except (pymysql.err.OperationalError,pymysql.err.InternalError) as error:
    print(f"Failed to delete constraint {error}")

try:
    mySql_DROP_query = "DROP TABLE Clientes"

    cursor = connection.cursor()
    cursor.execute(mySql_DROP_query)
    connection.commit()
    print("tabla borrada") 
    

except (pymysql.err.OperationalError,pymysql.err.InternalError) as error:
    print(f"Failed to delete table {error}")

try:

    mySql_Create_Table_Query= """CREATE TABLE if not exists clientes     ( 
                             id_cliente bigint NOT NULL,
                             nombre_cliente varchar(50) NOT NULL,
                             direccion_cliente varchar(255)NOT NULL,
                             tel_cliente bigint NOT NULL,
                             email_cliente varchar(50),
                             constraint pk_idcl primary key(id_cliente));
                              """
                              
    cursor.execute(mySql_Create_Table_Query)
    connection.commit()
    print( "tabla creada")

except (pymysql.err.OperationalError,pymysql.err.InternalError) as error:
    print(f"Failed to create table in MySQL: {error}")
try:
    mySql_DROP_query = "ALTER TABLE Factura ADD FOREIGN KEY(cliente_id) REFERENCES Clientes(id_cliente);"

    cursor = connection.cursor()
    cursor.execute(mySql_DROP_query)
    connection.commit()
    print("Constraint agregada") 
    

except (pymysql.err.OperationalError,pymysql.err.InternalError) as error:
    print(f"Failed to delete table {error}")

finally:
    if connection.open:
        connection.close()
        print("MySQL connection is closed")
