#   DICCIONARIOS
#       los diccionarios en python son los JSON de JavaScript
persona = {
    'nombre': 'Jhonatan Ossa',
    'edad': 32,
    'estatura': 1.80,
    'leGustaFutbol': False
}
print(persona)
print(persona['leGustaFutbol'])
print(persona.get('edad'))
persona['carrera'] = 'ingeniero'
print(persona)

opcion = -1
productos=[]
while(opcion!=0):
    print("**************")
    print("Digitar 1 para ingresar un producto")
    print("Digitar 2 para mostrar los productos ingresados")
    print("Digitar 3 para buscar por código de producto y editar su precio")
    print("Digitar 4 para buscar por código de producto y eliminarlo")
    opcion = int(input("Digite una opción: "))
    if (opcion == 1):
        producto = {}
        producto['codigo'] = input("Digita el codigo del producto: ")
        producto['nombre'] = input("Digita el nombre del producto: ")
        producto['costo'] = int(input("Digita el costo del producto: "))
        productos.append(producto)
        # noDuplicado = input("Digita el codigo del producto: ")
        # for producto in productos:
        #     print(producto['codigo'])
        #     print(noDuplicado)
        #     if(producto['codigo'] == noDuplicado):
        #         print("Codigo ya existe, intente de nuevo")
        #         opcion = 1
        #     else:
        #         producto['nombre'] = input("Digita el nombre del producto: ")
        #         producto['costo'] = int(input("Digita el costo del producto: "))
        #         productos.append(producto)
    elif (opcion==2):
        print(productos)
    elif (opcion==3):
        bandera = True
        buscarCodigo = input("Digite el codigo del producto a editar precio: ")
        for producto in productos:
            if (producto['codigo'] == buscarCodigo):
                producto['costo'] = int(input("Ingrese el nuevo precio: "))
                bandera = True
                break
            else: 
                bandera = False
        if(bandera == False):
            print("Producto no encontrado")  
    elif (opcion==4):
        bandera = True
        buscarCodigo = input("Digite el codigo del producto a eliminar: ")
        for producto in productos:
            if (producto['codigo'] == buscarCodigo):
                producto['costo'] = int(input("Ingrese el nuevo precio: "))
                bandera = True
                break
            else: 
                bandera = False
        if(bandera == False):
            print("Producto no encontrado")  

    else:
        print("Has salido")