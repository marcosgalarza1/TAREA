from nodo import Nodo

class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def _insertar_recursivo(self, nodo, valor):
        if nodo is None:
            return Nodo(valor)
        if valor < nodo.valor:
            nodo.izquierda = self._insertar_recursivo(nodo.izquierda, valor)
        elif valor > nodo.valor:
            nodo.derecha = self._insertar_recursivo(nodo.derecha, valor)
        return nodo # Ignorar valores duplicados

    def Insertar(self, valor):
        self.raiz = self._insertar_recursivo(self.raiz, valor)

    def _buscar_recursivo(self, nodo, valor):
        if nodo is None or nodo.valor == valor:
            return nodo
        if valor < nodo.valor:
            return self._buscar_recursivo(nodo.izquierda, valor)
        return self._buscar_recursivo(nodo.derecha, valor)

    def Buscar(self, valor):
        # Implementar la lógica de búsqueda
        # pass
        return self._buscar_recursivo(self.raiz, valor)

    def _encontrar_minimo(self, nodo):
        actual = nodo
        while actual.izquierda is not None:
            actual = actual.izquierda
        return actual

    def _eliminar_recursivo(self, raiz, valor):
        if raiz is None:
            return raiz

        if valor < raiz.valor:
            raiz.izquierda = self._eliminar_recursivo(raiz.izquierda, valor)
        elif valor > raiz.valor:
            raiz.derecha = self._eliminar_recursivo(raiz.derecha, valor)
        else:
            # Nodo a eliminar encontrado
            # Caso 1: Nodo sin hijos o con un hijo
            if raiz.izquierda is None:
                temp = raiz.derecha
                raiz = None
                return temp
            elif raiz.derecha is None:
                temp = raiz.izquierda
                raiz = None
                return temp

            # Caso 2: Nodo con dos hijos
            temp = self._encontrar_minimo(raiz.derecha)
            raiz.valor = temp.valor
            raiz.derecha = self._eliminar_recursivo(raiz.derecha, temp.valor)

        return raiz

    def Eliminar(self, valor):
        # Implementar la lógica de eliminación
        # pass
        self.raiz = self._eliminar_recursivo(self.raiz, valor)

    def _recorrido_inorden_recursivo(self, nodo):
        if nodo:
            self._recorrido_inorden_recursivo(nodo.izquierda)
            print(nodo.valor, end=' ')
            self._recorrido_inorden_recursivo(nodo.derecha)

    def Recorrido_inorden(self):
        # Implementar el recorrido inorden
        # pass
        self._recorrido_inorden_recursivo(self.raiz)
        print() # Imprimir una nueva línea al final del recorrido

    def _calcular_altura_recursivo(self, nodo):
        if nodo is None:
            return 0
        return 1 + max(self._calcular_altura_recursivo(nodo.izquierda), self._calcular_altura_recursivo(nodo.derecha))

    def Calcular_altura(self):
        # Implementar el cálculo de altura
        # pass
        # La altura del árbol es la altura de la raíz menos 1 (si la altura de un nodo es 1 + max(izq, der))
        # O simplemente la altura de la raíz si la altura de un nodo es max(izq, der) + 1.
        # La implementación actual de Calcular_altura en la imagen sugiere que la altura de un nodo es 1 + max(izq, der), por lo que la altura del árbol es la altura de la raíz.
        # Si la altura de un nodo hoja es 1, entonces la altura de un árbol de un solo nodo es 1. La altura de un árbol vacío sería 0.
        # Si la altura de un nodo hoja es 0, entonces la altura de un árbol de un solo nodo es 1. La altura de un árbol vacío sería 0.
        # Si la altura de un nodo hoja es 0, entonces la altura de un árbol de un solo nodo es 1. La altura de un árbol vacío sería -1.
        # La implementación en Nodo establece la altura inicial en 1, lo que sugiere que un nodo hoja tiene altura 1. Siguiendo esa convención, la altura de un árbol vacío sería 0.
        # Corrigiendo: La implementación de Nodo.altura = 1 es para usos futuros en AVL. La altura del árbol se calcula recursivamente aquí.
        # Si un nodo hoja tiene altura 0, la altura del árbol de un solo nodo es 1. Árbol vacío es altura -1.
        # Si un nodo hoja tiene altura 1, la altura del árbol de un solo nodo es 2. Árbol vacío es altura 0.
        # Considerando la convención común de BST/AVL, la altura de un nodo hoja es 0, y la altura de un árbol vacío es -1.
        # Por lo tanto, la implementación recursiva debe reflejar esto.
        # La función auxiliar _calcular_altura_recursivo(None) debe retornar -1. Un nodo hoja (izquierda y derecha None) debe retornar 0 (1 + max(-1, -1)).
        # Ajustando la lógica recursiva:
        return self._calcular_altura_recursivo(self.raiz)