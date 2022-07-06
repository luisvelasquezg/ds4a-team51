import pandas as pd

df_jardines = pd.read_csv('./data/BD.csv')

# Removing non-numerical characters in column 'INSCRIPCION'
df_jardines['INSCRIPCION'] = df_jardines['INSCRIPCION'].apply( lambda x: ''.join(filter(str.isdigit, str(x))) )


####################################################################################################
#       VARIABLES
###################################################################################################

# tipo cumplimiento

terminos = {
    'PRIVADO': 'Privado',
    'PUBLICO': 'Público'
}

ultimo_annio = 2019


####################################################################################################
#       FUNCTIONS
###################################################################################################

def tipo_jardines():
    '''
    Retorna la lista de Tipos de Jardines
    '''
    tipos = df_jardines['TIPO'].unique()
    return tipos


def cantidad_tipo_jardines():
    '''
    Retorna una Serie de Pandas del número de Jardines por Tipo.
    Columnas: 'TIPO', 'CANTIDAD'
    '''
    jardines_por_tipo = df_jardines[['INSCRIPCION', 'NOMBRE', 'TIPO']].drop_duplicates('INSCRIPCION')
    cantidad_tipos = jardines_por_tipo.groupby(jardines_por_tipo['TIPO']).size()#.reset_index()
    # info_tipos = info_tipos.rename(columns = {0: 'CANTIDAD'})
    # info_tipos['TOTAL']
    return cantidad_tipos


# def info_cumplimiento_general_tipo():
#     '''
#     Retorna un DataFrame con el promedio del Cumplimiento General por Tipo de Jardín del
#     último año.
#     '''
#     df_1 = df_jardines[df_jardines['AÑO'] == ultimo_annio][['INSCRIPCION', 'NOMBRE', 'TIPO', 'General']]
#     # Agrupación por Tipo
#     cumplimiento_general_tipo = df_1.groupby('TIPO').mean('General').reset_index()
#     return cumplimiento_general_tipo

def info_cumplimiento_tipos(cumplimiento_general = True):
    '''
    Retorna un DataFrame con el promedio del Cumplimiento de cada Componente
    Evaluativo por Tipo de Jardín, del último año.
    '''
    columnas = [
        'INSCRIPCION',
        'NOMBRE',
        'TIPO',
        'General',
        'Nutrición y Salubridad',
        'Ambientes Adecuados y Seguros',
        'Proceso Pedagógico',
        'Talento Humano',
        'Proceso Administrativo'
    ]

    df_1 = df_jardines[df_jardines['AÑO'] == ultimo_annio][columnas]
    cumplimiento_tipos_general = df_1.groupby('TIPO').mean().reset_index()

    if cumplimiento_general:
        ##  Columnas:   [TIPO, General, (... Componentes)]
        return cumplimiento_tipos_general
    else:
        ##  Columnas:   [COMPONENTE, PRIVADO, PUBLICO]
        
        # Se transpone el DataFrame 'cumplimiento_tipos_general'
        cumplimiento_tipos_componentes = cumplimiento_tipos_general.set_index('TIPO').T.rename_axis('COMPONENTE').reset_index()
        cumplimiento_tipos_componentes = cumplimiento_tipos_componentes.drop([0], axis = 0)
        # cumplimiento_tipos_componentes = cumplimiento_tipos_general.set_index('TIPO').T
        # cumplimiento_tipos_componentes.rename_axis('COMPONENTE').reset_index(inplace = True)
        
        # Se elimina la primera fila (Cumplimiento 'General')
        # cumplimiento_tipos_componentes = cumplimiento_tipos_componentes.drop([0], axis = 0)
        # cumplimiento_tipos_componentes.drop([0], inplace = True)
        
        return cumplimiento_tipos_componentes



