#Programa tickets: Rodríguez Luis María Sol y Jazmín

import pickle, sys, os, random,json

def alta_ticket ():
    print (str(input("Ingrese su nombre, sector , asunto y problema.")))
    ticket= {'Nombre': str(input("Nombre: ")),  'Sector': str(input("\nSector: ")), 'Asunto': str(input("\nAsunto: ")),  'Problema': str(input("\nProblema: "))}
    nro_ticket= str(random.randrange(1000, 9999))
    print (f"\n=======SE GENERÓ EL SIGUIENTE TICKET=======\n\nN° de Ticket: {nro_ticket}.\n")
    for c,v in ticket.items ():
        print(c,v)
    print("\nRecuerde su número de ticket.\n")

    with open (nro_ticket, "wb") as f:
        pickle.dump(ticket,f)               

def buscar_ticket ():
    buscar= (input("\nIngrese nro. de ticket: "))

    with open (buscar, "rb") as f:
        ticket=pickle.load(f)
    
    print (f"\n=======EL N° DE TICKET SELECCIONADO CONTIENE LA SIGUIENTE INFORMACIÓN=======\n\nN° de Ticket: {buscar}.\n")
    for c,v in ticket.items ():
        print(c,v)

    
control=True
while control:

    print("=============Bienvenido=============\n\n        PROGRAMA DE TICKETS")

    opcion_elegida= int(input("\nElija una opcion:\n\n>> 1. Generar ticket. \n>> 2. Leer ticket. \n>> 3. Salir.\n\nSu opción es: "))

    if opcion_elegida == 1:
        
        consulta= ''   
        while consulta != 'n':
            alta_ticket ()
            respuesta= str(input("Desea realizar otro ticket? s/n: "))
            
            if respuesta!="n":
                print("Registre su nuevo ticket.\n")
                   
            else:
                break
        print ("\nRetornará al menú principal.\n")        
                
         
    elif opcion_elegida == 2:
        control3=''   
        while control3 != 'n':
            buscar_ticket()
            respuesta= str(input("\nDesea visualizar otro ticket? s/n: "))
            if respuesta!="n":
                print("Ingrese otro n° de ticket.\n")   
            else:
                break   
        print ("\nRetornará al menú principal.\n") 

    elif opcion_elegida == 3:
        opcion_salida= str(input("Seguro que deseas salir? (s/n): \n"))
        
        if opcion_salida=="s":
            sys.exit ()
        
        else: 
            print()

    else:
        print("Las opciones disponibles son: 1, 2 o 3.") 
        


      