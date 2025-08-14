lista = [3, 8, 15, 22, 7, 10, 1, 14, 9, 4,1,1,1]


def repeticion_datos(lista):
    dato_a_buscar = int(input("que datos vas a ver para repetirse: "))
    apariciones = lista.count(dato_a_buscar)
    print(f"el dato a buscar {dato_a_buscar} aparece {apariciones} veces")

def mayor_menor_lista(lista):
    if lista != []:
        print(f"el numero menor es {min(lista)}")
        print(f"el numero mayor es {max(lista)}")

def promedio_numeros_pares(lista):
    sumatoria = 0
    contador = 0 
    for i in lista:
        if i % 2 == 0:
            sumatoria += i
            contador += 1
    if contador >= 1:
        resultado = sumatoria / contador
        print(f"el promedio de los numeros primos en la lista es {resultado}")
    else:
        print("no habia numeros primos para sacar un promedio")
       
promedio_numeros_pares(lista) 
def opciones_menu():
    print("menu opciones")
    print("-----------------")
    print("Encontrar cuantas veces se repite un dato")
    print("Encontrar el numero mayor y menor")
    print("Promedio de los numeros pares")
    print("Promedio entre el impar mayor y el impar menor")
    print("-----------------")
    
    return int(input("escoge una opcion porfavor: ")) #UNIT CASE

def opciones(opcion_escogida):
    match opcion_escogida:
        case 1:
            print(1)
        case 2:
            print(2)
        case 3:
            print(3)
        case 4:
            print(4)
        case other:
            print("no")
    

#opciones(opciones_menu())