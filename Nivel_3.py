#Nombre: Infante Lozano Javier Alonso

from functools import reduce
import time

print("")
print("Ejercicio #11:")
"""
11.- Pipeline de Mapeo y Filtrado Combinado: Crea la HOF procesar_coleccion(lista, fn_predicado, fn_transformacion) 
que combine internamente filter y map pasando expresiones lambda.
"""
def procesar_coleccion(lista: list, fn_predicado, fn_transformacion) -> list:
    items_filtrados = filter(fn_predicado, lista)
    items_mapeados = map(fn_transformacion, items_filtrados)
    return list(items_mapeados)

secuencia_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

res_pipeline = procesar_coleccion(
    secuencia_nums,
    lambda x: x > 3 and x % 2 == 0,
    lambda x: x ** 2
)
print("Pipeline resultado: ", res_pipeline)



print("")
print("Ejercicio #12:")
"""
12.- Reductor / Agrupador Personalizado: Crea la HOF agrupar_por(lista, fn_clave) que reciba una colección de diccionarios 
y los agrupe en un diccionario clave-valor basándose en el resultado de la lambda fn_clave.
"""
def agrupar_por(lista: list, fn_clave) -> dict:
    def reducir_grupos(mapa_agrupado: dict, registro: dict) -> dict:
        llave_grupo = fn_clave(registro)
        if llave_grupo not in mapa_agrupado:
            mapa_agrupado[llave_grupo] = []
        mapa_agrupado[llave_grupo].append(registro)
        return mapa_agrupado

    return reduce(reducir_grupos, lista, {})

listado_estudiantes = [
    {"nombre": "Carlos", "carrera": "Software", "promedio": 9.1},
    {"nombre": "David", "carrera": "TICS", "promedio": 9.1},
    {"nombre": "Maite", "carrera": "Software", "promedio": 8.9},
    {"nombre": "Angell", "carrera": "Informatica", "promedio": 8},
]

mapa_carreras = agrupar_por(listado_estudiantes, lambda item: item["carrera"])
print("Agrupados por carrera: ")
for carrera_nombre, alumnos in mapa_carreras.items():
    print(f" {carrera_nombre}:{[e['nombre'] for e in alumnos]}")




print("")
print("Ejercicio #13:")
"""
13.- Ejecutor Repetitivo con Estado Accesible: Crea ejecutar_y_rastrear(fn_tarea, n) que retorne un closure con el 
historial de resultados de haber ejecutado fn_tarea N veces.
"""
def ejecutar_y_rastrear(fn_tarea, n: int):
   
    registro_ejecuciones = [fn_tarea(i) for i in range(1, n + 1)]

    def obtener_historial():
        return registro_ejecuciones

    return obtener_historial

rastreador_lecturas = ejecutar_y_rastrear(lambda paso: f"Lectura #{paso}: {paso * 12.5} mA", 4) 
reporte_obtenido = rastreador_lecturas()

print("Todo el historial de ejecuciones realizadas: ")
for elemento in reporte_obtenido:
    print(" ", elemento)





print("")
print("Ejercicio #14:")
"""
14.- Compositor de Cadenas de Operaciones: Crea la HOF componer_dos(f, g) que devuelva un closure que aplique f(g(x)), 
permitiendo encadenar transformaciones complejas en línea.
"""
def componer_dos(f, g):
    def evaluar_composicion(val_entrada):
        return f(g(val_entrada))
    return evaluar_composicion

aplicar_descuento_20 = lambda precio: precio * 0.80
calcular_iva = lambda subtotal: subtotal * 1.15

evaluar_monto_final = componer_dos(calcular_iva, aplicar_descuento_20)
monto_inicial = 120
total_calculado = evaluar_monto_final(monto_inicial) 

print(f"Precio original ${monto_inicial}")
print(f"Precio final tras f(g(x))> ${total_calculado:.2f}")




print("")
print("Ejercicio #15:")
"""
15.- Decorador / HOF de Profiling y Auditoría: Crea la HOF auditar_ejecucion(fn_objetivo, fn_logger) que mida el tiempo 
y envíe el informe execution al closure/lambda de logging pasado por parámetro.
"""
def auditar_ejecucion(fn_objetivo, fn_logger):
    def envoltorio_auditoria(*args, **kwargs):
        tiempo_inicio = time.perf_counter()
        res_ejecucion = fn_objetivo(*args, **kwargs)
        tiempo_fin = time.perf_counter()
        lapso_ms = (tiempo_fin - tiempo_inicio) * 1000

        # Envía el informe estructurado a la función de logging inyectada
        fn_logger(fn_objetivo.__name__, lapso_ms, res_ejecucion)
        return res_ejecucion

    return envoltorio_auditoria


def suma_pesada(limite: int) -> int:
    return sum(range(limite))

log_auditoria = lambda fn_nom, tiempo, res: print(f"[AUDITORÍA] Función '{fn_nom}' | Tiempo: {tiempo:.4f} ms | Resultado: {res}")

medidor_tarea = auditar_ejecucion(suma_pesada, log_auditoria)
res_final = medidor_tarea(2_000_000)