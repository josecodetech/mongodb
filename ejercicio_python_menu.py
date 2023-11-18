import pymongo
# conexion
cliente = pymongo.MongoClient("mongodb://localhost:27017/")
# bd
db = cliente['ventas']
# coleccion
coleccion = db['articulos']

while True:
    print("Menu principal: ")
    print("1. Listar Articulos")
    print("2. Agregar Articulo")
    print("3. Editar Articulo")
    print("4. Borrar Articulo")
    print("5. Salir")
    opcion = input("Selecciona una opcion: ")
    if opcion == "1":
        documentos = coleccion.find({})
        print("Articulos disponibles : ")
        for doc in documentos:
            print(doc)
    elif opcion == "2":
        nombre = input("Nombre del articulo: ")
        precio = float(input("Precio: "))
        stock = int(input("Stock: "))
        nuevo = {"nombre":nombre,"precio":precio,"stock":stock}
        coleccion.insert_one(nuevo)
        print("Articulo insertado")
    elif opcion == "3":
        nombre = input("Nombre del articulo a modificar: ")
        filtro = {"nombre": nombre}
        nuevo_nombre = input("Nuevo nombre: ")
        nuevo_precio = float(input("Nuevo precio: "))
        nuevo_stock = int(input("Nuevo stock: "))
        nuevos_valores = {"$set":{"nombre":nuevo_nombre,"precio":nuevo_precio,"stock":nuevo_stock}}
        coleccion.update_one(filtro,nuevos_valores)
        print("Articulo actualizado")
    elif opcion == "4":
        nombre = input("Nombre del articulo a eliminar: ")
        filtro = {"nombre": nombre}
        coleccion.delete_one(filtro)
        print("Articulo eliminado")
    elif opcion == "5":
        print("Hasta pronto!!!")
        break
    else:
        print("Opcion no valida, intenta de nuevo")