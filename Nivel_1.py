#Nombre: Infante Lozano Javier Alonso
print("")
print("Ejercicio #1:")
"""
1.- Generador de Formateadores con Transformación: Crea crear_formateador(prefijo, fn_transformacion) 
que devuelva un closure. La función devuelta debe procesar un texto aplicando la lambda/función 
fn_transformacion y concatenar el prefijo.
"""
def crear_formateador(prefijo, fn_transformacion):
    def aplicar_formato(cadena: str) -> str:
        txt_modificado = fn_transformacion(cadena)
        return f"El prefijo {prefijo}, el texto procesado {txt_modificado}"
    return aplicar_formato

fmt_error = crear_formateador("[ERROR] ", lambda t: t.upper())
res_formato = fmt_error("conexion fallida")
print(res_formato)


print("")
print("Ejercicio #2:")
"""
2.- Multiplicador Paramétrico con Mapeo: Crea crear_operador(factor, operacion_lambda) que devuelva un 
closure capaz de aplicar la operación recibida utilizando el factor encapsulado.
"""
def crear_operador(factor, operacion_lambda):
    def ejecutar_operacion(valor_num: float) -> float:
        res_operacion = operacion_lambda(valor_num, factor)
        return res_operacion
    return ejecutar_operacion

duplicar_val = crear_operador(2, lambda x, f: x * f)
res_multiplicacion = duplicar_val(25)
print(res_multiplicacion)


print("")
print("Ejercicio #3:")
"""
3.- Calculador de Descuentos con Regla Dinámica: Crea crear_descuento_dinamico(regla_condicional_lambda) 
que devuelva un closure. Este evaluará el precio con la lambda enviada para determinar si aplica un 
descuento prefijado.
"""
def crear_descuento_dinamico(regla_condicional_lambda):
    tasa_descuento = 0.10  # Descuento prefijado del 10%
    def calcular_precio_final(monto_base: float) -> float:
        if regla_condicional_lambda(monto_base):
            return monto_base * (1.0 - tasa_descuento)
        return monto_base
    return calcular_precio_final

desc_compras_grandes = crear_descuento_dinamico(lambda p: p > 100)
res_sin_descuento = desc_compras_grandes(80)
res_con_descuento = desc_compras_grandes(150)
print(f"Total sin descuento ${res_sin_descuento}")
print(f"Total con descuento ${res_con_descuento}")


print("")
print("Ejercicio #4:")
"""
4.- Generador de Seriales / Nombres Únicos: Crea crear_generador_sufijos(patron_lambda) que devuelva un 
closure para transformar nombres de archivos basándose en una lambda de formato.
"""
def crear_generador_sufijos(patron_lambda):
    def construir_nombre(nombre_raiz: str, id_secuencia) -> str:
        sufijo_generado = patron_lambda(id_secuencia)
        return f"{nombre_raiz}{sufijo_generado}"
    return construir_nombre

generar_version = crear_generador_sufijos(lambda v: f"_v{v:03d}.txt")
archivo_salida = generar_version("reporte_mensual", 4)
print(archivo_salida)


print("")
print("Ejercicio #5:")
"""
5.- Conversor de Divisas con Margen: Crea crear_conversor(tasa, margen_lambda) que retorne una función para 
convertir montos calculando dinámicamente la comisión adicional.
"""
def crear_conversor(tasa, margen_lambda):
    def ejecutar_conversion(monto_origen: float) -> float:
        monto_convertido_base = monto_origen * tasa
        recargo_comision = margen_lambda(monto_origen)
        return monto_convertido_base + recargo_comision
    return ejecutar_conversion

conversor_eur_usd = crear_conversor(1.08, lambda m: 2.0 if m < 50 else m * 0.015)

monto_total_pago = conversor_eur_usd(100)
print(f"Total a pagar en Dolares ${monto_total_pago}")