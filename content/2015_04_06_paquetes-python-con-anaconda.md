Title: Paquetes Python para ciencia e ingeniería con Anaconda
Date: 2015-4-6 21:07
Category: Tutoriales
Tags: herramientas
Slug: paquetes-python-con-anaconda
Summary: Paquetes Python para ciencia e ingeniería con Anaconda, instalación, creación y gestión de entornos virtuales y comandos básicos.
Status: published

##Introducción

Si estás utilizando Scikit-learn, Pandas u otro paquete de Python para ingeniería o ciencia sabrás que es una pérdida de tiempo estar buscando y descargando los paquetes que deseas instalar. Además de tener en cuenta la compatibilidad entre paquetes. Para evitar problemas usamos herramientas como VirtualEnv (para crear entornos virtuales y trabajar con distintas versiones de librerías) y PIP (para instalar paquetes).

La buena noticia es que existe Anaconda,  que nos permite instalar paquetes y gestionar entornos virtuales fácilmente, además de tener otras ventajas:

* Ahorro de tiempo al instalar paquetes adicionales requeridos.
* Tiene un administrador de paquetes y gestor de entornos virtuales.
* No necesitas permisos de administrador.
* Multiplataforma (Windows, Mac y Linux).
* Es completamente gratuita, incluso para uso comercial y redistribución.

Ahora pasemos a definir Anaconda, ver la instalación, creación de entornos virtuales y conocer otros comandos básicos.

## ¿Qué es Anaconda?
Anaconda es una distribución de Python multiplataforma, desarrollada por [Continuum Analytics](http://continuum.io/). Contiene una gran colección de paquetes y librerías para análisis de datos, computación científica e ingeniería. Si no deseas descargar la distribución completa (por tener un ancho de banda reducido, ...) puedes optar por **Miniconda**, que contiene solamente el gestor de paquetes Conda y Python para luego instalar lo que necesites.

## Instalando Miniconda

Descarga la versión que desees:
* Conda: http://continuum.io/downloads
* Miniconda: http://conda.pydata.org/miniconda.html

Yo he descargado `Miniconda3-latest-Linux-x86_64.sh`,  Miniconda Python 3.4 64-bit(bash installer) y guardado en la carpeta `Donwloads`. Se recomienda usar Python 3, [que es el presente y futuro de Python](http://www.getpython3.com/).

Abrimos un terminal (Ctrl + Alt + t), vamos a la carpeta donde hemos guardado el instalador (en mi caso `Downloads`) y procedemos con la instalación.
```bash
cd Downloads
bash Miniconda3-latest-Linux-x86_64.sh
```
Nos aparecerá un mensaje de bienvenida, presionamos enter y nos saldrá la licencia. Para dejar de leerla presiona `Crtl + c` y para aceptar las condiciones escribimos "yes".

![Instalando Miniconda]({filename}images/instalando-miniconda.png)

Nos quedarán dos preguntas más por responder, en mi caso he presionado "enter" y escrito "yes". Finalmente para activar los cambios abre un nuevo terminal. Abajo puedes ver como he respondido:

```bash
Miniconda3 will now be installed into this location:
/home/italo/miniconda3

  - Press ENTER to confirm the location
  - Press CTRL-C to abort the installation
  - Or specify a different location below

[/home/italo/miniconda3] >>>
PREFIX=/home/italo/miniconda3
installing: python-3.4.2-0 ...
installing: conda-env-2.1.3-py34_0 ...
installing: openssl-1.0.1k-0 ...
installing: pycosat-0.6.1-py34_0 ...
installing: pyyaml-3.11-py34_0 ...
installing: readline-6.2-2 ...
installing: requests-2.5.3-py34_0 ...
installing: sqlite-3.8.4.1-0 ...
installing: system-5.8-1 ...
installing: tk-8.5.15-0 ...
installing: xz-5.0.5-0 ...
installing: yaml-0.1.4-0 ...
installing: zlib-1.2.8-0 ...
installing: conda-3.9.1-py34_0 ...
Python 3.4.2 :: Continuum Analytics, Inc.
creating default environment...
installation finished.
Do you wish the installer to prepend the Miniconda3 install location
to PATH in your /home/italo/.bashrc ? [yes|no]
[no] >>> yes

Prepending PATH=/home/italo/miniconda3/bin to PATH in /home/italo/.bashrc
A backup will be made to: /home/italo/.bashrc-miniconda3.bak


For this change to become active, you have to open a new terminal.

Thank you for installing Miniconda3!
```

## Actualizando Conda
Primero, abrimos un nuevo terminal y verificamos si la instalación ha sido correcta.
```bash
$ conda -V
conda 3.9.1
```
Otra forma:
```bash
$ conda info
```

Actualizando Conda:
```bash
$ conda update conda
```

## Entornos virtuales

Ver los entornos que tenemos:
```bash
$ conda info -e
```
Nos mostrará los entornos creados. Yo tengo dos: django y root. El símbolo * indica en que entorno estamos. Cuando instalas Anaconda el entorno por defecto (default) será root.
```bash
# conda environments:
#
django                   /home/italo/miniconda3/envs/django
root                  *  /home/italo/miniconda3
```
Crear un entorno. Por ejemplo llamado django y utilizando Python 3:
```bash
$ conda create -n django python
```

Crear un entorno usando python 2. La versión de un paquete se indica con el signo "=". 
```bash
$ conda create -n django python=2
```

Activar un entorno. Por ejemplo el entorno "django":
```bash
$ source activate django
```

Observa que ahora el nombre del entorno aparecerá entre paréntesis.
```bash
(django)italo@italo-tosh:~$
```

Desactivar entorno django:
```bash
(django)italo@italo-tosh:~$ source deactivate
```
Eliminar un entorno:
```bash
$ conda remove -n nombredelentorno --all
```

Clonar un entorno:
```bash
conda create -n nombredelnuevo --clone nombredelquequieresclonar
```

##Instalar paquetes
Primero veamos los entornos que tenemos. Tenemos dos, el root (raíz) y django, que lo acabamos de crear.
```bash
italo@italo-tosh:~$ conda info -e
# conda environments:
#
django                   /home/italo/miniconda3/envs/django
root                  *  /home/italo/miniconda3
```


Instalando paquetes en el entorno root. Por ejemplo el paquete Scipy:
```bash
conda install scipy
```
Instalando paquetes en otro entorno:
```bash
$ conda install -n mombredelentorno nombredelpaquete
```
Instalando una versión específica. Por ejemplo: en el entorno de nombre myenv instalamos el paquete Scipy, versión 0.12.0
```bash
$ conda install -n myenv scipy=0.12.0
```

Otra forma de instalar paquetes es activando el entorno y luego proceder con la instalación:
```bash
$ source activate nombredelentorno
$ conda install nombredelpaquete
```

Listar los paquetes instalados. Si estamos en el entorno root (entorno “myenv” desactivado):
```bash
$ conda list -n myenv
```
Si estamos en el entorno "myenv" (el entorno "myenv" está activado).
```bash
$ conda list
```
Ver si un paquete ya está instalado:
```bash
$ conda list -n myenv scipy
```

Comprobar si un paquete esta disponible para instalar:
```bash
$ conda search nombredelpaquete
```
O también:
```bash
conda search "^django$"
```
## Usar PIP para instalar otros paquetes

Anaconda incluye más de 190 paquetes pero puede pasar que el que desees no esté incluido en Anaconda. Entonces puedes hacer uso de PIP.

Primero instala el paquete PIP (probablemente ya esté instalado), activa el entorno y luego usa los comandos de PIP.
```bash
$ conda install -n nombredelentorno pip
$ source activate nombredelentorno
$ pip install nombredelpaquete
```
Con PIP puedes instalar librerías, crear un archivo de requerimientos, etc. 

##Más información
* [Reference Guide PIP (2015)](https://pip.pypa.io/en/latest/reference/pip.html) 
* [Entornos virtuales con PIP (2013)](http://soulchainer.github.io/posts/2013/12/30/python-paquetes-entornos-virtuales/)
* [Conda FAQ(2015)](http://conda.pydata.org/docs/faq.html)
* [Using the Anaconda Python Distribution(2014)](http://davebehnke.com/using-python-anaconda-distribution.html)
* [Virtualenv Python Guide(2014)](http://docs.python-guide.org/en/latest/dev/virtualenvs/#virtual-environments)


