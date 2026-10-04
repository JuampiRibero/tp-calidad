import pytest

from pedidos import calcular_total


@pytest.mark.parametrize(
    "tipo, pais, monto, vip, cupon, express, esperado",
    [
        ("minorista", "AR", 1000, True, "PROMO10", False, 800),
        ("minorista", "AR", 1000, True, "", False, 900),
        ("minorista", "AR", 1000, False, "PROMO10", False, 900),
        ("minorista", "AR", 1000, False, "", False, 1000),
        ("minorista", "UY", 1000, True, "", False, 850),
        ("minorista", "UY", 1000, False, "", False, 950),
        ("minorista", "BR", 1000, False, "", False, 1100),
        ("mayorista", "AR", 1000, True, "", False, 700),
        ("mayorista", "AR", 1000, False, "", False, 800),
        ("mayorista", "UY", 1000, False, "", False, 850),
        ("mayorista", "BR", 1000, False, "", False, 1050),
        ("otro", "AR", 1000, False, "", False, 1000),
        ("minorista", "AR", 1000, False, "", True, 2500),
    ],
)
def test_calcular_total(tipo, pais, monto, vip, cupon, express, esperado):
    assert calcular_total(tipo, pais, monto, vip, cupon, express) == pytest.approx(esperado)