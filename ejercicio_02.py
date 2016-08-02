#este codigo suma los terminos pares de la serie de fibonacci menores a
#4000000


yn=1
yn1=2
suma=0
while (yn1<4000000):
 if (yn1%2==0):
  suma=suma+yn1
 aux=yn1
 yn1=yn+yn1
 yn=aux
 aux=0

print(suma)
