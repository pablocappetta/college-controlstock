def filtrarDeudores(listaDeudores,cantidad):
    listaDeudores.sort(key=lambda x: x[1])
    
    if cantidad < len(listaDeudores):
        listaDeudores = listaDeudores[:cantidad]
    
    listaOrdenada = sorted(listaDeudores, key=lambda x: (x[2], -x[1]), reverse = True)
    
    return listaOrdenada
    
def generarReporte(informe,listaOrdenada):

    for valor in listaOrdenada:
        for i in range(0,3):
            informe.write(str(valor[i]))
            if i == 2:
                informe.write('\n')
            
            else:
                informe.write(";")    

def cargarDeudores(archivo,log):
    
    listaDeudores = []
    auxLista = []
    
    for linea in archivo:
        
        valores = linea.split(";")

        if len(valores) != 4:
            log.write(f'Este conjunto tiene más o menos de 4 elementos: {linea}')
            continue
        
        else:
            try:
                if float(valores[2]) < 0:
                    cuenta = int(valores[0])
                    saldo = float(valores[2])
                    sucursal = int(valores[3])
                    auxLista.append(cuenta)
                    auxLista.append(saldo)
                    auxLista.append(sucursal)
                    listaDeudores.append(auxLista)
                    auxLista = []
                    continue
                
                #informe.write(str(linea.split(";")[0])+';'+str(linea.split(";")[2])+';'+str(linea.split(";")[3]))
            
            except (ValueError,IndexError) as msg:
                log.write('Existen elementos que no corresponden. '+str(msg)+'\n')
        
    return listaDeudores
