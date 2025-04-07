import pytest
from models import Transaccion, ConteoTransacciones
from pydantic import ValidationError

def test_transaccion_valida():
    """Verifica creación de transacción válida."""
    t = Transaccion(id=1, tipo="Crédito", monto=100.50)
    assert t.monto == 100.50 

def test_transaccion_monto_invalido():
    """Verifica validación de montos negativos."""
    with pytest.raises(ValidationError) as excinfo:
        Transaccion(id=1, tipo="Crédito", monto=-100.00)
    assert "Input should be greater than 0" in str(excinfo.value)

def test_conteo_transacciones_con_alias():
    """Verifica mapeo correcto de alias 'Crédito' → 'credito'."""
    conteo = ConteoTransacciones(**{"Crédito": 5, "Débito": 3})
    assert conteo.credito == 5
    assert conteo.debito == 3

