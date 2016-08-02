#este codigo abre el archivo alojado en la carpeta Clase_1 y luego selecciona
#las lineas con datos y las guarda en un archivo nuevo

file="./Clase_1/Hands-On/log.melt-berendsen"

a=open(file,'r')
clave="Step"
fin="Loop"
b=open('resultado','w')
texto=a.readline()
while ~(clave in texto):
 texto=a.readline()
 if (clave in texto):
  texto=a.readline()
  break
 
while ~(fin in texto):
 b.write(texto)
 texto=a.readline()
 if (fin in texto):
  break 
 
a.close()
b.close()
