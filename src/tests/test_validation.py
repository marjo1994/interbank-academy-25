import pytest
import sys
import os
# Agrega el directorio src al PATH de Python
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from services.validation import validar_data
from models import Transaccion

def test_archivo_valido(tmp_path):
    """Verifica que un CSV válido se procese correctamente."""
    csv_data = "id,tipo,monto\n1,Crédito,100.50\n2,Débito,50.00"
    file_path = tmp_path / "test.csv"
    file_path.write_text(csv_data, encoding="utf-8")
    
    transacciones_validas, errores = validar_data(file_path)
    assert len(transacciones_validas) == 2
    assert not errores
    assert isinstance(transacciones_validas[0], Transaccion)

def test_archivo_con_errores(tmp_path):
    """Verifica detección de montos inválidos y tipos incorrectos."""
    csv_data = "id,tipo,monto\n1,Crédito,-100.00\n2,Préstamo,50.00"
    file_path = tmp_path / "test.csv"
    file_path.write_text(csv_data, encoding="utf-8")
    
    _, errores = validar_data(file_path)
    assert len(errores) == 2
    assert "monto: Input should be greater than 0" in errores[0]
    assert "tipo: Input should be 'Crédito' or 'Débito" in errores[1]

def test_archivo_no_existente():
    """Verifica manejo de archivos no encontrados."""
    with pytest.raises(FileNotFoundError):
        validar_data("ruta/inexistente.csv")