def mostrar_menu():
    print('Seleccione el proceso que desea aplicar')
    print('1: Ingresar puntuación y comentario')
    print('2: Comprueba los resultados obtenidos hasta ahora.')
    print('3: Finalizar')

def obtener_puntuacion():
    while True:
        print('Por favor, introduzca una puntuación en una escala de 1 a 5')
        point = input()
        
        if point.isdecimal():
            point = int(point)
            if 1 <= point <= 5:  # Verifica si la puntuación está en el rango de 1 a 5
                return point
            else:
                print('Por favor, introduzca un valor entre 1 y 5')
        else:
            print('Por favor, introduzca la puntuación en números')

def ingresar_comentario():
    print('Por favor, introduzca un comentario')
    return input()

def guardar_puntuacion_y_comentario(point, comment):
    post = f'punto: {point} comentario: {comment}'
    with open("data.txt", 'a') as file_pc:
        file_pc.write(f'{post}\n')

def mostrar_resultados():
    print('Resultados hasta la fecha:')
    with open("data.txt", 'r') as read_file:
        print(read_file.read())

def proceso_ingreso():
    point = obtener_puntuacion()
    comment = ingresar_comentario()
    guardar_puntuacion_y_comentario(point, comment)

def proceso_menu():
    while True:
        mostrar_menu()
        num = input()
        
        if num.isdecimal():
            num = int(num)
            if num == 1:
                proceso_ingreso()
            elif num == 2:
                mostrar_resultados()
            elif num == 3:
                print('Finalizando')
                break
            else:
                print('Por favor, introduzca un número del 1 al 3')
        else:
            print('Por favor, introduzca un número del 1 al 3')

# Ejecutar el programa
proceso_menu()
