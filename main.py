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

#    indices = cache.get(palabra["palabra"])
#    if indices is not None:
#       resultado = []
#       for indice in indices:
#           resultado.append(mook.my_document[indice])
#       return resultado
#   else:
#       return "No se encontró"
