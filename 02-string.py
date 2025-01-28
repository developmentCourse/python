texto = "Hola Mundo"
print( texto )
print( texto.upper() ) # Pasara todo el texto a mayusculas
print( texto.lower() ) # Pasara todo el texto a minuscular
print( texto.find("M") ) # Devuelve el índice de la primera aparición de la subcadena. "M"
nuevoTexto = texto.replace("Mun", "estudiantes de ingenieria") # Permitira remplazar una cadena de texto por otra
print(texto, "-", nuevoTexto )

# Uso de la variable in
print( "Mundo" in texto) # Devuelve un dato Booleano, True si es verdadero y False si es falo
print( "Mundo" in nuevoTexto)