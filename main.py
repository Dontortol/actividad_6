suma = []

def ingresar_numeros():
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
                positivo = 0
                negativo = 0
                for i in suma:
                    if i < 0:
                        negativo += 1
                    else:
                        positivo += 1

                print(f"La suma total es = {sum(suma)}\n"
                      f"El promedio de = {sum(suma) / len(suma)} \n"
                      f"la cantidad de positivos = {positivo} \n"
                      f"la cantidad de negativos = {negativo} \n")

                break
            case "3":
                print("Regresando al menu")
                break
            case _:
                print("No se puede ingresar esa opcion")


def area_triangulo(a, b):
    area = a * b/2
    return area

def impar_par(numero):
    if numero % 2 == 0:
        print("Es par")
        return ''
    else:
        print("Es impar")
        return ''

def promedio():
    prome = []
    while True:
        print("\n1. ingresar calificacion \n"
              "2. Conocer el promedio \n"
              "3. Regresar al menu \n")
        prom_select = input("Ingrese una opcion: ")
        match prom_select:
            case "1":
                p = int(input("Ingrese un numero: "))
                prome.append(p)
            case "2":
                print(f"El promedio de las calificaciones es = {sum(prome)/len(prome)}")
            case "3":
                print("Regresando al menu \n")
                break
            case _:
                print("opcion no valida")

def mayor_menor():
    numeros = []
    while True:
        print("\n1. ingresar numero: \n"
              "2. ver cual es el mayor y el menor\n"
              "3. regresar al menu \n")
        mm_select = input("Ingrese una opcion: ")
        match mm_select:
            case "1":
                a = int(input("Ingrese un numero: "))
                numeros.append(a)
            case "2":
                print(f"El mayor de la calificacion es = {max(numeros)}\n"
                      f"El menor de la calificacion es = {min(numeros)}")
            case "3":
                print("Regresando al menu \n")
                break
            case _:
                print("opcion no valida")

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
            ingresar_numeros()
        case "2":
            print("Calculadora de area de un triangulo")
            a = int(input("Ingrese la base: "))
            b = int(input("Ingrese la altura: "))
            print(f"El area del triangulo es: {area_triangulo(a, b)}")
        case "3":
            print("Verificar si un numero es par o impar")
            numero = int(input("Ingrese un numero: "))
            print(f" {impar_par(numero)}")
        case "4":
            promedio()
        case "5":
            mayor_menor()
        case "6":
            print("Saliendo del programa")
            break