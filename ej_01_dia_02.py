#este codigo resuelve el ejercicio 1 del dia 2. Dadas las coordenadas que ingre
#sa un usuario devuelve un mensaje indicando si el punto está en tierra o mar

#basado en una base de datos que nos entregraon


import numpy as np  #para trabajar con arrays

import argparse  #para generar la interface del usuario


# Define parser data
parser = argparse.ArgumentParser(description='Imprime si la coordenada es tierra o agua')
    # First arguments. Lat Lon. 
parser.add_argument('coords', metavar='Lat Lon', type=float, nargs=2,\
		      help='Latitude Longitude')
#    # Specify sattelites to exclude from command line. TODO: change to flag!
#    parser.add_argument('--no-ascat', dest='ascat_bool', action="store_true", \
#		      default= False, help="Don't display ASCAT information")

    # Extract dates from args
args=parser.parse_args()
#    initialDate = args.date[0]
#finalDate = args.date[1]

lat_ing = args.coords[0]
lon_ing = args.coords[1]
#lat_ing = -43.5;
#lon_ing = 130.25;


file='./Clase_2/Hands-On/data/gl-latlong-1km-landcover.bsq'

#Information
#Image Size: 				43200 Pixels 21600 Lines 
#Quantization:			    8-bit unsigned integer
#Output Georeferenced Units: LONG/LAT E019
#Projection:    				Geographic (geodetic)
#Earth Ellipsoid:			Sphere, rad 6370997 m 
#Upper Left Corner:			180d00'00.00" W Lon90d00'00.00" N Lat
#Lower Right Corner:			180d00'00.00" E Lon 90d00'00.00" S Lat
#Pixel Size (in Degrees):	0.00833 Lon 0.00833 Lat
#(Equivalent Deg,Min,Sec):	0d00'30.00"0d00'30.00" 
#UpLeftX:					-180 
#UpLeftY:      				90
#LoRightX:        			180
#LoRightY: -90
#dt = np.dtype([('time', [('min', int), ('sec', int)]),
#                ('temp', float)])
#x = np.zeros((1,), dtype=dt)
#x['time']['min'] = 10; x['temp'] = 98.25

mascara = np.fromfile(file,dtype=np.int8, count=-1)
print(mascara.shape)

dx = 360*120;
dy = 180*120;

lat = np.array(np.linspace(90,-90,dy,endpoint=True))
lon = np.array(np.linspace(-180,180,dx,endpoint=True))

mascara = np.reshape(mascara,(dy,dx))

print(mascara.shape)

#dadas dos coordenadas busco el punto mas cercano y me fijo si es tierra o agua


cota_lat = np.amin(np.abs(lat-lat_ing))
cota_lon = np.amin(np.abs(lon-lon_ing))

index_lat = np.where(np.abs(lat-lat_ing)==cota_lat)[0]
index_lon = np.where(np.abs(lon-lon_ing)==cota_lon)[0]

print(index_lat,index_lon)

if mascara[index_lat,index_lon]!=0:
  print('Tierra')
else:
  print('Agua')

print(mascara[index_lat,index_lon])


