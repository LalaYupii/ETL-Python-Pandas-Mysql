
'''
Procesamiento de los archivos
Fecha: 27-10-2022
'''
import chardet
from funciones import cambiarFecha, extraerNum, generarFecha, ordenarDataFrame, normalizar_id_producto
from os import listdir
from os.path import isfile, splitext
import pandas as pd



def main():
    print('Comenzando procesamiento')
    # Globales
    ruta_data = '../Datasets/'
    ruta_csv = '../csv/'
    archs = listdir(ruta_data)

    # Detectamos y seleccionamos los archivos a procesar
    extensiones = ['.txt', '.xlsx', '.json', '.csv', '.parquet']
    arch_fallos = []
    arch_ok = []
    # Recorremos los archivo encontrados    
    for arch in archs:
        if isfile(ruta_data + arch):
            # Separamos en nombre y ext de arhivo
            nombre_arch, ext_arch = splitext(arch)
            # Los clasificamos
            if ext_arch in extensiones:
                arch_ok.append(arch)
            else:
                arch_fallos.append(arch)

    ''' Crear CSVs'''
    # Procesamos los archivos xlsx
    for arch in arch_ok:
        # Separamos nombre de ext
        nombre_arch, ext_arch = splitext(arch)
        # Evaluamos la extensión
        if ext_arch == '.xlsx':
            xls = pd.ExcelFile(ruta_data + arch)
            hojas = xls.sheet_names
            xls.close()
            # Procesamos cada hoja del xlsx
            for hoja in hojas:
                # Armamos el nombre del archivo
                numero = hoja[hoja.find('_')+ 1:hoja.find('_', hoja.find('_') + 1)]
                nombre_csv = 'precios_semana_' + numero + '.csv'
                df_hoja = pd.read_excel(ruta_data + arch, sheet_name=hoja)
                df_hoja['sucursal_id'] = df_hoja['sucursal_id'].apply(cambiarFecha)
                if nombre_arch != 'sucursal' and nombre_arch != 'producto':
                    num = extraerNum(hoja)
                    df_hoja['fecha'] = generarFecha(num)
                    df_hoja['producto_id'] = df_hoja['producto_id'].apply(normalizar_id_producto)
                    df_hoja = ordenarDataFrame(df_hoja)
                df_hoja.to_csv(ruta_csv + nombre_csv, index=False, encoding='utf8')
            del(df_hoja)


    # Procesamos los archivos txt
    for arch in arch_ok:
        nombre_arch, ext_arch = splitext(arch)
        if ext_arch == '.txt':
            with open(ruta_data + arch, 'rb') as f:
                resultado = chardet.detect(f.read())
                encod = resultado['encoding']
            df_txt = pd.read_csv(ruta_data +  arch, sep='|', encoding=encod)
            if nombre_arch != 'sucursal' and nombre_arch != 'producto':
                num = extraerNum(nombre_arch)
                df_txt['fecha'] = generarFecha(num)
                df_txt['producto_id'] = df_txt['producto_id'].apply(normalizar_id_producto)
                df_txt = ordenarDataFrame(df_txt)
            df_txt.to_csv(ruta_csv + nombre_arch + '.csv', index=False, encoding='utf8')


    # Procesamos los archivo json
    for arch in arch_ok:
        nombre_arch, ext_arch = splitext(arch)
        if ext_arch == '.json':
            df_json = pd.read_json(ruta_data +  arch)
            if nombre_arch != 'sucursal' and nombre_arch != 'producto':
                num = extraerNum(nombre_arch)
                df_json['fecha'] = generarFecha(num)
                df_json['producto_id'] = df_json['producto_id'].apply(normalizar_id_producto)
                df_json = ordenarDataFrame(df_json)
            df_json.to_csv(ruta_csv + nombre_arch + '.csv', index=False, encoding='utf8')


    # Procesamos los archivos CSV
    for arch in arch_ok:
        nombre_arch, ext_arch = splitext(arch)
        if ext_arch == '.csv':
            with open(ruta_data + arch, 'rb') as f:
                # Detectamos el encoding
                resultado = chardet.detect(f.read())
                encod = resultado['encoding']
            df_csv = pd.read_csv(ruta_data +  arch, encoding=encod)
            if nombre_arch != 'sucursal' and nombre_arch != 'producto':
                num = extraerNum(nombre_arch)
                df_csv['fecha'] = generarFecha(num)
                df_csv['producto_id'] = df_csv['producto_id'].apply(normalizar_id_producto)
                df_csv = ordenarDataFrame(df_csv)
            df_csv.to_csv(ruta_csv + nombre_arch + '.csv', index=False, encoding='utf8')


    # Procesamos los archivos parquet
    for arch in arch_ok:
        nombre_arch, ext_arch = splitext(arch)
        if ext_arch == '.parquet':
            df_parquet = pd.read_parquet(ruta_data +  arch)
            df_parquet.drop(columns=['categoria1', 'categoria2', 'categoria3'], inplace=True)
            if nombre_arch != 'sucursal' and nombre_arch != 'producto':
                num = extraerNum(nombre_arch)
                df_parquet['fecha'] = generarFecha(num)
                df_parquet['producto_id'] = df_parquet['producto_id'].apply(normalizar_id_producto)
                df_parquet = ordenarDataFrame(df_parquet)
            df_parquet.to_csv(ruta_csv + nombre_arch + '.csv', index=False, encoding='utf8')
         
        
    '''Corregimos el ID producto'''
    # Obtenemos los archivos del directorio específico
    archs_csv = listdir(ruta_csv)

    # Nos quedamos solo con los de operaciones comerciales
    archs_csv.remove('sucursal.csv')
    archs_csv.remove('producto.csv')

    # Corregimos el ID de producto
    for csv in archs_csv:
        df = pd.read_csv(ruta_csv + csv, dtype={'producto_id':'str', 'sucursal_id':'str'})
        df['producto_id'] = df['producto_id'].apply(normalizar_id_producto)
        df.to_csv(ruta_csv + csv, index=False)


    '''Eliminamos nulos'''
    archs_csv = listdir(ruta_csv)

    archs_csv.remove('sucursal.csv')
    archs_csv.remove('producto.csv')

    # Eliminamos IDs nulos si los hay
    for arch in archs_csv:
        df = pd.read_csv(ruta_csv + arch, dtype={'producto_id':'str', 'sucursal_id':'str'})
        df.dropna(subset=['producto_id', 'sucursal_id'], inplace=True)
        df.to_csv(ruta_csv + arch, index=False)

    df = pd.read_csv(ruta_csv + 'producto.csv')
    df.dropna(inplace=True)
    df.to_csv(ruta_csv + 'producto.csv', index=False)


    '''Eliminamos duplicados en los ID'''

    df = pd.read_csv(ruta_csv + 'sucursal.csv')
    df.dropna(subset=['id'], inplace=True)
    df['id'] =  df['id'].drop_duplicates()
    df.to_csv(ruta_csv + 'sucursal.csv', index=False)

    df = pd.read_csv(ruta_csv + 'producto.csv')
    df.dropna(subset=['id'], inplace=True)
    df['id'] = df['id'].drop_duplicates()
    df.to_csv(ruta_csv + 'producto.csv', index=False)


    '''Remplazamos precios nulos con 0.0'''

    archs_csv = listdir(ruta_csv)

    archs_csv.remove('producto.csv')
    archs_csv.remove('sucursal.csv')

    for arch in archs_csv:
        df = pd.read_csv(ruta_csv + arch, dtype={'producto_id':'str', 'sucursal_id':'str', 'precio':'float'})
        df['precio'].fillna(0.0, inplace=True)
        df.to_csv(ruta_csv + arch, index=False)

    print('Procesamiento finalizado con éxito!')


if __name__ == '__main__':

    '''
    Procesamiento de los archivos
    Fecha: 27-10-2022
    '''

    import chardet
    from funciones import cambiarFecha, extraerNum, generarFecha, ordenarDataFrame, normalizar_id_producto
    from os import listdir
    from os.path import isfile, splitext
    import pandas as pd
