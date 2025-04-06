from typing import List, Tuple
import pandas as pd
from pydantic import ValidationError
from models import Transaccion

def validar_data(ruta_csv: str) -> Tuple[List[Transaccion], List[str]]:
    """
    Valida un archivo CSV y retorna las transacciones válidas y errores encontrados.
    
    Args:
        ruta_csv (str): Ruta al archivo CSV.
        
    Returns:
        Tuple[List[Transaccion], List[str]]: (transacciones válidas, lista de errores)
    """

    # Lee el archivo CSV
    df = pd.read_csv(ruta_csv)

    transacciones_validas = []
    errores = []

    # Itera cada una de las filas del archivo
    for indice, fila in df.iterrows():
        try:
            # Convierte cada fila a diccionario y valida con el modelo Transaccion
            transaccion = Transaccion(**fila.to_dict())
            transacciones_validas.append(transaccion)
        except ValidationError as e:
            # Formatear errores de validación de Pydantic
            mensajes_error = [f"{error['loc'][0]}: {error['msg']}" for error in e.errors()]
            errores.append(f"Fila {indice + 1} - {', '.join(mensajes_error)}")
        except Exception as e:
            #Formatea errores genéricos, no esperados.
            errores.append(f"Fila {indice + 1} - Error inesperado: {str(e)}")

    return transacciones_validas, errores