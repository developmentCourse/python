#Ejercicio de conversor de temperatura 
#Aplicacion que ingrese temperatura a compartir - fahrenheit a celsius y viceversa

temperatura = float(input("Ingrese temperatura: "))
escala = input("Es Fahrenheit(F) o es Celsius(C)?:").lower()

if escala == "f":
    celsius = ( temperatura - 32) * 5/9
    print( celsius )
    print( celsius)
elif escala == "c":
    fahrenheit = temperatura * 1.8 + 32
    print( fahrenheit )
else:
    print("Escala incorrecta")