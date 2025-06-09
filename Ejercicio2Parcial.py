#Ejercicio 2: Dada una lista de personajes de marvel (la desarrollada en clases) debe tener 100 o mas, resolver:
# Listado ordenado de manera ascendente por nombre de los personajes.
# Determinar en que posicion esta The Thing y Rocket Raccoon.
# Listar todos los villanos de la lista.
# Poner todos los villanos en una cola para determinar luego cuales aparecieron antes de 1980.
# Listar los superheores que comienzan con  Bl, G, My, y W.
# Listado de personajes ordenado por nombre real de manera ascendente de los personajes.
# Listado de superheroes ordenados por fecha de aparación.
# Modificar el nombre real de Ant Man a Scott Lang.
# Mostrar los personajes que en su biografia incluyan la palabra time-traveling o suit.
# Eliminar a Electro y Baron Zemo de la lista y mostrar su información si estaba en la lista.

from SuperHeroesParcial import superheroes
from list import List
from queuee import Queue

# Cargar los personajes a la lista principal
lista = List()
for personaje in superheroes:
    lista.insert_value(personaje)

# 1. Listado ordenado ascendente por nombre
print("1. Personajes ordenados por nombre:")
lista.add_criterion('name', lambda x: x['name'])
lista.sort_by_criterion('name')
lista.show()

# 2. Posición de The Thing y Rocket Raccoon
print("\n2. Posiciones:")
for buscado in ["The Thing", "Rocket Raccoon"]:
    pos = lista.search(buscado, 'name')
    if pos is not None:
        print(f"{buscado} está en la posición {pos}")
    else:
        print(f"{buscado} no está")

# 3. Listar todos los villanos
print("\n3. Villanos:")
villanos = List()
for personaje in lista:
    if personaje.get('is_villain', False):
        villanos.insert_value(personaje)
villanos.show()

# 4. Cola con villanos para ver cuáles son anteriores a 1980
print("\n4. Villanos que aparecieron antes de 1980:")
cola_villanos = Queue()
for villano in villanos:
    cola_villanos.arrive(villano)

while cola_villanos.size() > 0:
    villano = cola_villanos.attention()
    if villano['first_appearance'] < 1980:
        print(f"{villano['name']} - {villano['first_appearance']}")

# 5. Superhéroes que comienzan con Bl, G, My o W
print("\n5. Superhéroes que comienzan con Bl, G, My o W:")
for personaje in lista:
    nombre = personaje['name']
    if nombre.startswith(('Bl', 'G', 'My', 'W')):
        print(nombre)

# 6. Ordenar por nombre real
print("\n6. Personajes ordenados por nombre real:")
lista_real = List()
lista_real.add_criterion('real_name', lambda x: x.get('real_name', "") or "")
for personaje in lista:
    lista_real.insert_value(personaje)
lista_real.sort_by_criterion('real_name')
lista_real.show()

# 7. Ordenar por fecha de aparición
print("\n7. Personajes ordenados por año de aparición:")
lista_fecha = List()
lista_fecha.add_criterion('first_appearance', lambda x: x['first_appearance'])
for personaje in lista:
    lista_fecha.insert_value(personaje)
lista_fecha.sort_by_criterion('first_appearance')
lista_fecha.show()

# 8. Modificar nombre real de Ant Man
print("\n8. Modificar nombre real de Ant Man:")
for personaje in lista:
    if personaje['name'] == "Ant Man":
        personaje['real_name'] = "Scott Lang"
        print(f"Modificado: {personaje}")

# 9. Mostrar personajes con 'time-traveling' o 'suit' en la bio
print("\n9. Personajes con 'time-traveling' o 'suit':")
for personaje in lista:
    bio = personaje.get('short_bio', '').lower()
    if 'time-traveling' in bio or 'suit' in bio:
        print(personaje['name'])

# 10. Eliminar Electro y Baron Zemo
print("\n10. Eliminar Electro y Baron Zemo:")
for nombre in ["Electro", "Baron Zemo"]:
    eliminado = lista.delete_value(nombre, 'name')
    if eliminado:
        print(f"{eliminado['name']} eliminado, era {eliminado['real_name']}")
    else:
        print(f"{nombre} no estaba en la lista")