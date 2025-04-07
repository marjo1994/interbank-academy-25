from typing import List, Optional
from dataclasses import dataclass
from services.reporting import generar_reporte
from services.validation import validar_data
from models import ReporteTransaccion

@dataclass
class ProcesamientoResultado:
    reporte: Optional[ReporteTransaccion]
    errores: List[str]

def ejecutar_procesamiento(ruta_csv: str) -> ProcesamientoResultado:
    """
    Función principal que incluye el procesamiento completo
    
    Args:
        ruta_csv: Ruta al archivo CSV de entrada
        
    Returns:
        ProcesamientoResultado: Contiene el reporte y los errores
    """
    try:
        # Validación de datos
        transacciones_validas, errores = validar_data(ruta_csv)
        
        # Si no hay transacciones válidas, retorna solo errores
        if not transacciones_validas:
            return ProcesamientoResultado(None, errores)
        
        # Generación del reporte
        reporte = generar_reporte(transacciones_validas)
        
        # Retorno del resultado
        return ProcesamientoResultado(reporte, errores)
        
    except Exception as e:
        # Manejo de errores inesperados
        return ProcesamientoResultado(None, [str(e)])