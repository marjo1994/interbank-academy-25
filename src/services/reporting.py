from typing import List
import pandas as pd
from models import Transaccion, ReporteTransaccion, ConteoTransacciones, MaxTransaccion

def generar_reporte(transacciones_validas: List[Transaccion]) -> ReporteTransaccion:
    """
    Genera un reporte de transacciones con balance, transacción máxima y conteo por tipo.
    
    Args:
        transacciones_validas (List[Transaccion]): Lista de transacciones válidas.
        
    Returns:
        ReporteTransaccion: Reporte estructurado.
    """
    if not transacciones_validas:
        raise ValueError("No hay transacciones válidas para generar el reporte")

    # Convertir a DataFrame para cálculos
    df = pd.DataFrame([t.model_dump() for t in transacciones_validas])

    # Filtra las transacciones de crédito y suma los montos, las mismas operaciones para las transacciones tipo débito. Finalmente, halla el balance realizando la resta de ambos montos (créditos - débitos)
    credito_total = df[df["tipo"] == "Crédito"]["monto"].sum()
    debito_total = df[df["tipo"] == "Débito"]["monto"].sum()
    balance_final = round(credito_total - debito_total, 2)

    # Encuentra la transacción de mayor monto, utilizando idxmax para calcular el índice de la transacción de mayor monto y loc para buscar la fila por el índice correspondiente.
    max_row = df.loc[df['monto'].idxmax()]

    # Valida el modelo de MaxTransacción
    max_transaccion = MaxTransaccion(id=int(max_row['id']), monto=float(max_row['monto']))

    # Conteo por tipo de transacción: crédito y débito
    conteo = df['tipo'].value_counts().to_dict()

    # Valida el modelo de ConteoTransacciones
    conteo_transacciones = ConteoTransacciones(
        Crédito=conteo.get('Crédito', 0),
        Débito=conteo.get('Débito', 0)
    )
    
    #Valida el modelo del reporte
    return ReporteTransaccion(
        balance_final=balance_final,
        max_transaccion=max_transaccion,
        conteo_transacciones=conteo_transacciones
    )



