# Tres módulos que ya vienen con Python: sys para el intérprete, platform para el sistema operativo 
# os para el sistema de ficheros.

import sys
import os
import platform

version = sys.version
sistema = platform.system() + " " + platform.release()
directorio = os.getcwd()

print(f"Python: {version}")
print(f"Sistema: {sistema}")
print(f"Directorio: {directorio}")

version_ok = sys.version_info >= (3, 10)
print(f"¿Versión 3.10+? {version_ok}")

# Comprobacion para hacer despues de una instalacion de python en Windows o Mac
# Linux ya viene con python instalado version 3.12+