<<<<<<< HEAD
'''
Módulo de funciones generales
'''

from datetime import datetime


# Cambiar / por -
def cambiarFecha(valor):
    '''
    Corrige los ID consideardos fechas
    valor -> date
    '''
    if type(valor) == datetime:
        valor = str(valor).strip()
        valor = valor[ :valor.find(' ')]
        e1, e2, e3 = valor.split('-')
        if e2[0] == '0':
            e2 = e2[1:]
        if e3[0] == '0':
            e3 = e3[1:]
        valor = f'{e3}-{e2}-{e1}'

    return valor


def extraerNum(cadena):
    '''
    Extrae el numero del nombre de los archivos de precio para generar después la fecha
    cadena -> cadena a procesar
    '''
    numero = cadena[cadena.rfind('_') + 1: ]
    return numero



def generarFecha(numero):
    '''
    Crea la fecha a partir del número
    numero -> número a procesar
    '''
    numero = str(numero)
    anio = numero[ :4]
    mes = numero[4:6]
    dia = numero[6: ]
    fecha = anio + '-' + mes + '-' + dia
    fecha = datetime.strptime(fecha, '%Y-%m-%d')

    return fecha


def ordenarDataFrame(df):
    '''
    Ordena las columnas del df
    df -> df de pandas
    '''
    df = df[['producto_id', 'sucursal_id', 'precio', 'fecha']]
    return df


def normalizar_id_producto(id_prod): 
    '''
    Corrige el formato del ID del producto
    id_prod -> ID del producto a procesar
    '''  

    id_prod = str(id_prod)
           
    if ('.' in id_prod):             
        id_prod = id_prod[ :id_prod.find('.')]
   
    cantidad_caracter = len(id_prod) 
    if (cantidad_caracter < 13):    
        id_prod = '0'*(13-cantidad_caracter)+id_prod 
         
=======
'''
Módulo de funciones generales
'''

from datetime import datetime


# Cambiar / por -
def cambiarFecha(valor):
    '''
    Corrige los ID consideardos fechas
    valor -> date
    '''
    if type(valor) == datetime:
        valor = str(valor).strip()
        valor = valor[ :valor.find(' ')]
        e1, e2, e3 = valor.split('-')
        if e2[0] == '0':
            e2 = e2[1:]
        if e3[0] == '0':
            e3 = e3[1:]
        valor = f'{e3}-{e2}-{e1}'

    return valor


def extraerNum(cadena):
    '''
    Extrae el numero del nombre de los archivos de precio para generar después la fecha
    cadena -> cadena a procesar
    '''
    numero = cadena[cadena.rfind('_') + 1: ]
    return numero



def generarFecha(numero):
    '''
    Crea la fecha a partir del número
    numero -> número a procesar
    '''
    numero = str(numero)
    anio = numero[ :4]
    mes = numero[4:6]
    dia = numero[6: ]
    fecha = anio + '-' + mes + '-' + dia
    fecha = datetime.strptime(fecha, '%Y-%m-%d')

    return fecha


def ordenarDataFrame(df):
    '''
    Ordena las columnas del df
    df -> df de pandas
    '''
    df = df[['producto_id', 'sucursal_id', 'precio', 'fecha']]
    return df


def normalizar_id_producto(id_prod): 
    '''
    Corrige el formato del ID del producto
    id_prod -> ID del producto a procesar
    '''  

    id_prod = str(id_prod)
           
    if ('.' in id_prod):             
        id_prod = id_prod[ :id_prod.find('.')]
   
    cantidad_caracter = len(id_prod) 
    if (cantidad_caracter < 13):    
        id_prod = '0'*(13-cantidad_caracter)+id_prod 
         
>>>>>>> f51e15f9726ac2d6b8ef3596280b1aecd6ae9edf
    return id_prod