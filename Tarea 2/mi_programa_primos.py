def comprobar_primo():
  numero = int(input('Introduce un número: '))
  if numero > 1:
    for i in range(2, numero):
      # print('i ', i)
      resto = numero % i
      # print('resto ', resto)
      if (resto) == 0:
        print('El número', numero, 'no es un número primo porque es divisible entre', i)
        break
    else: 
      print('El número', numero, 'es un número primo')
  else: 
    print('El número ', numero, 'es un número primo')


while True:
  comprobar_primo()