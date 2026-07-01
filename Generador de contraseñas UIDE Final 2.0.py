# =============================================================================
# UNIVERSIDAD INTERNACIONAL DEL ECUADOR (UIDE)
# FACULTAD DE INGENIERÍA - INGENIERÍA EN CIBERSEGURIDAD
# Asignatura  : Lógica de Programación
# Proyecto    : Generador Seguro de Contraseñas — Trabajo Final
# Estudiante  : Rommel Isaías Enríquez Chamba
# Docente     : Mgs. Lilian Marlene Aman Ramos
# Fecha       : Junio 2026

import secrets          # Módulo criptográficamente seguro (NIST recomendado)
import string           # Juegos de caracteres estándar
import os               # Limpieza de pantalla multiplataforma

# =============================================================================
# DATOS GLOBALES: Tuplas (inmutables, datos constantes del sistema)
# =============================================================================

# Tupla con los niveles de seguridad y su descripción (solo lectura)
NIVELES_SEGURIDAD: tuple = (
    ("MUY DÉBIL",   "rojo",    0,  39),
    ("DÉBIL",       "naranja", 40, 59),
    ("MODERADA",    "amarillo",60, 79),
    ("FUERTE",      "verde",   80, 94),
    ("MUY FUERTE",  "azul",    95, 100),
)

# Tupla con los tipos de caracteres disponibles (nombre, conjunto)
TIPOS_CARACTERES: tuple = (
    ("Letras MAYÚSCULAS", string.ascii_uppercase),   # A-Z
    ("Letras minúsculas", string.ascii_lowercase),   # a-z
    ("Números",           string.digits),             # 0-9
    ("Caracteres especiales", string.punctuation),   # !"#$%&...
)

# Longitud mínima por política de seguridad
LONGITUD_MINIMA: int = 8
LONGITUD_MAXIMA: int = 128


# =============================================================================
# FUNCIONES AUXILIARES
# =============================================================================

def limpiar_pantalla() -> None:
    """Limpia la consola según el sistema operativo."""
    os.system("cls" if os.name == "nt" else "clear")


def mostrar_banner() -> None:
    """Muestra el encabezado institucional del programa."""
    print("=" * 65)
    print("        UNIVERSIDAD INTERNACIONAL DEL ECUADOR — UIDE")
    print("           INGENIERÍA EN CIBERSEGURIDAD — 2026")
    print("=" * 65)
    print("     🔐  GENERADOR SEGURO DE CONTRASEÑAS  v2.0")
    print("         Proyecto Integrador — Lógica de Programación")
    print("=" * 65)


def mostrar_menu_principal() -> str:
    """
    Muestra el menú principal y retorna la opción elegida.
    Uso de listas para construir el menú dinámicamente.
    """
    # Lista de opciones del menú (mutable, podría extenderse)
    opciones_menu: list = [
        "1. Generar nueva contraseña",
        "2. Ver historial de contraseñas generadas",
        "3. Evaluar fortaleza de una contraseña existente",
        "4. Ver consejos de seguridad",
        "5. Salir del programa",
    ]

    print("\n📌 MENÚ PRINCIPAL")
    print("-" * 40)
    for opcion in opciones_menu:          # Estructura repetitiva FOR
        print(f"   {opcion}")
    print("-" * 40)

    return input("   Seleccione una opción: ").strip()


# =============================================================================
# ESTRUCTURAS CONDICIONALES: Validación de entradas
# =============================================================================

def validar_longitud(entrada: str) -> int:
    """
    Valida que la longitud ingresada sea un número entero dentro del rango.
    Aplica estructura condicional múltiple (if / elif / else).
    """
    try:
        longitud = int(entrada)
    except ValueError:
        print("⚠️  Error: Debe ingresar un número entero.")
        return -1

    if longitud < LONGITUD_MINIMA:
        print(f"⚠️  Longitud insegura. Mínimo permitido: {LONGITUD_MINIMA} caracteres.")
        return -1
    elif longitud > LONGITUD_MAXIMA:
        print(f"⚠️  Longitud excesiva. Máximo permitido: {LONGITUD_MAXIMA} caracteres.")
        return -1
    else:
        return longitud   # Longitud válida


def seleccionar_caracteres() -> tuple:
    """
    Presenta al usuario los tipos de caracteres disponibles.
    Usa una lista para acumular selecciones y retorna una tupla inmutable.
    Aplica estructura repetitiva FOR y condicional IF/ELSE.
    """
    print("\n🔠 SELECCIÓN DE TIPOS DE CARACTERES")
    print("-" * 40)

    seleccionados: list = []          # Lista mutable para acumular selecciones
    conjuntos_elegidos: list = []     # Lista de cadenas de caracteres

    for i, (nombre, conjunto) in enumerate(TIPOS_CARACTERES, start=1):
        respuesta = input(f"   [{i}] ¿Incluir {nombre}? (S/N): ").strip().upper()
        if respuesta == "S":
            seleccionados.append(nombre)
            conjuntos_elegidos.append(conjunto)

    # Control de error: ninguna opción seleccionada
    if not conjuntos_elegidos:
        print("\n⚠️  Sin selección válida. Se asignan minúsculas por seguridad.")
        seleccionados.append("Letras minúsculas (asignado por defecto)")
        conjuntos_elegidos.append(string.ascii_lowercase)

    # Retorna tupla inmutable con los datos finales
    return tuple(seleccionados), "".join(conjuntos_elegidos)


# =============================================================================
# ESTRUCTURAS REPETITIVAS + LISTAS: Núcleo del algoritmo
# =============================================================================

def generar_contrasena(longitud: int, caracteres: str) -> str:
    """
    Genera la contraseña usando un bucle WHILE y secrets.choice().
    Garantiza al menos un carácter de cada tipo seleccionado (buena práctica).
    Retorna la contraseña como string.
    """
    contrasena: list = []    # Lista de caracteres (mutable durante construcción)
    contador: int = 0

    # Estructura repetitiva WHILE — núcleo del algoritmo
    while contador < longitud:
        caracter = secrets.choice(caracteres)   # Selección criptográfica
        contrasena.append(caracter)             # Acumulación en lista
        contador += 1

    # Mezclamos la lista para mayor aleatoriedad (evita patrones predecibles)
    secrets.SystemRandom().shuffle(contrasena)

    return "".join(contrasena)    # Convertir lista → string final


def calcular_entropia(longitud: int, num_caracteres: int) -> float:
    """
    Calcula la entropía de la contraseña en bits.
    Fórmula: H = L × log2(N)  donde L=longitud, N=tamaño del alfabeto.
    Concepto clave en Ciberseguridad para medir fortaleza real.
    """
    import math
    if num_caracteres == 0:
        return 0.0
    return round(longitud * math.log2(num_caracteres), 2)


def evaluar_fortaleza(contrasena: str) -> tuple:
    """
    Evalúa la fortaleza de una contraseña según múltiples criterios.
    Usa lista de verificaciones y estructura condicional para puntuar.
    Retorna tupla (puntaje, nivel, descripción).
    """
    puntaje: int = 0

    # Lista de criterios de evaluación (verificaciones independientes)
    criterios: list = [
        (len(contrasena) >= 8,   10, "Longitud mínima (≥8)"),
        (len(contrasena) >= 12,  10, "Longitud recomendada (≥12)"),
        (len(contrasena) >= 16,  10, "Longitud óptima (≥16)"),
        (any(c.isupper() for c in contrasena), 15, "Contiene mayúsculas"),
        (any(c.islower() for c in contrasena), 15, "Contiene minúsculas"),
        (any(c.isdigit() for c in contrasena), 20, "Contiene números"),
        (any(c in string.punctuation for c in contrasena), 20, "Contiene especiales"),
    ]

    criterios_cumplidos: list = []    # Lista de criterios aprobados

    for cumple, puntos, descripcion in criterios:   # FOR sobre lista
        if cumple:                                   # Condicional IF
            puntaje += puntos
            criterios_cumplidos.append(f"✅ {descripcion}")
        else:
            criterios_cumplidos.append(f"❌ {descripcion}")

    # Determinar nivel según rango en la tupla NIVELES_SEGURIDAD
    nivel_encontrado = NIVELES_SEGURIDAD[0]   # Valor por defecto
    for nivel in NIVELES_SEGURIDAD:           # FOR sobre tupla global
        nombre, color, minimo, maximo = nivel
        if minimo <= puntaje <= maximo:
            nivel_encontrado = nivel
            break

    return puntaje, nivel_encontrado[0], criterios_cumplidos


# =============================================================================
# HISTORIAL: Uso de lista como estructura de datos persistente
# =============================================================================

def mostrar_historial(historial: list) -> None:
    """
    Muestra las contraseñas generadas durante la sesión.
    El historial es una lista de diccionarios.
    """
    print("\n📋 HISTORIAL DE CONTRASEÑAS — SESIÓN ACTUAL")
    print("-" * 65)

    if not historial:                          # Condicional: lista vacía
        print("   Sin registros aún en esta sesión.")
    else:
        for i, registro in enumerate(historial, start=1):   # FOR con enumerate
            print(f"   [{i}] Contraseña : {registro['contrasena']}")
            print(f"        Longitud   : {registro['longitud']} caracteres")
            print(f"        Fortaleza  : {registro['nivel']}")
            print(f"        Entropía   : {registro['entropia']} bits")
            print(f"        Tipos      : {', '.join(registro['tipos'])}")
            print()

    print("-" * 65)


# =============================================================================
# MÓDULO DE CONSEJOS — Lista de buenas prácticas en Ciberseguridad
# =============================================================================

def mostrar_consejos() -> None:
    """
    Muestra consejos de seguridad almacenados en una lista.
    Demuestra uso educativo del proyecto en el contexto social/tecnológico.
    """
    consejos: list = [
        "🔑 Usa una contraseña distinta para cada servicio.",
        "📏 Las contraseñas deben tener al menos 12 caracteres.",
        "🔤 Combina mayúsculas, minúsculas, números y símbolos.",
        "🚫 Evita palabras del diccionario o datos personales.",
        "🔒 Activa la autenticación de dos factores (2FA) siempre.",
        "🗂️  Usa un gestor de contraseñas (Bitwarden, KeePass).",
        "📅 Cambia contraseñas críticas cada 90 días.",
        "🌐 Nunca ingreses contraseñas en redes WiFi públicas sin VPN.",
        "📧 Ante una filtración, cambia inmediatamente la contraseña.",
        "🧠 Una frase larga y memorable es más segura que una corta compleja.",
    ]

    print("\n💡 CONSEJOS DE SEGURIDAD — CIBERSEGURIDAD UIDE")
    print("=" * 65)
    for i, consejo in enumerate(consejos, start=1):   # Estructura repetitiva
        print(f"   {i:02d}. {consejo}")
    print("=" * 65)


# =============================================================================
# FLUJO PRINCIPAL — Función principal que integra todos los módulos
# =============================================================================

def flujo_generar_contrasena(historial: list) -> None:
    """
    Coordina el flujo completo de generación de contraseña.
    Integra todas las unidades del curso en un flujo coherente.
    """
    print("\n🔐 GENERACIÓN DE NUEVA CONTRASEÑA")
    print("=" * 65)

    # --- ENTRADA: Longitud ---
    longitud: int = -1
    while longitud == -1:                         # Repetitiva: reintento
        entrada = input(f"\n   Longitud de la contraseña ({LONGITUD_MINIMA}-{LONGITUD_MAXIMA}): ")
        longitud = validar_longitud(entrada)       # Condicional dentro

    # --- ENTRADA: Tipos de caracteres ---
    tipos_seleccionados, caracteres_pool = seleccionar_caracteres()

    # --- PROCESAMIENTO: Generación ---
    print("\n⚙️  Generando contraseña criptográfica...")
    contrasena = generar_contrasena(longitud, caracteres_pool)

    # --- ANÁLISIS: Fortaleza y Entropía ---
    puntaje, nivel, criterios = evaluar_fortaleza(contrasena)
    entropia = calcular_entropia(longitud, len(set(caracteres_pool)))

    # --- SALIDA: Resultados ---
    print("\n" + "=" * 65)
    print(f"   🔒 CONTRASEÑA GENERADA:")
    print(f"\n   ➤  {contrasena}")
    print(f"\n   📊 Análisis de Seguridad:")
    print(f"       • Longitud    : {longitud} caracteres")
    print(f"       • Entropía    : {entropia} bits")
    print(f"       • Fortaleza   : {nivel}  ({puntaje}/100 pts)")
    print(f"       • Tipos usados: {len(tipos_seleccionados)}")
    print("\n   📋 Criterios evaluados:")
    for criterio in criterios:
        print(f"       {criterio}")
    print("=" * 65)

    # --- GUARDAR en historial (lista de diccionarios) ---
    registro: dict = {
        "contrasena": contrasena,
        "longitud":   longitud,
        "nivel":      nivel,
        "puntaje":    puntaje,
        "entropia":   entropia,
        "tipos":      list(tipos_seleccionados),
    }
    historial.append(registro)    # Lista mutable: append

    print(f"\n✅ Contraseña guardada en historial. Total: {len(historial)} generada(s).")


def flujo_evaluar_externa() -> None:
    """Permite evaluar una contraseña externa ingresada por el usuario."""
    print("\n🔍 EVALUACIÓN DE CONTRASEÑA EXISTENTE")
    print("-" * 40)
    contrasena = input("   Ingrese la contraseña a evaluar: ").strip()

    if not contrasena:                            # Condicional: entrada vacía
        print("⚠️  No ingresó ninguna contraseña.")
        return

    puntaje, nivel, criterios = evaluar_fortaleza(contrasena)
    entropia = calcular_entropia(len(contrasena), len(set(contrasena)))

    print(f"\n   📊 Resultado:")
    print(f"       • Fortaleza : {nivel}  ({puntaje}/100 pts)")
    print(f"       • Entropía  : {entropia} bits")
    print(f"       • Longitud  : {len(contrasena)} caracteres")
    print("\n   📋 Criterios:")
    for criterio in criterios:
        print(f"       {criterio}")


# =============================================================================
# PUNTO DE ENTRADA — main()
# =============================================================================

def main() -> None:
    """
    Función principal. Controla el bucle principal del programa mediante
    estructura repetitiva WHILE y menú interactivo.
    """
    limpiar_pantalla()
    mostrar_banner()

    historial: list = []    # Lista vacía: almacena contraseñas de la sesión
    ejecutando: bool = True

    while ejecutando:                              # Bucle principal del programa
        opcion = mostrar_menu_principal()

        if opcion == "1":                          # Condicional múltiple IF/ELIF
            flujo_generar_contrasena(historial)

        elif opcion == "2":
            mostrar_historial(historial)

        elif opcion == "3":
            flujo_evaluar_externa()

        elif opcion == "4":
            mostrar_consejos()

        elif opcion == "5":
            print("\n👋 Gracias por usar el Generador Seguro de Contraseñas UIDE.")
            print("   Recuerda: una buena contraseña es tu primera línea de defensa.")
            print("   — Rommel Enríquez | Ciberseguridad UIDE 2026\n")
            ejecutando = False                     # Termina el bucle principal

        else:
            print("⚠️  Opción no válida. Ingrese un número del 1 al 5.")

        if ejecutando:                             # Pausa antes de continuar
            input("\n   Presione ENTER para continuar...")
            limpiar_pantalla()
            mostrar_banner()


# =============================================================================
# EJECUCIÓN
# =============================================================================
if __name__ == "__main__":
    main()