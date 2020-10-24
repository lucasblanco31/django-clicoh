# django-clicoh

https://www.youtube.com/watch?v=7XO1AzwkPPE&list=PLU8oAlHdN5BmfvwxFO7HdPciOCmmYneAB

Se creo el proyecto con django-admin startproject Clicoh

Se activo el uso de sqlite3 con python manage.py migrate

Para levantar el servidor python manage.py runserver
Para limpiar el puerto sudo fuser -k 8000/tcp

Para iniciar app python manage.py startapp gestionPedidos

Para checkear si hay errores en app python manage.py chech app

Para migrar base de datos python manage.py makemigrations

para generar codigo sql de la migracion python manage.py sqlmigrate appname migrationid

Para pasar todo al archivo base de datos python manage.py migrate

Para abrir shell python manage.py shell

MANEJO DE BD POR CONSOLA:

╭─lblanco@ContactAR ~/Documentos/Lucas/Clicoh/django-clicoh/TiendaOnline ‹main*› 
╰─$ python manage.py shell
Python 3.8.5 (default, Sep  5 2020, 10:50:12) 
Type 'copyright', 'credits' or 'license' for more information
IPython 7.18.1 -- An enhanced Interactive Python. Type '?' for help.

In [1]: from gestionPedidos.models import Articulos

In [2]: art=Articulos(nombre='mesa', seccion='decoracion', precio=10)

In [3]: art.save()

In [4]: art2=Articulos(nombre='camisa', seccion='ropa', precio=130)

In [5]: art2.save()

In [6]: art3=Articulos.objects.create(nombre='taladro', seccion='herramientas', precio=1030)

In [7]: art.precio=95

In [8]: art.save()

In [9]: art4=Articulos.objects.get(id=2)

In [10]: art4.delete()
Out[10]: (1, {'gestionPedidos.Articulos': 1})

In [11]: Lista=Articulos.objects.all()

In [12]: Lista
Out[12]: <QuerySet [<Articulos: Articulos object (1)>, <Articulos: Articulos object (3)>]>

In [13]: Lista.query.__str__()
Out[13]: 'SELECT "gestionPedidos_articulos"."id", "gestionPedidos_articulos"."nombre", "gestionPedidos_articulos"."seccion", "gestionPedidos_articulos"."precio" FROM "gestionPedidos_articulos"'

In [14]: 

