numero = (input('Ingresa algun numero: '))
# Usamos una f-string para meter la variable 'numero' dentro del texto
confirmacion = input(f'Perfecto, el numero que ingresaste es {numero}. ¿Es correcto? (s/n): ')

numero1 = (input('Ingrese algun otro numero: '))
# Ahora pediremos la confirmacion
confirmacion1 = input(f'Perfecto, el numero que ingresaste es {numero}. Es correcto? (s/n)')

print(f'Perfecto los numeros que ingresaste son: {numero} y {numero1}')

print('''Dime ahora que es lo que quisieras hacer con tus numeros, tenemos las siguentes opciones: 
1. Sumar 
2. Restar
3. Multiplicar''')

opcion = input('Dime cual de las opciones escogiste: ').lower().strip()

if opcion == '1' or opcion == 'sumar':
    resultado = numero + numero1
    print(f'El resultado de la suma de {numero} + {numero1} = {resultado}')
elif opcion == '2' or opcion == 'restar':
    resultado = numero - numero1
    print(f'El resultado de la resta de {numero} - {numero1} = {resultado} ')
elif opcion == '3' or opcion == 'multiplicar':
    resultado = numero * numero1
    print(f'El resultado de la multiplicacion de {numero} * {numero1} = {resultado}')

lista = [numero, confirmacion, numero1, confirmacion1, opcion, resultado]
print(type(lista))
print(lista)
lista.append('programando')
print(lista)
lista.append('estudiando')
print(lista)
print(lista[1])
lista.insert(1, 'Anthony')
print(lista)
lista[1] = 'bebe'
print(lista)
lista.remove('bebe')
del lista[0]
print(lista)
print(len(lista))

print("Contenido de mi lista:")
for elemento in lista:
    print(f"- {elemento.capitalize()}")












# while True:
#     try:
#         numero = int(input('Ingresa un número para el registro: '))
        
#         # Pregunta de confirmación clara
#         print(f"\nHas ingresado: {numero}")
#         confirmar = input("¿Deseas continuar con este valor? (s/n): ").lower().strip()

#         if confirmar == 's':
#             print("Dato guardado exitosamente.")
#             break # Sale del bucle porque todo está bien
#         else:
#             print("Entendido, intentemos de nuevo.\n")
            
#     except ValueError:
#         print("Error: Por favor, ingresa un número válido (solo dígitos).")