#este codigo resuelve el ejercicio 1 de la practica de python

#tengo que buscar los multiplos de 3 o 5 bajo 1000 y sumarlos

y=0
for x in range(1000):
 if ((x%3==0)|(x%5==0)):
  y=y+x

print(y)


#la forma pythonica es la siguiente
x=0

print(sum(x for x in range(1,1000) if (x%3 == 0 | x%5 == 0) ))


