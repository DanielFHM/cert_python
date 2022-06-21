#  3.2.1.3 LABORATORIO: Lo esencial del bucle while - Adivina el número secreto 

secret_number = 777

print(
"""
+==================================+
| ¡Bienvenido a mi juego, muggle!  |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")

user_number = int(input("Ingresa el número: "))

while user_number != secret_number:
    print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
    user_number = int(input("Ingresa el número nuevamente: "))
print(secret_number, "¡Bien hecho, muggle! Eres libre ahora.")
