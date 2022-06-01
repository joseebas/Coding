import os 
import shutil
from distutils.dir_util import copy_tree
import filecmp
import time

#Comparar archivos

dc = filecmp.dircmp('/home/usuario/Escritorio/Python', '/home/usuario/Escritorio/Copia')
dc.report()

#Copiar los ficheros de una Carpeta a otra

fuente = '/home/usuario/Escritorio/Python/Archivos'
destino = '/home/usuario/Escritorio/Copia/Archivos'

print("Copiando...")
copy_tree(fuente, destino)
print("Copiado!")

