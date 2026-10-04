import os, sys

def calcular_total(tipo_cliente, pais, monto, es_vip, cupon, envio_express):
    if tipo_cliente == "minorista":
        if pais == "AR":
            if es_vip:
                if cupon == "PROMO10":
                    total = monto * 0.80
                else:
                    total = monto * 0.90
            else:
                if cupon == "PROMO10":
                    total = monto * 0.90
                else:
                    total = monto
        elif pais == "UY":
            if es_vip:
                total = monto * 0.85
            else:
                total = monto * 0.95
        else:
            total = monto * 1.10
    elif tipo_cliente == "mayorista":
        if pais == "AR":
            if es_vip:
                total = monto * 0.70
            else:
                total = monto * 0.80
        elif pais == "UY":
            total = monto * 0.85
        else:
            total = monto * 1.05
    else:
        total = monto
    if envio_express:
        total = total + 1500
    return total

def calcular_total_exportacion(tipo_cliente, pais, monto, es_vip, cupon, envio_express):
    if tipo_cliente == "minorista":
        if pais == "AR":
            if es_vip:
                if cupon == "PROMO10":
                    total = monto * 0.80
                else:
                    total = monto * 0.90
            else:
                total = monto
        else:
            total = monto * 1.10
    else:
        total = monto
    if envio_express:
        total = total + 1500
    return total