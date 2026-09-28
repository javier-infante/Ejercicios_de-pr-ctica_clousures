#Nombre: Infante Lozano Javier Alonso


print("")
print("Ejercicio #6:")
"""
6.- Contador Ponderado: Crea crear_contador_paso(fn_paso) que incremente su estado interno 
utilizando una lambda fn_paso(cuenta_actual) en lugar de un incremento fijo.
"""
def crear_contador_paso(fn_paso):
    conteo_actual = 0
    def avanzar_paso():
        nonlocal conteo_actual
        conteo_actual = fn_paso(conteo_actual)
        return conteo_actual
    return avanzar_paso

secuencia_exp = crear_contador_paso(lambda c: c + 2 if c < 6 else c * 2)
print("Paso 1.-", secuencia_exp())
print("Paso 2.-", secuencia_exp())
print("Paso 3.-", secuencia_exp())
print("Paso 4.-", secuencia_exp())



print("")
print("Ejercicio #7:")
"""
7.- Acumulador con Filtro de Aceptación: Crea crear_acumulador_validado(criterio_lambda) 
que mantenga un total acumulado privado, pero solo sume los valores que superen la prueba 
de la lambda enviada.
"""
def crear_acumulador_validado(criterio_lambda):
    suma_acumulada = 0
    def sumar_valor(monto: float) -> float:
        nonlocal suma_acumulada
        if criterio_lambda(monto):
            suma_acumulada += monto
        return suma_acumulada
    return sumar_valor


acumulador_numeros_pares = crear_acumulador_validado(lambda x: x > 0 and x % 2 == 0)
print("Suma 4 que es valido: ", acumulador_numeros_pares(4))
print("Suma 5 que es rechazado: ", acumulador_numeros_pares(5))
print("Suma -2 que es rechazado: ", acumulador_numeros_pares(-2))
print("Suma 6 que es valido: ", acumulador_numeros_pares(6))



print("")
print("Ejercicio #8:")
"""
8.- Promediador con Eliminación de Valores Extremos: Crea crear_promediador_filtrado(filtro_ruido_lambda) 
que acumule datos privadamente pero aplique la lambda para descartar valores atípicos antes de r
ecalcular el promedio.
"""
def crear_promediador_filtrado(filtro_ruido_lambda):
    registro_datos = []

    def calcular_promedio(valor_ingresado: float):
        nonlocal registro_datos
        if filtro_ruido_lambda(valor_ingresado):
            registro_datos.append(valor_ingresado)

        if not registro_datos:
            return 0.0

        promedio_obtenido = sum(registro_datos) / len(registro_datos)
        return promedio_obtenido

    return calcular_promedio


promediador_calificaciones = crear_promediador_filtrado(lambda valor: 0 <= valor <= 100)

print("Ingresa 80 que es valido y su promedio es:", promediador_calificaciones(80))
print("Ingresa 90 que es valido y su promedio es:", promediador_calificaciones(90))
print("Ingresa 500 que NO es valido y su promedio es::", promediador_calificaciones(500))
print("Ingresa 75 que es valido y su promedio es:", promediador_calificaciones(75))



print("")
print("Ejercicio #9:")
"""
9.- Limitador de Tasa Inteligente (Rate Limiter con Reset): Crea crear_limitador_avanzado(max_intentos, fn_alerta) 
que cuente ejecuciones privadas y ejecute fn_alerta cuando el límite sea superado.
"""
def crear_limitador_avanzado(max_intentos, fn_alerta):
    conteo_intentos = 0

    def verificar_acceso(actividad_usr: str):
        nonlocal conteo_intentos
        conteo_intentos += 1

        if conteo_intentos > max_intentos:
            return fn_alerta(conteo_intentos)

        return f"La accion {actividad_usr} permitida. Intento {conteo_intentos}/{max_intentos}"

    return verificar_acceso

notificacion_bloqueo = lambda cuenta: f"[BLOQUEO] el limite ha sido superado, numero de intentos {cuenta}"
gestor_acceso = crear_limitador_avanzado(3, notificacion_bloqueo)

print(gestor_acceso("Inicio #1"))
print(gestor_acceso("Inicio #2"))
print(gestor_acceso("Inicio #3"))
print(gestor_acceso("Inicio #4")) 



print("")
print("Ejercicio #10:")
"""
10.- Interruptor Múltiple (Máquina de Estados Ligera): Crea crear_conmutador(lista_estados) 
que alterne cíclicamente entre una lista de estados internos privados en cada llamada.
"""
def crear_conmutador(lista_estados: list):
    posicion_actual = 0

    def rotar_estado() -> str:
        nonlocal posicion_actual
        estado_obtenido = lista_estados[posicion_actual]
        #Avanzamos los indices
        posicion_actual = (posicion_actual + 1) % len(lista_estados)
        return estado_obtenido

    return rotar_estado

control_semaforo = crear_conmutador(["Verde", "Amarillo", "Rojo"])
print("Estado 1.-", control_semaforo())
print("Estado 2.-", control_semaforo())
print("Estado 3.-", control_semaforo())
print("Estado 4.-", control_semaforo(), " se reinicia jaja") 