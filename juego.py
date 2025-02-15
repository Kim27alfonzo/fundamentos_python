# Solicitar elección de los usuarios

usuario_1 = input ("Ingrese su nombre de jugador 1:")
usuario_2 = input ("Ingrese su nombre de jugador 2:") 

seleccion_usuario_1 = input(f"{usuario_1}, elige piedra, papel o tijera: ").lower()
seleccion_usuario_2 = input(f"{usuario_2}, elige piedra, papel o tijera: ").lower()

# Determinar el resultado
if usuario_1 == usuario_2:
    print("¡Es un empate!")
elif (seleccion_usuario_1 == "piedra" and seleccion_usuario_2 == "tijera") or \
     (seleccion_usuario_1 == "papel" and seleccion_usuario_2 == "piedra") or \
     (seleccion_usuario_1 == "tijera" and seleccion_usuario_2 == "papel"):

    mensaje = f"{usuario_1} ha ganado "
    if seleccion_usuario_1 == "piedra":
        mensaje += "porque la piedra aplasta la tijera"
    elif seleccion_usuario_1 == "papel":
        mensaje += "porque el papel envuelve la piedra"
    elif seleccion_usuario_1 == "tijera":
        mensaje += "porque la tijera corta el papel"
    print(mensaje)

else:
    mensaje = f"{usuario_2} ha ganado "
    if seleccion_usuario_2 == "piedra":
        mensaje += ", Piedra aplasta la tijera!!"
    elif seleccion_usuario_2 == "papel":
        mensaje += ", Papel envuelve la piedra!!"
    elif seleccion_usuario_2 == "tijera":
        mensaje += ", Tijera corta el papel!!"
    print(mensaje)