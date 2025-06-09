#Ejercicio 1: Dado una lista simple de python (array) de 15 superheroes realizar dos funciones recursivas:
# funcion recursiva  para buscar, determinar si Capitan America esta en la lista.
# funcion recursiva para listar los superheroes de la lista.

superheroes = [
    "Iron Man", "Thor", "Hulk", "SpiderMan", "Black Widow",
    "Captain America", "Black Panther", "Doctor Strange", 
    "AntMan", "Wasp", "Hawkeye", "Scarlet", 
    "Vision", "Falcon", "Deadpool"
]

# Función recursiva para buscar a "Captain America"
def buscar_capitan_america(lista, indice=0):
    if indice >= len(lista):
        return False
    if lista[indice] == "Captain America":
        return True
    return buscar_capitan_america(lista, indice + 1)

# Función recursiva para listar todos los superhéroes
def listar_superheroes(lista, indice=0):
    if indice >= len(lista):
        return
    print(lista[indice])
    listar_superheroes(lista, indice + 1)

# --- Ejecución ---
if buscar_capitan_america(superheroes):
    print("Si, Captain America esta en la lista")
else:
    print("No, Captain America no está en la lista")

print("\nLista de superheroes:")
listar_superheroes(superheroes)