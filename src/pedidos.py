from dataclasses import dataclass

COSTO_ENVIO_EXPRESS = 1500
DESCUENTO_CUPON_PROMO = 0.10

# Factor multiplicador por (tipo_cliente, país). Sin ramas anidadas.
FACTORES = {
    ("minorista", "AR"): 1.00,
    ("minorista", "UY"): 0.95,
    ("mayorista", "AR"): 0.80,
    ("mayorista", "UY"): 0.85,
}
FACTOR_POR_DEFECTO = {"minorista": 1.10, "mayorista": 1.05}
BONUS_VIP = {"AR": 0.10, "UY": 0.10}


@dataclass(frozen=True)
class Pedido:
    tipo_cliente: str
    pais: str
    monto: float
    es_vip: bool = False
    cupon: str = ""
    envio_express: bool = False


def _factor_base(pedido: Pedido) -> float:
    clave = (pedido.tipo_cliente, pedido.pais)
    if clave in FACTORES:
        return FACTORES[clave]
    return FACTOR_POR_DEFECTO.get(pedido.tipo_cliente, 1.0)


def _descuento_extra(pedido: Pedido) -> float:
    extra = BONUS_VIP.get(pedido.pais, 0) if pedido.es_vip else 0
    if pedido.cupon == "PROMO10":
        extra += DESCUENTO_CUPON_PROMO
    return extra


def calcular_total(pedido: Pedido) -> float:
    total = pedido.monto * (_factor_base(pedido) - _descuento_extra(pedido))
    if pedido.envio_express:
        total += COSTO_ENVIO_EXPRESS
    return total
