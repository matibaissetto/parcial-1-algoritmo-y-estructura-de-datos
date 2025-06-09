from SuperHeroesParcial import superheroes
from list import List
from queuee import Queue

# Cargar los personajes a la lista principal
lista = List()
for personaje in superheroes:
    lista.insert_value(personaje)  # Usamos insert_value en lugar de insert

# 1. Listado ordenado ascendente por nombre
print("1. Personajes ordenados por nombre:")
lista.add_criterion('name', lambda x: x['name'])  # Agregamos criterio de ordenamiento
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
for personaje in lista:
    lista_real.insert_value(personaje)

lista_real.add_criterion('real_name', lambda x: x['real_name'])
lista_real.sort_by_criterion('real_name')
lista_real.show()

# 7. Ordenar por fecha de aparición
print("\n7. Personajes ordenados por año de aparición:")
lista_fecha = List()
for personaje in lista:
    lista_fecha.insert_value(personaje)

lista_fecha.add_criterion('first_appearance', lambda x: x['first_appearance'])
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
    bio = personaje['short_bio'].lower()
    if 'time-traveling' in bio or 'suit' in bio:
        print(personaje['name'])

# 10. Eliminar Electro y Baron Zemo
print("\n10. Eliminar Electro y Baron Zemo:")
for nombre in ["Electro", "Baron Zemo"]:
    pos = lista.search(nombre, 'name')
    if pos is not None:
        eliminado = lista.delete_value(nombre, 'name')
        print(f"{eliminado['name']} eliminado, era {eliminado['real_name']}")
    else:
        print(f"{nombre} no estaba en la lista")