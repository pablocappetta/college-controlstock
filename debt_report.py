'''Ejercicio 1
A partir de las cuentas corrientes de un Banco, emitir un informe con las N cuentas de mayor saldo deudor
(saldo < 0) ordenadas por mayor nombre de sucursal y dentro de la misma sucursal ordenado por saldo
deudor de mayor a menor. El informe debe contener número de cuenta, sucursal y saldo. Considerar que
puede haber menos de N cuentas deudoras (e incluso ninguna). Por cada cuenta el archivo contiene los
siguientes datos separados por punto y coma. Además, algunos registros pueden no estar correctos
informando menos campos de los indicados, cuyo caso se deberá ignorar y crear un archivo de log con los
datos y número de registro original'''

'''Campos:
a. Nro. de cuenta corriente
b. Nombre Titular
c. Saldo
d. Sucursal'''  

from Funciones.files import *

#Funciones

def main():
    
    while True:
        
        try:
            n = int(input("Ingrese la cantidad de elementos que desea obtener del reporte: "))
            
            if n < 0:
                raise ValueError
            
            break
        
        except ValueError:
            
            continue

    try:
        
        log = open('log.txt',mode='w')
        archivo = open('info_cuentas.txt',mode='r')
        informe = open('informe_cuentas.txt',mode='w')
        listaDeudores = cargarDeudores(archivo,log)
        deudoresFiltrados = filtrarDeudores(listaDeudores,n)
        generarReporte(informe,deudoresFiltrados)   

    except OSError as msg:
        
        print("No se encuentra el archivo 'info_cuentas.txt'")
        log.write(str(msg)+'\n')

    finally:
        
        try:
            
            archivo.close()
            informe.close()
            log.close()
            
        except NameError as msg:
            
            log.write(str(msg)+'\n')
            log.close()

#Programa Principal
if __name__ == '__main__':
    main()
