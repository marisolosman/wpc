#codigo para encontrar el factor primo mas grande de
#600851475143

import math

nro=600851475143
cota=round(math.sqrt(nro))

print(cota)

for x in range(1,cota):
 if nro%x==0:
  aux=0
  for y in range (1,x):
   if ((x%y==0)&((y!=1)&(y!=x))):
    aux=1
    break
  if (aux!=1):
   maximo=x

print(maximo)

