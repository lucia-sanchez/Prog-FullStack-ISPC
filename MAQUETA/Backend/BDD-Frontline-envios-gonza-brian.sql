create database frontline_bdd
use frontline_bdd;

-- Tabla Clientes
create table Clientes(
id_cliente bigint NOT NULL,
nombre_cliente varchar(50) NOT NULL,
direccion_cliente varchar(255) NOT NULL,
tel_cliente bigint NOT NULL,
email_cliente varchar(50),
constraint pk_idcl primary key(id_cliente))

-- Tabla Destino
create table Destino(
cod_postal int NOT NULL,
destinatario varchar(50) NOT NULL,
constraint pk_cp primary key(cod_postal))

-- Tabla Sucursal
create table Sucursal(
id_sucursal bigint NOT NULL,
postal_cod int NOT NULL,
constraint pk_idsuc primary key(id_sucursal),
constraint fk_cp2 foreign key(postal_cod) references Destino(cod_postal))

-- Tabla Servicios
create table Servicios(
cod_servicio varchar(1),
nombre_servicio varchar(50) NOT NULL,
descripcion_serv varchar(400) NOT NULL,
precio_kg_km float NOT NULL,
constraint pk_servcod primary key(cod_servicio))

-- Tabla Transportista
create table Transportista(
id_transportista bigint NOT NULL,
sucursal bigint NOT NULL,
nombre_transp varchar(50) NOT NULL,
email_transp varchar(50) NOT NULL,
horarios_transp varchar(50),
tel_transp bigint UNIQUE,
constraint pk_transpid primary key(id_transportista),
constraint fk_idsuc2 foreign key(sucursal) references Sucursal(id_sucursal))

-- Tabla Administrativo
create table Administrativo(
id_administrador bigint NOT NULL,
sucursal bigint NOT NULL,
nombre_admin varchar(50) NOT NULL,
email_admin varchar(50) NOT NULL,
horarios_admin varchar(50),
tel_admin bigint UNIQUE,
constraint pk_adminid primary key(id_administrador),
constraint fk_idsuc1 foreign key(sucursal) references Sucursal(id_sucursal))

-- Tabla Factura
create table Factura(
cod_factura bigint NOT NULL auto_increment,
cliente_id bigint NOT NULL,
emisor bigint NOT NULL,
precio_total float NOT NULL,
constraint pk_codfac primary key(cod_factura),
constraint fk_idc foreign key(cliente_id) references Clientes(id_cliente),
constraint fk_emisor foreign key(emisor) references Administrativo(id_administrador))

-- Tabla Pedidos
create table Pedidos(
cod_pedido bigint NOT NULL auto_increment,
postal_cod int NOT NULL,
factura_cod bigint NOT NULL,
precio_pedido  float NOT NULL,
ubicacion_pedido char(255) NOT NULL,
constraint pk_codpd primary key(cod_pedido),
constraint fk_cp1 foreign key(postal_cod) references Destino(cod_postal),
constraint fk_codfac1 foreign key(factura_cod) references Factura(cod_factura))

-- Tabla Paquetes
create table Paquetes(
cod_paquete bigint NOT NULL auto_increment,
pedido_cod  bigint NOT NULL,
servicio_cod varchar(1),
contenido varchar(255) NOT NULL,
peso float NOT NULL,
altura float NOT NULL,
ancho float NOT NULL,
largo float NOT NULL,
precio_paquete float NOT NULL,
constraint pk_paqcod primary key(cod_paquete),
constraint fk_codpd1 foreign key(pedido_cod) references Pedidos(cod_pedido),
constraint fk_servcod1 foreign key(servicio_cod) references Servicios(cod_servicio)
)

-- Tabla Vehículos
create table Vehiculos(
patente varchar(8) NOT NULL,
modelo_vehiculo varchar(50) NOT NULL,
ano_vehiculo int NOT NULL,
constraint pk_vehi primary key(patente))

-- Tabla Paquete/Vehiculo
create table Paquete_Vehiculo(
cod_paquete bigint NOT NULL,
patente varchar(8) NOT NULL,
constraint fk_paqcod2 foreign key(cod_paquete) references Paquetes(cod_paquete),
constraint fk_vehi2 foreign key(patente) references Vehiculos(patente))

-- Tabla Vehiculo/Conductor

create table Vehiculo_Conductor(
patente varchar(8) NOT NULL,
transp_id bigint NOT NULL,
constraint fk_vehi1 foreign key(patente) references Vehiculos(patente),
constraint fk_traspid foreign key(transp_id) references Transportista(id_transportista))


