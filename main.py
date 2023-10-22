from typing import List
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


class Nodo():
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

    def __repr__(self) -> str:
        return f"<nodo {self.valor}>"

def detectar_ciclo(lista):
    tortuga = lista
    liebre = lista

    while liebre and liebre.siguiente and tortuga:
        tortuga = tortuga.siguiente
        liebre = liebre.siguiente.siguiente

        if tortuga == liebre:
            return tortuga

    return None

@app.get("/floyd-algorithm")
def floyd_algorithm():

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

    nodo_ciclo = detectar_ciclo(nodo1)
    if nodo_ciclo:
        return {"tiene_ciclo": True, "valor_nodo_ciclo": nodo_ciclo.valor, "nodo_ciclo": str(nodo_ciclo)}
    else:
        return {"tiene_ciclo": False}

#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

@app.post("/Números-duplicados")
def find_duplicate(nums: List[int]):
    tortoise = hare = nums[0]
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break

    hare = nums[0]
    while tortoise != hare:
        tortoise = nums[tortoise]
        hare = nums[hare]

    return {"duplicate": hare}