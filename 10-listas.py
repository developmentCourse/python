lenguajes = ["Python", "Ruby", "PHP", "JavaScript", "Java"]
           #   -5        -4      -3       -2          -1
print( lenguajes )

#valor especifico
print( lenguajes[1] )

#indice negativ
print( "indice negativo", lenguajes[-3])

#mediante rangos
print( "rangos", lenguajes[1:3]) # "Ruby", "PHP" | No incluira hasta el tercer elemento
print( "rangos :3 - ", lenguajes[:3])

#editar valor de lista
lenguajes[1] = "Go"
print( lenguajes)

#añadir valor a la lista
lenguajes.append("C")
print( lenguajes )

#Elimnar por elementos
lenguajes1 = ["Python", "Ruby", "PHP", "JavaScript", "Java"]
lenguajes1.remove("PHP")
print( "Elimnar por elemenos: ", lenguajes1 )  # ['Python', 'Ruby', 'JavaScript', 'Java']

#Eliminar por indice - "del" eliminar un elemento en una posición específica | "pop" Elimina y devuelve el elemento en la posición especificada, si no se especifica un índice, elimina el último elemento

deel = ["Python", "Ruby", "PHP", "JavaScript", "Java"]
del deel[2]  # Eliminar el elemento en la posición 2 (PHP)
print( "pop", deel )  # ['Python', 'Ruby', 'JavaScript', 'Java']

poop = ["Python", "Ruby", "PHP", "JavaScript", "Java"]
poop.pop(3)  # Eliminar el elemento en la posición 3 (JavaScript)
print(poop)  # ['Python', 'Ruby', 'PHP', 'Java']

# Sin índice, elimina el último
poop.pop()  # Eliminar el último elemento (Java)
print( "poop",poop )  # ['Python', 'Ruby', 'PHP']



lenguajes_1 = ["Python", "Ruby", "PHP", "JavaScript", "Java"]
lenguajes_1.insert(3, "Go")
lenguajes_1.insert(0, "C")
print( lenguajes_1 )
print( "PHP" in lenguajes_1) #devolvera False si no exsite en el listado
#limpiar lista
lenguajes_1.clear()
print( lenguajes_1 )
