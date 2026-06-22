# 🔒 Proyecto: Generador Seguro de Contraseñas

## 👨‍🎓 Datos del Estudiante
* **Universidad:** Universidad Internacional del Ecuador (UIDE)
* **Facultad:** Ingeniería en Ciberseguridad
* **Asignatura:** Lógica de Programación
* **Estudiante:** Rommel Isaías Enríquez Chamba

---

## 📝 1. Descripción del Programa
Este programa genera contraseñas aleatorias y criptográficamente seguras adaptadas a las necesidades del usuario. Solicita una longitud específica (mínimo de 8 caracteres por seguridad) y permite elegir qué tipos de caracteres incluir (mayúsculas, minúsculas, números y símbolos). Cuenta con un sistema de control de errores que impide que el programa falle si el usuario deniega todas las opciones.

---

## 📥 2. Especificaciones de Entrada
* **longitud_usuario (Entero):** Cantidad total de caracteres.
* **quiere_mayus (Texto):** Opción ("S" o "N") para incluir mayúsculas.
* **quiere_minus (Texto):** Opción ("S" o "N") para incluir minúsculas.
* **quiere_num (Texto):** Opción ("S" o "N") para incluir números.
* **quiere_esp (Texto):** Opción ("S" o "N") para incluir caracteres especiales.

---

## 📤 3. Especificaciones de Salida
* **contrasena_final (Texto):** Una cadena de texto aleatoria que combina los caracteres seleccionados con la longitud requerida.

---

## 🛠️ 4. Diccionario de Variables

| Nombre de la Variable | Tipo de Dato | Propósito / Función |
| :--- | :--- | :--- |
| `longitud_usuario` | Entero (`int`) | Guarda el tamaño de la contraseña. |
| `quiere_mayus` | Texto (`str`) | Almacena si desea letras MAYÚSCULAS. |
| `quiere_minus` | Texto (`str`) | Almacena si desea letras minúsculas. |
| `quiere_num` | Texto (`str`) | Almacena si desea dígitos numéricos. |
| `quiere_esp` | Texto (`str`) | Almacena si desea símbolos especiales. |
| `caracteres_permitidos` | Texto (`str`) | Junta todos los caracteres válidos elegidos. |
| `contrasena_final` | Texto (`str`) | Aquí se construye el resultado final. |
| `contador` | Entero (`int`) | Controla las vueltas del bucle repetitivo. |

---

## 🎥 5. Enlaces de los Videos Explicativos
* **Video 1 (Explicación del Diagrama en Raptor):https://bit.ly/4fVZPU7 
* **Video 2 (Explicación y Demostración del Código en Python):https://bit.ly/4b3fhdA
