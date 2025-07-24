suma = []

def area_triangulo(a, b):
    area = a * b/2
    return area

def impar_par(numero):
    if numero % 2 == 0:
        print("par")
    else:
        pass

while True:
    print("----Bienvenido al menu----")
    print("1. Ingresar numeros\n"
          "2. Calcular area de un triangulo\n"
          "3. Verificar si un numero es par o impar\n"
          "4. Calcular promedio de n calificaciones\n"
          "5. Conocer numero mayor y el menor\n"
          "6. salir del programa")
    select = input("Ingrese una opcion: ")
    match select:
        case "1":
            while True:
                print("1. Ingresar numero:\n"
                      "2. ver suma total, promedio, cuantos positivos y negativos \n"
                      "3. regresar al menu\n")
                select1 = input("Ingrese una opcion: ")
                match select1:
                    case "1":
                        num = int(input("Ingrese un numero: "))
                        suma.append(num)
                    case "2":
                        print(f"La suma total es = {sum(suma)}\n"
                              f"El promedio de = {sum(suma)/len(suma)} \n"
                              f"la cantidad de positivos es de = {len(suma) > 0} \n"
                              f"la cantidad de negativos es de = {len(suma) < 0} \n")
                        break
                    case "3":
                        print("Regresando al menu")
                        break
        case "6":
            print("Saliendo del programa")
            break