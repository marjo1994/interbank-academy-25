import pytest
import sys
import os
# Agrega el directorio src al PATH de Python
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from services.reporting import generar_reporte
from models import Transaccion, TipoTransaccion, ReporteTransaccion

def test_generar_reporte_con_datos_validos():
    """Verifica cálculo correcto de balance, máximo y conteos."""
    transacciones = [
        Transaccion(id=1, tipo=TipoTransaccion.CREDITO, monto=150.75),
        Transaccion(id=2, tipo=TipoTransaccion.CREDITO, monto=200.00),
        Transaccion(id=3, tipo=TipoTransaccion.DEBITO, monto=50.25)
    ]
    
    reporte = generar_reporte(transacciones)
    
    assert reporte.balance_final == 300.50
    assert reporte.max_transaccion.id == 2
    assert reporte.conteo_transacciones.credito == 2
    assert reporte.conteo_transacciones.debito == 1

def test_redondeo_a_dos_decimales():
    """Verifica que el balance final tenga exactamente 2 decimales."""
    transacciones = [
        Transaccion(id=1, tipo=TipoTransaccion.CREDITO, monto=100.4567),
        Transaccion(id=2, tipo=TipoTransaccion.DEBITO, monto=50.1234)
    ]
    
    reporte = generar_reporte(transacciones)
    assert reporte.balance_final == 50.34
    assert str(reporte.balance_final).split('.')[1] == '34'  # Verifica decimales

def test_reporte_sin_transacciones():
    """Verifica manejo de lista vacía."""
    with pytest.raises(ValueError, match="No hay transacciones válidas"):
        generar_reporte([])