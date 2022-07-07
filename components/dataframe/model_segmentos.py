import pandas as pd

segmentos = pd.read_csv('./data/segmentos.csv')

# Removing non-numerical characters in column 'INSCRIPCION'
segmentos['INSCRIPCION'] = segmentos['INSCRIPCION'].apply( lambda x: ''.join(filter(str.isdigit, str(x))) )


####################################################################################################
#       VARIABLES
###################################################################################################

# tipo cumplimiento

terminos = {
    'PRIVADO': 'Privado',
    'PUBLICO': 'Público'
}

annio_reciente = 2019

# columnas_segmentos = [
#             # 'INSCRIPCION',
#             # 'NOMBRE',
#             'Segmento',
#             'LOCALIDAD',
#             'TIPO',
#             'Nutrición y Salubridad',
#             'Ambientes Adecuados y Seguros',
#             'Proceso Pedagógico',
#             'Talento Humano',
#             'Proceso Administrativo'
#         ]



####################################################################################################
#       FUNCTIONS
###################################################################################################

def consultar_datos_componentes(segmento, localidad, tipo):
    '''
    Retorna DataFrame de los Componentes Evaluativos con los parámetros especificados.
    '''

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
    #     return datos_seleccionados

    # Se calcula el promedio de cada columna numérica y se agrupan los datos por el Segmento
    promedio_componentes = datos_seleccionados.groupby('Segmento').mean()
    
    # Se transpone el DataFrame y se renombra el eje
    promedio_componentes = promedio_componentes.T.rename_axis('COMPONENTE').reset_index()

    # Se renombra la columna de promedios
    promedio_componentes = promedio_componentes.rename(columns = {f'{segmento[0]}': 'PROMEDIO'})

    return promedio_componentes

