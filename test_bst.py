from arbol_binario_busqueda import ArbolBinarioBusqueda

# Crear una instancia del árbol
arbol = ArbolBinarioBusqueda()

# Insertar algunos valores
arbol.Insertar(50)
arbol.Insertar(30)
arbol.Insertar(20)
arbol.Insertar(40)
arbol.Insertar(70)
arbol.Insertar(60)
arbol.Insertar(80)

print("Recorrido inorden:")
arbol.Recorrido_inorden() 