# =================================================================
# UNIVERSIDAD INTERNACIONAL DEL ECUADOR (UIDE)
# FACULTAD DE INGENIERÍA - INGENIERÍA EN CIBERSEGURIDAD
# Asignatura: Lógica de Programación
# Proyecto: Generador Seguro de Contraseñas (Trabajo Autónomo 2)
# Estudiante: Rommel Isaías Enríquez Chamba
# =================================================================

import secrets  # Biblioteca criptográficamente segura (Mandatorio en Ciberseguridad)
import string

def generar_contrasena():
    print("==================================================")
    print("      GENERADOR SEGURO DE CONTRASEÑAS - UIDE     ")
    print("==================================================\n")
    
    # -------------------------------------------------------------
    # FASE 1: Captura de Requerimientos (Entrada de Datos)
    # -------------------------------------------------------------
    longitud_usuario = int(input("1. Ingrese la longitud de la contraseña (Mínimo 8): "))
    
    # Estructura Condicional: Validación de la longitud mínima
    if longitud_usuario < 8:
        print("⚠️ [SEGURIDAD] Longitud insegura. Se ha forzado a 8 caracteres por defecto.")
        longitud_usuario = 8

    # Inicialización de la variable de caracteres (Misma lógica de Raptor)
    caracteres_permitidos = ""
    
    print("\n--- Selección de Componentes (Responda 'S' o 'N') ---")
    quiere_mayus = input("¿Deseas incluir letras MAYÚSCULAS? (S/N): ").strip().upper()
    quiere_minus = input("¿Deseas incluir letras minúsculas? (S/N): ").strip().upper()
    quiere_num   = input("¿Deseas incluir Números? (S/N): ").strip().upper()
    quiere_esp   = input("¿Deseas incluir Caracteres Especiales? (S/N): ").strip().upper()

    # Estructuras Condicionales de Selección Independientes
    if quiere_mayus == "S":
        caracteres_permitidos += string.ascii_uppercase  # ABCDEFGHIJKLMNOPQRSTUVWXYZ
    if quiere_minus == "S":
        caracteres_permitidos += string.ascii_lowercase  # abcdefghijklmnopqrstuvwxyz
    if quiere_num == "S":
        caracteres_permitidos += string.digits           # 0123456789
    if quiere_esp == "S":
        caracteres_permitidos += string.punctuation      # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

    # -------------------------------------------------------------
    # FASE 2: CONTROL DE ERRORES (Idéntico a tu Diagrama de Raptor)
    # -------------------------------------------------------------
    # Si la variable está vacía porque todo se configuró en 'N'
    if caracteres_permitidos == "":
        print("\n⚠️ ADVERTENCIA: ¡No has seleccionado ninguna opción válida!")
        print("-> Por defecto y seguridad, el sistema asignará letras minúsculas.")
        caracteres_permitidos = string.ascii_lowercase  # Asignación segura automática

    # -------------------------------------------------------------
    # FASE 3: El Núcleo del Algoritmo (Estructura Repetitiva / Bucle)
    # -------------------------------------------------------------
    contrasena_final = ""  
    contador = 0           
    
    # Bucle secuencial idéntico al bloque Loop de Raptor
    while contador < longitud_usuario:
        caracter_azar = secrets.choice(caracteres_permitidos)
        contrasena_final += caracter_azar
        contador += 1

    # -------------------------------------------------------------
    # FASE 4: Salida del Sistema
    # -------------------------------------------------------------
    print("\n==================================================")
    print(f"🔒 Contraseña Criptográfica Generada: {contrasena_final}")
    print("==================================================\n")

if __name__ == "__main__":
    generar_contrasena()