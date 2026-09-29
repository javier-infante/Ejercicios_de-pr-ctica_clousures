#Nombre: Infante Lozano Javier Alonso


from functools import reduce
import math

print("")
print("Ejercicio #16:")
"""
16.- Validador Compuesto de Reglas de Negocio: Crea crear_validador_multiple(*lambdas_criterios) 
que retorne un closure que evalúe si un objeto cumple todas las reglas pasadas como argumento.
"""
def crear_validador_multiple(*lambdas_criterios):
    def verificar_cumplimiento(entidad: dict) -> bool:
        return all(regla(entidad) for regla in lambdas_criterios)
    return verificar_cumplimiento

es_mayor_edad = lambda u: u.get("edad", 0) >= 18
ingresos_suficientes = lambda u: u.get("ingresos", 0) >= 1200
buen_historial = lambda u: u.get("score_crediticio", 0) >= 700

evaluar_solicitante = crear_validador_multiple(es_mayor_edad, ingresos_suficientes, buen_historial)

usr_aprobado = {"edad": 24, "ingresos": 1500, "score_crediticio": 752}
usr_rechazado = {"edad": 19, "ingresos": 900, "score_crediticio": 710}

print("Solicitud #1 Aprobada?: ", evaluar_solicitante(usr_aprobado))
print("Solicitud #2 Aprobada?: ", evaluar_solicitante(usr_rechazado))




print("")
print("Ejercicio #17:")
"""
17.- Caché con Expiración o Tamaño Máximo (Memoización Profesional): Crea la HOF 
memoizar_avanzado(fn_costosa, max_items) que retorne un closure controlando el estado 
privado de una memoria caché con límite de capacidad.
"""
def memoizar_avanzado(fn_costosa, max_items: int = 3):
    memoria = {}
    cola_llaves = []

    def operacion_memoizada(*args):
        if args in memoria:
            print(f"[CACHE HIT] recuperando para  {args}")
            return memoria[args]

        print(f"[CALCULANDO] ejecutando funcion para  {args}")
        res_calculado = fn_costosa(*args)

        if len(memoria) >= max_items:
            llave_expulsada = cola_llaves.pop(0)
            del memoria[llave_expulsada]
            print(f"[DESALOJO] cache llena, se eliminó la clave {llave_expulsada}")

        memoria[args] = res_calculado
        cola_llaves.append(args)
        return res_calculado

    return operacion_memoizada

def calcular_fact(n: int) -> int:
    return math.factorial(n)

evaluar_factorial = memoizar_avanzado(calcular_fact, max_items=2)
print("Resultado #5!: ", evaluar_factorial(5))
print("Resultado #5! (reintento): ", evaluar_factorial(5))
print("Resultado #6!: ", evaluar_factorial(6))
print("Resultado #7! (fuerza desalojo de 5): ", evaluar_factorial(7))
print("Resultado #5! (de nuevo vuelve a caluclar por desalojo previo): ", evaluar_factorial(5))




print("")
print("Ejercicio #18:")
"""
18.- Motor de Pipeline Secuencial (Currying / Middleware): Crea crear_pipeline(*funciones_transformacion) 
que permita pasar un dato inicial y hacerlo fluir en orden a través de todas las lambdas/funciones del pipeline.
"""
def crear_pipeline(*funciones_transformacion):
    def ejecutar_flujo(valor_inicial):
        return reduce(lambda val_actual, fn_paso: fn_paso(val_actual), funciones_transformacion, valor_inicial)
    return ejecutar_flujo


quitar_espacios_ext = lambda texto: texto.strip()
pasar_a_minusculas = lambda texto: texto.lower()
sustituir_espacios = lambda texto: texto.replace(" ", "_")
limpiar_cadena_texto = crear_pipeline(quitar_espacios_ext, pasar_a_minusculas, sustituir_espacios)

cadena_bruta = " Sistema de distribucion y redes 2026 "
cadena_limpia = limpiar_cadena_texto(cadena_bruta)

print("Texto original: ", f"'{cadena_bruta}'")
print("Texto procesado por Pipeline: ", cadena_limpia)




print("")
print("Ejercicio #19:")
"""
19.- Sistema Pub/Sub (Event Listener con HOFs y Closures): Crea crear_sistema_eventos() que 
devuelva un closure gestor capaz de registrar suscriptores (lambdas) y emitir eventos notificando a cada uno.
"""
def crear_sistema_eventos():
    tabla_suscripciones = {}

    def administrar_eventos(tipo_accion: str, nombre_evento: str, handler_o_payload = None):
        nonlocal tabla_suscripciones

        if tipo_accion == "suscribir":
            if nombre_evento not in tabla_suscripciones:
                tabla_suscripciones[nombre_evento] = []
            tabla_suscripciones[nombre_evento].append(handler_o_payload)
            return f"Suscripcion registrada en {nombre_evento}"

        elif tipo_accion == "emitir":
            oyentes = tabla_suscripciones.get(nombre_evento, [])
            respuestas = [listener(handler_o_payload) for listener in oyentes]
            return respuestas

    return administrar_eventos

event_bus = crear_sistema_eventos()


event_bus("suscribir", "usuario_creado", lambda u: print(f"   [LOG]: Usuario {u['email']} guardado en la Base de Datos"))
event_bus("suscribir", "usuario_creado", lambda u: print(f"  [EMAIL]: Correo de ingreso y bienvenida a {u['email']}"))

print("Emitiendo evento 'usuario_creado': ")
event_bus("emitir", "usuario_creado", {"email": "davidguale@upse.edu.ec"})




print("")
print("Ejercicio #20:")
"""
20.- Mini-Query Engine sobre Listas de Objetos: Crea crear_consultor(campo) que devuelva una HOF para generar 
filtros dinámicos sobre listas de diccionarios/objetos mediante expresiones lambda complejas.
"""
def crear_consultor(campo: str):
    def construir_filtro(predicado_lambda):
        def filtrar_lista(dataset: list) -> list:
            return [elemento for elemento in dataset if predicado_lambda(elemento.get(campo))]
        return filtrar_lista
    return construir_filtro

lista_servidores = [
    {"ip": "192.168.1.10", "cpu_uso": 85, "ram_gb": 32, "estado": "activo"},
    {"ip": "192.168.1.11", "cpu_uso": 42, "ram_gb": 16, "estado": "inactivo"},
    {"ip": "192.168.1.12", "cpu_uso": 94, "ram_gb": 64, "estado": "activo"},
    {"ip": "192.168.1.13", "cpu_uso": 15, "ram_gb": 8, "estado": "activo"}
]

consultor_metrica_cpu = crear_consultor("cpu_uso")
filtro_alto_consumo = consultor_metrica_cpu(lambda uso: uso is not None and uso > 80)

nodos_sobrecargados = filtro_alto_consumo(lista_servidores)

print("Servidores con CPU crítico (> 80%):")
for servidor in nodos_sobrecargados:
    print(f"  Ip: {servidor['ip']} | CPU: {servidor['cpu_uso']}% | Ram: {servidor['ram_gb']}GB")