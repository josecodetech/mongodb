import pymongo
cliente = pymongo.MongoClient("mongodb://localhost:27017/")
# crea bd
db = cliente['ventas']
# crea coleccion
coleccion = db['articulos']
# inserta datos
articulo1 = {"nombre":"camiseta","precio":15.99,"stock":50}
articulo2 = {"nombre":"pantalones","precio":35.99,"stock":30}
# insertar documentos
# inserta 1
# coleccion.insert_one(articulo1)
# inserta varios
articulos = [articulo1,articulo2]
coleccion.insert_many(articulos)
# listado
colecciones = db.list_collection_names()
print("Colecciones en la base de datos : ")
for col in colecciones:
    print(col)
# listado de documentos
documentos = coleccion.find({})
print("\nDocumentos en la colección artículos : ")
for doc in documentos:
    print(doc)
# edicion, modificacion y borrado
# actualizar documento
filtro = {"nombre":"camiseta"}
nuevo_valor = {"$set":{"stock":45}}
coleccion.update_one(filtro,nuevo_valor)
# eliminar
filtro = {"nombre":"pantalones"}
coleccion.delete_one(filtro)







