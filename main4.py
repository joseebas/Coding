
import os 
import shutil
from distutils.dir_util import copy_tree
import filecmp
import time
import zipfile

#Comprimir el archivo

print("Comprimiendo...")
archzip = zipfile.ZipFile('/home/joseebas/Escritorio/Copia/Archivo', 'w')
archzip.write('/home/joseebas/Escritorio/Python/Comprimidos', compress_type=zipfile.ZIP_DEFLATED)
archzip.close()

#Comparar archivos

print("Comparando...")
dc = filecmp.dircmp('/home/usuario/Escritorio/Python', '/home/usuario/Escritorio/Copia')
dc.report()

#Descomprimir el archivo

print("Descomprimiendo...")
extract = zipfile.ZipFile('/home/joseebas/Escritorio/Copia/Archivo', 'r')
extract.extractall('/home/joseebas/Escritorio/Copia/Comprimidos')
extract.close()

#Copiar los ficheros de una Carpeta a otra

fuente = '/home/usuario/Escritorio/Python/Archivos'
destino = '/home/usuario/Escritorio/Copia/Archivos'

print("Copiando...")
copy_tree(fuente, destino)
print("Copiado!")
