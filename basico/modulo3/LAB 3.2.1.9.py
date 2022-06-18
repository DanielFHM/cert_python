#      3.2.1.9 LABORATORIO: La sentencia break - Atascado en un bucle

while True:
    word = input("¡Estás atrapado en un bucle infinito!\nIngresa la palabra secreta para dejar el bucle: ")
    if word == "chupacabra":
        break
print("¡Has dejado el bucle con éxito!")
