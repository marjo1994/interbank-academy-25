import argparse
import sys
from pathlib import Path
from main import ejecutar_procesamiento
from models import ReporteTransaccion
from config import INPUT_DIR, OUTPUT_DIR

def validar_archivo(nombre_archivo: str) -> Path:
    """Valida y localiza un archivo CSV, buscando en:
    1. La ruta exacta proporcionada
    2. El directorio de input configurado
    
    Args:
        nombre_archivo: Nombre o ruta del archivo
        
    Returns:
        Path del archivo validado
        
    Raises:
        FileNotFoundError: Si no se encuentra en ninguna ubicación válida
        ValueError: Si no es un archivo CSV
    """
    # Convertir a Path
    archivo_path = Path(nombre_archivo)
    
    # Primero intentar con la ruta exacta
    if archivo_path.exists():
        if archivo_path.suffix.lower() == '.csv':
            return archivo_path.resolve()
        raise ValueError(f"El archivo {archivo_path} no es CSV")

    # Buscar en el directorio de input
    ruta_input = INPUT_DIR / nombre_archivo
    if ruta_input.exists():
        if ruta_input.suffix.lower() == '.csv':
            return ruta_input.resolve()
        raise ValueError(f"El archivo {ruta_input} no es CSV")

    # Si no se encontró en ninguna ubicación
    raise FileNotFoundError(
        f"No se encontró '{nombre_archivo}' como:\n"
        f"- Ruta absoluta/relativa: {archivo_path.resolve()}\n"
        f"- En directorio input: {ruta_input.resolve()}"
    )

def formatear_reporte(reporte: ReporteTransaccion) -> str:
    """Formatea el reporte para salida en consola/archivo"""
    return (
        "Reporte de Transacciones\n"
        f"{'-' * 30}\n"
        f"Balance Final: {reporte.balance_final}\n"
        f"Transacción de Mayor Monto: ID {reporte.max_transaccion.id} - {reporte.max_transaccion.monto}\n"
        f"Conteo de Transacciones: Crédito: {reporte.conteo_transacciones.credito} Débito: {reporte.conteo_transacciones.debito}"
    )

def configurar_argumentos() -> argparse.ArgumentParser:
    """Configura los argumentos de línea de comandos"""
    parser = argparse.ArgumentParser(
        description='Generador de Reportes de Transacciones Bancarias',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    
    parser.add_argument(
        'archivo',
        type=str,
        help='Ruta al archivo CSV con transacciones'
    )
    
    parser.add_argument(
        '-o', '--output',
        type=str,
        help='Guardar reporte en archivo (opcional)'
    )
    
    parser.add_argument(
        '--mostrar-errores',
        action='store_true',
        help='Mostrar todos los errores de validación'
    )
    
    return parser

def main():
    parser = configurar_argumentos()
    args = parser.parse_args()
    
    try:
        # Validar archivo de entrada
        archivo_csv = validar_archivo(args.archivo)
        
        # Ejecutar procesamiento principal
        resultado = ejecutar_procesamiento(str(archivo_csv))
        
        # Manejar errores
        if resultado.errores:
            print(f"\nErrores de validación ({len(resultado.errores)}):", file=sys.stderr)
            if args.mostrar_errores:
                for error in resultado.errores:
                    print(f" • {error}", file=sys.stderr)
        
        # Mostrar reporte
        if resultado.reporte:

            resultado_formateado = formatear_reporte(resultado.reporte)
            print(resultado_formateado)
            
            # Guardar en archivo si se especificó
            if args.output:

                nombre_salida = args.output.replace('.txt', '') + '.txt'
                ruta_salida = OUTPUT_DIR / nombre_salida
                
                with open(ruta_salida, 'w', encoding='utf-8') as f:
                    f.write(resultado_formateado)
                
                print(f"\nReporte guardado en: {ruta_salida}")
        
    except Exception as e:
        print(f"\nError: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()