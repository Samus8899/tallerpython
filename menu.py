from itertools import product
from math import prod


print("***MENU***")
print("1. AGREGAR PRODUCTO")
print("2. MOSTRAR PRODUCTOS")
print("3. EDITAR PRODUCTO")
print("4. ELIMINAR PRODUCTO")
print("0. SALIR")
opcion=100
productos=[]



while(opcion!=0):
    producto={}
    opcion=int(input("DIGITE UNA OPCION DEL MENU: "))
    if(opcion==1):
        producto['codigo']=int(input("DIGITE EL CODIGO DE PRODUCTO: "))
        producto['nombre']=input("DIGITE UN NOMBRE PARA EL PRODUCTO: ")
        producto['precio']=input("DIGITE UN PRECIO PARA EL PRODUCTO: ")
        productos.append(producto)
        print("PRODUCTO AGREGADO CON EXITO")
    elif(opcion==2):
        print("MOSTRANDO PRODUCTOS")
        print(productos)
    elif(opcion==3):
        cd=int(input("DIGITE CODIGO DE PRODUCTO A EDITAR: "))
        for i in productos:
            if(i['codigo']==cd):
                nuevo=input("DIGITE EL NUEVO PRECIO DEL PRODUCTO: ")
                i['precio']=nuevo
                print("PRECIO MODIFICADO CON EXITO")
            else:
                print("EL CODIGO DE PRODUCTO NO EXISTE")
    elif(opcion==4):
         cd=int(input("DIGITE EL CODIGO DEL PRODUCTO A ELIMINAR: "))
         for i in productos:
            if(i['codigo']==cd):
                productos.remove(i)
else:
    print("FIN")