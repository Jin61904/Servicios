from fastapi import FastAPI
import mook

app = FastAPI()

@app.get("/")
def root():
    return{
        "Servicio": "Estructuras de Datos"
    }

@app.post("/indices-invertidos")
def indices_invertidos(palabra: dict):
    cache = {}
    for index, documento in enumerate(mook.my_document):
        words = documento.lower().split()

        for word in words:
            if word in cache:
                cache[word].append(mook.my_document[index])
            else:
                cache[word] = [mook.my_document[index]]
    return cache.get(palabra ["palabra"], "No se encontró")

@app.post("/Floyd-algorithm")

class Nodo():
  def __init__(self, valor):
    self.valor = valor
    self.siguiente = None

  def __repr__(self) -> str:
    return f"<nodo {self.valor}>"

def detectar_ciclo(lista):
  class NodoInterno(Nodo):
    pass

  tortuga = lista
  liebre = lista

  while liebre and liebre.siguiente and tortuga:
    tortuga = tortuga.siguiente
    liebre = liebre.siguiente.siguiente

    if tortuga == liebre:
      print(tortuga, liebre)
      break

  liebre = lista

  while liebre != tortuga:
    liebre = liebre.siguiente
    tortuga = tortuga.siguiente
    print(tortuga, liebre)

  return False

nodo1 = Nodo(1)
nodo2 = Nodo(2)
nodo3 = Nodo(3)
nodo4 = Nodo(4)
nodo5 = Nodo(5)

nodo1.siguiente = nodo2
nodo2.siguiente = nodo3
nodo3.siguiente = nodo4
nodo4.siguiente = nodo5
nodo5.siguiente = nodo2

detectar_ciclo(nodo1)
class Nodo():
  def __init__(self, valor):
    self.valor = valor
    self.siguiente = None

  def __repr__(self) -> str:
    return f"<nodo {self.valor}>"

def detectar_ciclo(lista):
  class NodoInterno(Nodo):
    pass

  tortuga = lista
  liebre = lista

  while liebre and liebre.siguiente and tortuga:
    tortuga = tortuga.siguiente
    liebre = liebre.siguiente.siguiente

    if tortuga == liebre:
      print(tortuga, liebre)
      break

  liebre = lista

  while liebre != tortuga:
    liebre = liebre.siguiente
    tortuga = tortuga.siguiente
    print(tortuga, liebre)

  return False

nodo1 = Nodo(1)
nodo2 = Nodo(2)
nodo3 = Nodo(3)
nodo4 = Nodo(4)
nodo5 = Nodo(5)

nodo1.siguiente = nodo2
nodo2.siguiente = nodo3
nodo3.siguiente = nodo4
nodo4.siguiente = nodo5
nodo5.siguiente = nodo2

detectar_ciclo(nodo1)

#@app.post("/BusquedaRepetidos")