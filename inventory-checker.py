'''Su empresa de desarrollo de software fue contactada para desarrollar un sistema de
control de stock. Una fábrica desea realizar un control de inventario de sus productos,
la empresa fabrica N productos diferentes y quiere mantener en stock un mínimo de
M unidades por producto. No tiene capacidad para almacenar más de X unidades por producto.

    a. Darle nombre a la fábrica e indicar qué producto produce.
    
    b. Se solicita simular una situación de stock actual para ello puede optar por lo siguiente:
    
        2. Simular tanto el código de producto de cuatro dígitos como la cantidad inicial
        en stock con un número al azar entre dos valores solicitados del teclado.
        
        Por supuesto que si el código ya existe se debe rechazar porque estamos creando el stock
        inicial y debe respetar las consignas iniciales respecto a las cantidades de stock.
        
    c. Se solicita ingresar un código de producto, luego ingresar la cantidad vendida.
    Si el código existe, actualizar su stock cuidando que existan unidades disponibles para vender,
    en caso de no alcanzar, emitir un mensaje. Si el código no existe, agregarlo como nuevo producto
    asignando un código nuevo de producto.
    
    d.Luego de cada cambio o como opción a ejecutar cuando lo requiera el usuario, se debe poder consular:
        
        1. Listado completo con los códigos y su cantidad correspondiente por pantalla ordenado por código de producto.
        
        2. Productos  y  su  cantidad  en  stock  que  se  encuentran  por  debajo  del  stock  mínimo ordenado por cantidad de stock mínimo.
        
        3. Posibilidad de ingresar un código de producto e informe cuál es su stock actual.'''

'''Nuestra empresa, Oculus S.A., produce elementos de mueblería tales como sillas,
sillones, puffs, mesas, escritorios.'''

import random

#Funciones
def randomValores(minimo):
    maximo = int(input("Valor máximo para el stock: ")) #Asumimos que de acuerdo al espacio en los depósitos los máximos tienen que ser diferentes por cuestiones de tamaño.
    while maximo < minimo or maximo < 0:
        maximo = int(input("El valor máximo no puede ser inferior al valor minimo o igual a 0. Por favor, intente nuevamente: "))
    valor = random.randint(minimo,maximo)
    return(valor)

def ventaChecker(listaProductos,listaStock,item,vendidos):
    print("------------------------------------------------------------------------------")
    print("-------------------------------VALIDADOR VENTAS-------------------------------")
    print("------------------------------------------------------------------------------")
    index = listaProductos.index(item) #Creamos una variable para especificar el indice para que sea mas legible
    if listaStock[index] >= vendidos:
        print("Stock disponible.")
        print("Existían",listaStock[index], "unidades disponibles del producto con ID",item,".")
        listaStock[index] = (listaStock[index] - vendidos)
        print("Ahora restan: ",listaStock[index],"unidades.")
        if listaStock[index] == 0:
            print("Por favor, comuníquese con su proveedor de inmediato para reponer stock.")
        print("------------------------------------------------------------------------------")
    else:
        print("Stock no disponible.")
        print("Existen",listaStock[index], "unidades disponibles del producto con ID",item," y no son suficientes para cubrir la venta. Por favor, comuníquese con el proveedor de inmediato.")
        print("------------------------------------------------------------------------------")

def stockChecker(listaProductos,listaStock,item):
    index = listaProductos.index(item)
    print("------------------------------------------------------------------------------")
    print("-------------------------------CONTROL DE STOCK-------------------------------")
    print("------------------------------------------------------------------------------")
    print("Verificando stock...")
    print("Existen",listaStock[index], "unidades disponibles del producto con ID",item,".")
    if listaStock[index] == 0:
        print("Por favor, comunicarse con el proveedor de inmediato.")
    print("------------------------------------------------------------------------------")

def minChecker(listaProductos,listaStock,listaStockMinimo):
    print("------------------------------------------------------------------------------")
    print("------------------------------CONTROL DE MÍNIMOS------------------------------")
    print("------------------------------------------------------------------------------")
    print("Verificando stock...")
    sortListas(listaStockMinimo,listaStock,listaProductos)
    aux = 0
    for i in range(len(listaProductos)):
        if listaStock[i] <= listaStockMinimo[i]:
            print("El stock del producto",listaProductos[i],", que consta de",listaStock[i],"unidades, igualó o se encuentra por debajo de la cantidad mínima definida:",listaStockMinimo[i])
            aux = aux + 1  
    if aux > 0:
        print("Por favor, comunicarse con el proveedor de inmediato.")
    else:
        print("No se detectó que ningún producto haya alcanzado el mínimo de existencias predefinidas.")
    print("------------------------------------------------------------------------------")

def sortListas(listaUno,listaDos,listaTres):
    for numPasada in range(len(listaUno)-1,0,-1):
        for i in range(numPasada):
            if listaUno[i]>listaUno[i+1]:
                temp = listaUno[i]
                listaUno[i] = listaUno[i+1]
                listaUno[i+1] = temp
                temp = listaDos[i]
                listaDos[i] = listaDos[i+1]
                listaDos[i+1] = temp
                temp = listaTres[i]
                listaTres[i] = listaTres[i+1]
                listaTres[i+1] = temp
    return(listaUno,listaDos,listaTres)

#Programa
listaProductos = []
listaStock = []
listaStockMinimo = []

print("")
print("------------------------------------------------------------------------------")
print("---------------------------------OCULUS S.A.----------------------------------")
print("------------------------------------------------------------------------------")
print("Bienvenido/a a EnterpriseManagement v2.0.3 - Diseñado con amor por UADE Alumni")
print("------------------------------------------------------------------------------")
print("---------------------------------R2D2C3P0SKY----------------------------------")
print("------------------------------------------------------------------------------")
print("")

producto = int(input("Ingrese el número del producto que desea agregar (4 dígitos): "))
while producto != -1:
    if producto > 9999 or producto < 1000:
        print("El código que ingresaste no es válido.")   
    else:
        if producto not in listaProductos:
            listaProductos.append(producto)
            minimo = int(input("Valor mínimo para el stock: "))
            while minimo < 1:
                minimo = int(input("El valor mínimo no puede ser inferior a 1. Por favor, intente nuevamente: "))
            listaStockMinimo.append(minimo)
            listaStock.append(randomValores(minimo))
        else:
            print("El código ya existe.")
            
    producto = int(input("Ingrese el número del producto que desea agregar (4 dígitos): "))

print("")
print("La base de datos ha sido actualizada.")
print("")
print("------------------------------------------------------------------------------")
print("IDs de los productos onboardeados: ",listaProductos)
print("Stock de los productos onboardeados: ",listaStock)
print("------------------------------------------------------------------------------")
print("")

productoVendido = int(input("Ingrese el número del producto que vendió o -1 para salir: "))

while productoVendido != -1:
    if (productoVendido > 9999) or (productoVendido < 1000):
        print("El código que ingresaste no es válido.")
    else:
        if productoVendido not in listaProductos: #Si el producto no se onboardeó anteriormente, se crea automáticamente una entrada con el nuevo ID especificado
            print("No existe un código relacionado a ese producto, por lo que se ha agregado a la lista de productos disponibles bajo el código especificado.")
            listaProductos.append(productoVendido)
            minimo = int(input("Valor mínimo para el stock: "))
            while minimo < 1:
                minimo = int(input("El valor mínimo no puede ser inferior a 1. Por favor, intente nuevamente: "))
            listaStockMinimo.append(minimo)
            listaStock.append(randomValores(minimo))
            print("")
            print("La base de datos ha sido actualizada.")
            print("")
            print("------------------------------------------------------------------------------")
            print("Lista de productos onboardeados actualizada:")
            print("------------------------------------------------------------------------------")
            print("IDs de los productos onboardeados: ",listaProductos)
            print("Stock de los productos onboardeados: ",listaStock)
            print("------------------------------------------------------------------------------")
            print("")
        
        cantidadVendida = int(input("Ingrese la cantidad de unidades vendidas del producto: "))
        
        while cantidadVendida <= 0:
            cantidadVendida = int(input("No podés vender 0 o unidades negativas. Por favor, intentá de nuevo: "))
    
        validarVenta = ventaChecker(listaProductos,listaStock,productoVendido,cantidadVendida) #Llama a la función para determinar si es posible o no concretar la venta
    
    productoVendido = int(input("Ingrese el número del producto que vendió o '-1' para continuar: "))


prodABuscar = int(input("Por favor, ingrese el ID del producto para el cual desea chequear la cantidad de existencias o '-1' para continuar: "))

while prodABuscar != -1:
    if prodABuscar in listaProductos:
        stockChecker(listaProductos,listaStock,prodABuscar)
    else:
        print("No se encontró ningún producto con el ID ingresado. Por favor, intente nuevamente: ")

    prodABuscar = int(input("Por favor, ingrese el ID del producto para el cual desea chequear la cantidad de existencias o '-1' para continuar: "))

faltantes = int(input("Por favor, ingrese '1' si quiere obtener un reporte de productos que se encuentran por debajo de los mínimos de existencias definidas anteriormente o '-1' para continuar: "))

while faltantes != -1:
    if faltantes == 1:
        minChecker(listaProductos,listaStock,listaStockMinimo)
    else:
        print("El número ingresado no es válido.")
        
    faltantes = int(input("Por favor, ingrese '1' si quiere obtener un reporte de productos que se encuentran por debajo de los mínimos de existencias definidas anteriormente o '-1' para continuar: "))

reporteGeneral = int(input("Por favor, ingrese '1' si quiere obtener un reporte final de los productos disponibles y sus existencias o '-1' para terminar con el programa: "))

while reporteGeneral != -1:
    if reporteGeneral == 1:
        print("")
        print("------------------------------------------------------------------------------")
        print("Lista final de productos disponibles: ",listaProductos)
        print("Lista final de existencias: ",listaStock)
        print("------------------------------------------------------------------------------")
        print("")
    else:
        print("El número ingresado no es válido.")
    
    reporteGeneral = int(input("Por favor, ingrese '1' si quiere obtener un reporte final de los productos disponibles y sus existencias o '-1' para terminar con el programa: "))
