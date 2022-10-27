<<<<<<< HEAD
'''
Sube los CSV a la base de datos
Fecha: 27-10-2022
'''

import sys
import getopt
import pymysql
import csv
from os import listdir
from os.path import isfile, isdir, splitext
import pandas as pd
from datetime import datetime
import chardet    


def main(argv):
    host = argv[0]
    user = argv[1]
    psw = argv[2]
    datab = argv[3]

    #print(host, user, psw, datab)

    print('Comenzando la Carga de los archivos')

    '''Producto'''
    ruta_csv = '../csv/'

    # Abrimos el archivo csv de productos
    df = pd.read_csv(ruta_csv + 'producto.csv')

    # Abrimos la conexión
    db = pymysql.connect(host=host, user=user, passwd=psw, db=datab)
    cur = db.cursor()

    cur.execute('SET FOREIGN_KEY_CHECKS = 0')
    db.commit()    

    # Insertamos los registros
    hasta = len(df)
    for i in range(hasta):
        idProducto = df['id'][i]
        marca = df['marca'][i]
        nombre = df['nombre'][i]
        presentacion = df['presentacion'][i]
        # Query
        qry = 'INSERT INTO producto \
            (IdProducto, marca, nombre, presentacion) \
                VALUES (%s, %s, %s, %s);'
        cur.execute(qry,(idProducto, marca, nombre, presentacion))
        db.commit()
        try:
            db.rollback()
        except:
            print('Error al enviar los datos')
    
    cur.execute('SET FOREIGN_KEY_CHECKS = 1')
    db.commit()  

    # Cerramos la conexión
    cur.close()
    db.close()


    '''Sucursal'''
    # Abrimos el archivo csv de sucursal
    df = pd.read_csv(ruta_csv + 'sucursal.csv')    

    # Abrimos la conexión
    db = pymysql.connect(host=host, user=user, passwd=psw, db=datab)
    cur = db.cursor()

    cur.execute('SET FOREIGN_KEY_CHECKS = 0')
    db.commit()  

    # Insertamos los registros
    hasta = len(df)
    for i in range(hasta):
        idSucursal = df['id'][i]
        idComercio = df['comercioId'][i]
        idBandera = df['banderaId'][i]
        banderaDesc = df['banderaDescripcion'][i]
        comercioRazonSocial = df['comercioRazonSocial'][i]
        provincia = df['provincia'][i]
        localidad = df['localidad'][i]
        direccion = df['direccion'][i]
        lat = df['lat'][i]
        lng = df['lng'][i]
        sucursalNombre = df['sucursalNombre'][i]
        sucursalTipo = df['sucursalTipo'][i]
        # Query
        qry = 'INSERT INTO sucursal \
            (IdSucursal, IdComercio, IdBandera, BanderaDesc, ComercioRazonSocial, \
                Provincia, Localidad, Domicilio, Latitud, Longitud, SucursalNombre, SucursalTipo) \
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);'
        cur.execute(qry,(idSucursal, idComercio, idBandera, banderaDesc, comercioRazonSocial, \
                        provincia, localidad, direccion, lat, lng, sucursalNombre, sucursalTipo))
        db.commit()
        try:
            db.rollback()
        except:
            print('Error al enviar los datos')
    
    cur.execute('SET FOREIGN_KEY_CHECKS = 1')
    db.commit()  

    # Cerramos la conexión
    cur.close()
    db.close()
    
    '''Operacion'''
    ruta_csv = '../csv/'    

    archs_csv = listdir(ruta_csv)

    archs_csv.remove('producto.csv')
    archs_csv.remove('sucursal.csv')

    # Abrimos la conexión
    db = pymysql.connect(host=host, user=user, passwd=psw, db=datab)
    cur = db.cursor()

    cur.execute('SET FOREIGN_KEY_CHECKS = 0')
    db.commit()  

    for arch in archs_csv:
        df = pd.read_csv(ruta_csv + arch, dtype={'producto_id':'str', 'sucursal_id':'str', 'precio':'float'})


        # Insertamos los registros
        hasta = len(df)
        for i in range(hasta):
            idProducto = df['producto_id'][i]
            idSucursal = df['sucursal_id'][i]
            precio = df['precio'][i]
            fecha = df['fecha'][i]
            outlier = 0
            #print(type(fecha))
            # Query
            qry = 'INSERT INTO operacion \
                (IdProducto, IdSucursal, precio, fecha, outlier) \
                    VALUES (%s, %s, %s, %s, %s);'
            cur.execute(qry, (idProducto, idSucursal, precio, fecha, outlier)) 
            db.commit()
            try:
                db.rollback()
            except:
                print('Error al enviar los datos')

    cur.execute('SET FOREIGN_KEY_CHECKS = 1')
    db.commit()         

    # Cerramos la conexión
    cur.close()
    db.close()

    print('La carga de los archivos a finalizado')


if __name__ == '__main__':
    main(sys.argv[1: ])

=======
'''
Sube los CSV a la base de datos
Fecha: 27-10-2022
'''

import sys
import getopt
import pymysql
import csv
from os import listdir
from os.path import isfile, isdir, splitext
import pandas as pd
from datetime import datetime
import chardet    


def main(argv):
    host = argv[0]
    user = argv[1]
    psw = argv[2]
    datab = argv[3]

    #print(host, user, psw, datab)

    print('Comenzando la Carga de los archivos')

    '''Producto'''
    ruta_csv = '../csv/'

    # Abrimos el archivo csv de productos
    df = pd.read_csv(ruta_csv + 'producto.csv')

    # Abrimos la conexión
    db = pymysql.connect(host=host, user=user, passwd=psw, db=datab)
    cur = db.cursor()

    cur.execute('SET FOREIGN_KEY_CHECKS = 0')
    db.commit()    

    # Insertamos los registros
    hasta = len(df)
    for i in range(hasta):
        idProducto = df['id'][i]
        marca = df['marca'][i]
        nombre = df['nombre'][i]
        presentacion = df['presentacion'][i]
        # Query
        qry = 'INSERT INTO producto \
            (IdProducto, marca, nombre, presentacion) \
                VALUES (%s, %s, %s, %s);'
        cur.execute(qry,(idProducto, marca, nombre, presentacion))
        db.commit()
        try:
            db.rollback()
        except:
            print('Error al enviar los datos')
    
    cur.execute('SET FOREIGN_KEY_CHECKS = 1')
    db.commit()  

    # Cerramos la conexión
    cur.close()
    db.close()


    '''Sucursal'''
    # Abrimos el archivo csv de sucursal
    df = pd.read_csv(ruta_csv + 'sucursal.csv')    

    # Abrimos la conexión
    db = pymysql.connect(host=host, user=user, passwd=psw, db=datab)
    cur = db.cursor()

    cur.execute('SET FOREIGN_KEY_CHECKS = 0')
    db.commit()  

    # Insertamos los registros
    hasta = len(df)
    for i in range(hasta):
        idSucursal = df['id'][i]
        idComercio = df['comercioId'][i]
        idBandera = df['banderaId'][i]
        banderaDesc = df['banderaDescripcion'][i]
        comercioRazonSocial = df['comercioRazonSocial'][i]
        provincia = df['provincia'][i]
        localidad = df['localidad'][i]
        direccion = df['direccion'][i]
        lat = df['lat'][i]
        lng = df['lng'][i]
        sucursalNombre = df['sucursalNombre'][i]
        sucursalTipo = df['sucursalTipo'][i]
        # Query
        qry = 'INSERT INTO sucursal \
            (IdSucursal, IdComercio, IdBandera, BanderaDesc, ComercioRazonSocial, \
                Provincia, Localidad, Domicilio, Latitud, Longitud, SucursalNombre, SucursalTipo) \
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);'
        cur.execute(qry,(idSucursal, idComercio, idBandera, banderaDesc, comercioRazonSocial, \
                        provincia, localidad, direccion, lat, lng, sucursalNombre, sucursalTipo))
        db.commit()
        try:
            db.rollback()
        except:
            print('Error al enviar los datos')
    
    cur.execute('SET FOREIGN_KEY_CHECKS = 1')
    db.commit()  

    # Cerramos la conexión
    cur.close()
    db.close()
    
    '''Operacion'''
    ruta_csv = '../csv/'    

    archs_csv = listdir(ruta_csv)

    archs_csv.remove('producto.csv')
    archs_csv.remove('sucursal.csv')

    # Abrimos la conexión
    db = pymysql.connect(host=host, user=user, passwd=psw, db=datab)
    cur = db.cursor()

    cur.execute('SET FOREIGN_KEY_CHECKS = 0')
    db.commit()  

    for arch in archs_csv:
        df = pd.read_csv(ruta_csv + arch, dtype={'producto_id':'str', 'sucursal_id':'str', 'precio':'float'})


        # Insertamos los registros
        hasta = len(df)
        for i in range(hasta):
            idProducto = df['producto_id'][i]
            idSucursal = df['sucursal_id'][i]
            precio = df['precio'][i]
            fecha = df['fecha'][i]
            outlier = 0
            #print(type(fecha))
            # Query
            qry = 'INSERT INTO operacion \
                (IdProducto, IdSucursal, precio, fecha, outlier) \
                    VALUES (%s, %s, %s, %s, %s);'
            cur.execute(qry, (idProducto, idSucursal, precio, fecha, outlier)) 
            db.commit()
            try:
                db.rollback()
            except:
                print('Error al enviar los datos')

    cur.execute('SET FOREIGN_KEY_CHECKS = 1')
    db.commit()         

    # Cerramos la conexión
    cur.close()
    db.close()

    print('La carga de los archivos a finalizado')


if __name__ == '__main__':
    main(sys.argv[1: ])

>>>>>>> f51e15f9726ac2d6b8ef3596280b1aecd6ae9edf
