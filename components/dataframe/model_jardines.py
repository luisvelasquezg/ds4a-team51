import pandas as pd

df_jardines = pd.read_csv('./data/BD.csv')
# df_jardines = pd.read_csv('./data/BD.xlsx')

# Removing non-numerical characters in column 'INSCRIPCION'
df_jardines['INSCRIPCION'] = df_jardines['INSCRIPCION'].apply( lambda x: ''.join(filter(str.isdigit, str(x))) )

# df_jardines['LOCALIDAD'] = df_jardines['LOCALIDAD'].dropna()


# print(df_jardines['LOCALIDAD'].tolist())
####################################################################################################
#       VARIABLES
###################################################################################################

# tipo cumplimiento

terminos = {
    'PRIVADO': 'Privado',
    'PUBLICO': 'Público'
}

annio_reciente = 2019

listado_cumplimiento = [
    'General',
    'Nutrición y Salubridad',
    'Ambientes Adecuados y Seguros',
    'Proceso Pedagógico',
    'Talento Humano',
    'Proceso Administrativo'
]

# print(df_jardines['AÑO'].unique())
# print(df_jardines['LOCALIDAD'].unique())
# print(df_jardines['LOCALIDAD'].sort_values().unique())

listado_localidades = df_jardines['LOCALIDAD'].drop_duplicates().dropna().sort_values()#.unique()
# listado_localidades = df_jardines['LOCALIDAD'].sort_values().unique()
# listado_localidades = sorted(df_jardines['LOCALIDAD'].sort_values().unique().tolist())
listado_annios = df_jardines['AÑO'].drop_duplicates().dropna()
# listado_annios = df_jardines['AÑO'].unique()
listado_tipos = ['PRIVADO', 'PUBLICO']




####################################################################################################
#       FUNCTIONS
###################################################################################################

def consultar_promedio_cumplimiento(cumplimiento, localidades, annios, tipos):
    '''
    Retorna una DataFrame sobre el promedio de los cumplimientos según
    los parámetros especificados.
    '''
    existen_datos = True
    # datos_seleccion = df_jardines['INSCRIPCION'].drop_duplicates()
    datos_seleccion = df_jardines[
                            df_jardines['LOCALIDAD'].isin(localidades) &
                            df_jardines['AÑO'].isin(annios) &
                            df_jardines['TIPO'].isin(tipos)
                        ]
    
    if datos_seleccion.empty:
        existen_datos = False

    datos_seleccion = pd.DataFrame(datos_seleccion.groupby(['LOCALIDAD', 'AÑO'])[cumplimiento].mean()).reset_index()
    return datos_seleccion, existen_datos



# def consultar_promedio_cumplimiento_2(cumplimiento, localidad, annio, tipo):
    
#     new_df = df_jardines[df_jardines['LOCALIDAD'].isin(localidad) & df_jardines["AÑO"].isin(annio)]
#     line_data = pd.DataFrame(new_df.groupby(['LOCALIDAD','AÑO'])[cumplimiento].mean()).reset_index()
#     return line_data


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
    jardines_por_tipo = df_jardines[df_jardines['AÑO'] == annio_reciente]
    jardines_por_tipo = jardines_por_tipo[['INSCRIPCION', 'NOMBRE', 'TIPO']].drop_duplicates('INSCRIPCION')
    cantidad_tipos = jardines_por_tipo.groupby(jardines_por_tipo['TIPO']).size()#.reset_index()
    # info_tipos = info_tipos.rename(columns = {0: 'CANTIDAD'})
    # info_tipos['TOTAL']
    return cantidad_tipos



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

    df_1 = df_jardines[df_jardines['AÑO'] == annio_reciente][columnas]
    cumplimiento_tipos_general = df_1.groupby('TIPO').mean().reset_index()

    if cumplimiento_general:
        ##  Columnas:   [TIPO, General, (... Componentes)]
        return cumplimiento_tipos_general
    else:
        ##  Columnas:   [COMPONENTE, PRIVADO, PUBLICO]
        # Se transpone el DataFrame 'cumplimiento_tipos_general'
        cumplimiento_tipos_componentes = cumplimiento_tipos_general.set_index('TIPO').T.rename_axis('COMPONENTE').reset_index()
        cumplimiento_tipos_componentes = cumplimiento_tipos_componentes.drop([0], axis = 0)
        
        
        return cumplimiento_tipos_componentes



