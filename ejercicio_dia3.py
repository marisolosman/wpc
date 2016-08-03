#este codigo prueba graficar con proyeccion estereografica polar un archivo
#netcdf cualquiera con el geopotencial de 250 pronosticado en diversos plazos
#voy a aprender a usar netcdf4 y basemap

import numpy as np
import netCDF4
import matplotlib.pyplot as plt
import datetime
import calendar
import time

file = '/home/marisol/hgt.mon.mean.nc'

nc = netCDF4.Dataset(file)

hgt = nc.variables["hgt"]   #obtengo el objeto para geopotencial

#print(hgt)

lon = nc.variables["lon"][:]
lat = nc.variables["lat"][:]
tiempo=nc.variables["time"]
times = nc.variables["time"][:]
print(tiempo)
levels = nc.variables["level"][:]

dttme=datetime.date(1,1,1) 

inicio=dttme+datetime.timedelta(hours=times[0])
fin=dttme+datetime.timedelta(hours=times[-1])
deltat=datetime.timedelta(hours=times[1])-datetime.timedelta(hours=times[0])

print(inicio)
print(fin)
print(deltat)

#arranco desde Jan 1948

hs=lat<=0
lev_200=levels==200

#tomo el nivel de 200hPa y los datos de abril
hgt=hgt[3:-1:12,lev_200,hs,:]

lat=lat[hs]

times=times[3:-1:12]

print(hgt.shape)

#saco climatologia anios 1981-2010

anios=np.array(range(1948,2013,1))

clima=(anios>1980)&(anios<=2010)

hgt_clima=hgt[clima,0,:,:]

print(hgt_clima.shape)

#saco promedio respecto al tiempo

hgt_clima=np.mean(hgt_clima,0)
print(hgt_clima.shape)

#calculo anomalia para el anio 2013

hgt_anom_2013=hgt[-1,:,:,:]-hgt_clima

print(hgt_anom_2013.shape)

### PLOTEO EN PROYECCION ESTEREOGRAFICA

import mpl_toolkits.basemap as bm

#limites para colores

v=np.array(range(-140,160,20))

mapproj = bm.Basemap(projection='spstere',\
            boundinglat=0,lon_0=120,resolution='l') 

mapproj.drawcoastlines()
mapproj.drawcountries()
mapproj.drawparallels(np.array([-60, -40, -20, 0]))#, labels=[1,0,0,0])
mapproj.drawmeridians(np.arange(0,360,60))#, labels=[0,0,0,1])

lonall, latall = np.meshgrid(lon, lat)
lonproj, latproj = mapproj(lonall, latall)

cs = plt.contourf(lonproj, latproj, hgt_anom_2013[0,:,:],levels = v)
cs.set_clim(-160,160)
cmap = plt.cm.jet
#cmap(6) = (0,0,0,0)
#incorporo barra
#cbar = ccmap
plt.colorbar(cs,ticks = np.arange(-120,140,20))
#print(cmap(1)
#agrego titulo
plt.title("Anomalia HGT 200hPa Abril 2013")

plt.show()

