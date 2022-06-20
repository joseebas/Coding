import os 
import shutil
import filecmp
import time
import zipfile

#Localizar el directorio actual

os.chdir(r"/home/joseebas/Escritorio/Copia/Archivo")

#Comprimir el archivo

print("Comprimiendo archivos...")
archzip = shutil.make_archive('Datos','zip','/home/joseebas/Escritorio/Copia/DTS', './')
shutil.move(archzip, '/home/joseebas/Escritorio/Python/Comprimidos')
print("Zip creado:", archzip)

print("Comprimiendo archivos...")
archzip = shutil.make_archive('Archivo','zip','/home/joseebas/Escritorio/Copia/Archivo', './')
shutil.move(archzip, '/home/joseebas/Escritorio/Python/Comprimidos')
print("Zip creado:", archzip)

#Comparar archivos

dc = filecmp.dircmp('/home/joseebas/Escritorio/Copia/DTS', '/home/joseebas/Escritorio/Copia/Archivo')
dc.report_full_closure()

#Descomprimir el archivo y copiarlo a un directorio, finalmente se borra el archivo original

archzip = zipfile.ZipFile('/home/joseebas/Escritorio/Python/Comprimidos/Archivo.zip')
archzip.extractall('/home/joseebas/Escritorio/Copia/Final')
archzip.close()
os.remove('/home/joseebas/Escritorio/Python/Comprimidos/Archivo.zip')

archzip = zipfile.ZipFile('/home/joseebas/Escritorio/Python/Comprimidos/Datos.zip')
archzip.extractall('/home/joseebas/Escritorio/Copia/Final')
archzip.close()
os.remove('/home/joseebas/Escritorio/Python/Comprimidos/Datos.zip')

#Cada vez que se descomprime el archivo, se borra el archivo original

if os.path.exists('/home/joseebas/Escritorio/Copia/Archivo/Archivo.zip'):
    os.remove('/home/joseebas/Escritorio/Copia/Archivo/Archivo.zip')
    print("Archivo borrado:", '/home/joseebas/Escritorio/Copia/Archivo/Archivo.zip')

if os.path.exists('/home/joseebas/Escritorio/Copia/DTS/Datos.zip'):
    os.remove('/home/joseebas/Escritorio/Copia/DTS/Datos.zip')
    print("Archivo borrado:", '/home/joseebas/Escritorio/Copia/DTS/Datos.zip')

#crear una ventana para mostrar los archivos que se han descomprimido

if os.path.exists('/home/joseebas/Escritorio/Copia/Final/Archivo.zip'):
    print("Archivo descomprimido:", '/home/joseebas/Escritorio/Copia/Final/Archivo.zip')

if os.path.exists('/home/joseebas/Escritorio/Copia/Final/Datos.zip'):
    print("Archivo descomprimido:", '/home/joseebas/Escritorio/Copia/Final/Datos.zip')
