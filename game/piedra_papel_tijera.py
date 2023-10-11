"""Se desarrarrollara el juego de piedra, papel o tijera 
con python
"""
import random
options= ("piedra", "papel", "tijera")
puntos_PC=0
puntos_user=0
cont=0

print("Juego de piedra, papel o tijera")
print("El que tenga tres puntos es el Ganador, el empate no cuenta")

while True:
  print("______Juega_____")
  User=input("Ingrese su opcion:").lower()
  Computer= random.choice(options)
  if User not in options:
    print("esa opcion no es valida")
    continue
  print("User option:",User)
  print("Computer option:", Computer)
  
  if (User==Computer):
    print("empate")
    continue
  elif(User=="piedra"):
    if(Computer=="tijera"):
      print("piedra gana a tijera")
      print("Usuario gana")
      puntos_user+=1
    else:
      print("papel gana a piedra")
      print("Computer gana")
      puntos_PC+=1
  elif(User=="papel"):
    if(Computer=="piedra"):
      print("papel gana a piedra")
      print("Usuario gana")
      puntos_user+=1
    else:
      print("tijera gana a papel")
      print("Computer gana")
      puntos_PC+=1
  elif(User=="tijera"):
    if(Computer=="papel"):
      print("tijera gana a papel")
      print("Usuario gana")
      puntos_user+=1
    else:
      print("piedra gana a tijera")
      print("Computer gana")
      puntos_PC+=1

  if (puntos_user==3):
    print("¡¡¡ El usuario GANO !!!")
    break
  elif (puntos_PC==3):
    print("¡¡¡ El Computador GANO !!!")
    break
  
