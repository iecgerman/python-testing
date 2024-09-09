# Curso de Unit Testing en Python

# Fundamentos del Testing en Python

# Instalación y Configuración del Entorno de Pruebas

"""
Instalación de pip y activación de entornos virtuales en Windows por iecgerman

https://platzi.com/tutoriales/4261-python-pip/39879-instalacion-de-pip-y-activacion-de-entornos-virtuales-en-windows-por-iecgerman/

paso 1 

pip install virtualenv

paso 2

 virtualenv venv # aquí nos crea la carpeta venv

 paso 3

cd <nombre_entorno>\Scripts
# en nuestro caso sería:
cd venv\Scripts

debemos de quedar en:

C:\Users\info\python-testing\PYTHON-TESTING\venv\Scripts>

por ultimo teclamos:

.\activate

ojo 👀 si les aparece este error como en mi caso:

C:\Users\info\python-testing\PYTHON-TESTING\venv\Scripts> .\activate
.\activate : No se puede cargar el archivo C:\Users\info\python-testing\PYTHON-TESTING\venv\Scripts\activate.ps1 porque la 
ejecución de scripts está deshabilitada en este sistema. Para obtener más información, consulta el tema
about_Execution_Policies en https:/go.microsoft.com/fwlink/?LinkID=135170.
En línea: 1 Carácter: 1
+ .\activate
+ ~~~~~~~~~~
    + CategoryInfo          : SecurityError: (:) [], PSSecurityException
    + FullyQualifiedErrorId : UnauthorizedAccess

****  SE SOLUCIONA MUY FACIL ***

-Primero debemos abrir powershell como administrador (con click derecho ejecutar  como admin)

-despues sólo ponemos el sigueinte comando:

C:\WINDOWS\system32> Set-ExecutionPolicy Unrestricted

listo volvemos a VSCode y ahora si:

.\active

RESULTADO:

(venv) PS C:\Users\info\python-testing\PYTHON-TESTING\venv\Scripts> C:\Users\info\python-testing\PYTHON-TESTING\venv\Scripts>C:\Users\info\python-testing\PYTHON-TESTING\venv\Scripts>



"""


# ****************



"""
(venv) PS C:\Users\info\python-testing\PYTHON-TESTING> python -m unittest         
                                                                                  
----------------------------------------------------------------------
Ran 0 tests in 0.000s

NO TESTS RAN
(venv) PS C:\Users\info\python-testing\PYTHON-TESTING> 
"""

"""
(venv) PS C:\Users\info\python-testing\PYTHON-TESTING> python -m unittest discover -s tests
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
(venv) PS C:\Users\info\python-testing\PYTHON-TESTING> 
"""

