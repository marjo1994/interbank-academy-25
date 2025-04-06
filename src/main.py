from services.reporting import generar_reporte
from services.validation import validar_data
import os

def main():

    # Definimos la ruta de la data, utilizando os para compatibilidad con los sistemas
    ruta_csv = os.path.join("../input", "data.csv")
    
    try:
        transacciones_validas, errores = validar_data(ruta_csv)

        if transacciones_validas:

            reporte = generar_reporte(transacciones_validas)
            print(f"Reporte: {reporte}");

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{ruta_csv}'")

    except Exception as e:
        print(f"Error inesperado: {str(e)}")

if __name__ == "__main__":
    main()
