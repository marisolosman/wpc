#este codigo resuelve el ejercicio 4 del curso de python


cota=999999
cad_maxima=0
for x in range(cota,1,-1):
 x=cota
 cadena=1
 while(x>1):
  if (x%2==0):
   x=x//2
   cadena=cadena+1
  else:
   x=x*2+1
   cadena=cadena+1
 if (cadena>cad_maxima):
  cad_maxima=cadena
  termino=x

print(cad_maxima)
print(termino)


