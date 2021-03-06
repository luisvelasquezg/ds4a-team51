import pandas as pd
from components.table.table import *

segmentos = pd.read_csv('./data/segmentos.csv')

# Removing non-numerical characters in column 'INSCRIPCION'
segmentos['INSCRIPCION'] = segmentos['INSCRIPCION'].apply( lambda x: ''.join(filter(str.isdigit, str(x))) )


####################################################################################################
#       VARIABLES
###################################################################################################

dic_tipo_jardines = {'PRIVADO': 'Privado', 'PUBLICO': 'Público'}

annio_reciente = 2019

listado_segmentos = ['Alto', 'Medio', 'Bajo']
listado_localidades = sorted(list(segmentos['LOCALIDAD'].unique()))
listado_tipos = ['PRIVADO', 'PUBLICO']


# Variables para Tabla Segmentos

# columnas_tabla = [
#     'INSCRIPCION',
#     'NOMBRE',
#     'LOCALIDAD',
#     'TIPO',
#     'Segmento'
# ]

# parametros_tabla = {
#     'title': 'Segmentos',
#     'description': 'Tabla de segmentación de los jardines',
#     'columns': columnas_tabla
# }



####################################################################################################
#   Funciones
###################################################################################################

def consultar_datos_componentes(segmento, localidad, tipo):
    '''
    Retorna DataFrame ('promedio_componentes') de los Componentes Evaluativos
    con los parámetros especificados y una variable Booleana ('existen_datos')
    referente a si existen datos o no.
    '''
    existen_datos = True
    columnas_segmentos = [
            # 'INSCRIPCION',
            # 'NOMBRE',
            'Segmento',
            'LOCALIDAD',
            'TIPO',
            'Nutrición y Salubridad',
            'Ambientes Adecuados y Seguros',
            'Proceso Pedagógico',
            'Talento Humano',
            'Proceso Administrativo'
    ]

    # segmentos_reciente  = segmentos.copy()
    # filtro = segmentos['AÑO'] == annio_reciente
    segmentos_reciente = segmentos[segmentos['AÑO'] == annio_reciente][columnas_segmentos]

    datos_seleccionados = segmentos_reciente[
                                    segmentos_reciente['Segmento'].isin(segmento) &
                                    segmentos_reciente['LOCALIDAD'].isin(localidad) &
                                    segmentos_reciente['TIPO'].isin(tipo)
                                ]

    # if datos_seleccionados.empty:
    #     # mensaje = 'No se encuentran datos con los parámetros seleccionados.'
    #     # return mensaje
    #     return None

    # Se calcula el promedio de cada columna numérica y se agrupan los datos por el Segmento
    promedio_componentes = datos_seleccionados.groupby('Segmento').mean()
    
    # Se transpone el DataFrame y se renombra el eje
    promedio_componentes = promedio_componentes.T.rename_axis('COMPONENTE').reset_index()

    # Se renombra la columna de promedios
    promedio_componentes = promedio_componentes.rename(columns = {f'{segmento[0]}': 'PROMEDIO'})

    if 'PROMEDIO' not in promedio_componentes.columns:
        existen_datos = False
        promedio_componentes['PROMEDIO'] = 0.0

    return promedio_componentes, existen_datos

################################################################

def generar_tabla_segmentos():
    '''
    Retorna tabla de Segmentos de los Jardines.
    '''
    columnas_tabla = [
        'INSCRIPCION',
        'NOMBRE',
        'LOCALIDAD',
        'TIPO',
        'Segmento'
    ]

    parametros_tabla = {
        'title': 'Segmentos',
        'description': 'Tabla de segmentación de los jardines.',
        'columns': columnas_tabla
    }

    datos_tabla = segmentos[columnas_tabla]
    tabla_segmentos = table(datos_tabla, parametros_tabla)

    return tabla_segmentos



    ###################################################################################################