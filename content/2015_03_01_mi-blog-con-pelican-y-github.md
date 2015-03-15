Title: Mi blog con Pelican y Github
Date: 2015-3-1 11:46
Category: tutoriales
Tags: python, pelican
Slug: mi-blog-con-pelican-y-github
Summary: Guía para crear tu blog o web con Github, dominio propio y Pelican (generador de sitios web escrito en Python).


Cansado de lidiar con el editor de wordpress (y antes con el de blogger) decidí buscar herramientas que me ofrecieran construir un blog más limpio, integrar código y los notebooks de python más fácilmente y sobre todo alojamiento gratuito. A continuación describiré como configuré mi blog con dominio propio usando Pelican y espero te sirva si no eres informático.

## Ingredientes:

- Pelican: un generador de sitios estáticos construido con Python. Hay muchos más, me quede con Pelican por la comunidad activa (lo que significa: más documentación, plugins, plantillas).
- GitHub Pages: que permite alojar webs para ti y tus proyectos alojadas en tu repositorio Github.
- Dominio propio: no es obligatorio. Si no lo tienes la url de tu blog será usuario.github.io

## Configuración de GitHub Pages
Crea un repositorio en github con el nombre: usuario.github.io 

Si sigues las instrucciones de [Github Pages](http://pages.github.com/) solo crea el repositorio (primer paso), nada más. Allí es donde se alojará el contenido de tu blog/web.

## Instalación y configuración de Pelican

Tienes que instalar Pelican y Markdown, este último es opcional. Markdown es un lenguaje sencillo para generar contenido HTML sin necesidad de saber HTML. Pelican usa reStructuredText (rST) que también es fácil de manejar. [Más info sobre paquetes](http://docs.getpelican.com/en/3.1.1/getting_started.html#installing-pelican).
```bash
$ pip install pelican markdown
```

Crea una carpeta por ejemplo, `blog`. Esta contendrá todo lo necesario para crear tu blog/web, dentro de ella ejecutaremos `pelican quickstart`. Pelican por medio de un diálogo te ayuda con la configuración.
```bash
$ mkdir blog
$ cd blog
$ pelican-quickstart
```
Abajo puedes ver como respondi:
```bash
Where do you want to create your new web site? [.]
What will be the title of this web site?
> Italo Farfán
Who will be the author of this web site?
> Italo Farfán Vera
What will be the default language of this web site? [es]
Do you want to specify a URL prefix? e.g., http://example.com   (Y/n)
> y
What is your URL prefix? (see above example; no trailing slash)
> http://italofarfan.github.io
Do you want to enable article pagination? (Y/n)
> y
How many articles per page do you want? [10]
Do you want to generate a Fabfile/Makefile to automate generation and publishing? (Y/n)
> y
Do you want an auto-reload & simpleHTTP script to assist with theme and site development? (Y/n)
> y
Do you want to upload your website using FTP? (y/N)
> n
Do you want to upload your website using SSH? (y/N)
> n
Do you want to upload your website using Dropbox? (y/N)
> n
Do you want to upload your website using S3? (y/N)
> n
Do you want to upload your website using Rackspace Cloud Files? (y/N)
> n
> 
```

Pelican creará la siguiente estructura de directorios:

```bash
$ tree

├── Makefile
├── content
├── develop_server.sh
├── fabfile.py
├── output
├── pelicanconf.py
└── publishconf.py
```

Pelican asume que los artículos que escribirás los guardarás en la carpeta `content`. Adicionalmente deberías crear dos nuevas carpetas.
```bash
$ mkdir content/pages
$ mkdir content/images
```
En pages podrás crear los archivos `about me`, `contact`, etc. Pelican los reconocerá sin problemas.

Pelican convertirá tus artículos guardados en `content` en html y los guardará en la carpeta `output`. Más adelante comentaré cómo hacer para que tengan el siguiente estilo: midominio.com/2015/01/31/nombre-de-mi posts.html

Es en `output` donde se generará tu sitio web y es donde tendrás que colocar el archivo CNAME si deseas utilizar un dominio propio (tudominio.com).

## Subiendo nuestros cambios a la nube

Tenemos que inicializar un repositorio github desde nuestra carpeta output y conectarlo con nuestro repositorio remoto creado anteriormente (usuario.github.io).
```bash
$ cd output
$ git init
$ git remote add origin https://github.com/username/username.github.io.git
$ git add --all
$ git commit -m "commit message"
$ git push origin master
```
Ya estás listo para publicar pero ****no todas las plantillas ofrecen soporte a todos los plugins****. Por ejemplo Disqus, que permite integrar comentarios en tu blog, no funciona con la plantilla por defecto. La plantilla que usa Amy y la mía funcionan. [Amy Hanlon tiene una guía en inglés muy completa](http://mathamy.com/migrating-to-github-pages-using-pelican.html).

## Plugins y plantillas
Yo estoy utilizando la plantilla pelican-bootstrap3 y el plugin Tipue Search para agregar el cuadro de búsqueda en la parte superior derecha. La plantilla es responsive.

Para usarlas lo más rápido es clonar el repositorio plugins.

```bash
$ git clone https://github.com/getpelican/pelican-themes
```
Y el repositorio plantillas al directorio que creaste, en mi caso el directorio "blog".
```bash
$ git clone https://github.com/getpelican/pelican-plugins
```

Luego tienes que abrir el archivo `pelicanconf.py` e indicar la ruta donde se encuentran los plugins y el plugin que usarás. Agregar lo siguiente:
```python
# Plugins
PLUGIN_PATH = 'pelican-plugins'
PLUGINS = ['tipue_search']
```
Indica la plantilla que usarás, en mi caso al usar la plantilla pelican-bootstrap3  la variable `THEME` queda de la siguiente forma: pelican-themes/nombre-de-plantilla.

```python
THEME = "pelican-themes/pelican-bootstrap3"
```
Si aún te quedan dudas echa un vistazo [al archivo pelicancof.py y publishconf.py de DandyDev creador de plantilla Booostrap3](https://github.com/DandyDev/dandydev.net)

Más información:
* [Documentación de la plantilla Bootstrap3](https://github.com/DandyDev/pelican-bootstrap3)
*  [Migrating to GitHub Pages using Pelican por Amy Hanlon](http://mathamy.com/migrating-to-github-pages-using-pelican.html)

## Agregando Disqus, Google Analytics y Addthis (botones para compartir)
Se supone que ya tienes una cuenta en estos servicios gratuitos.

* Disqus: necesitas de un `short_name`, para ello registra tu web: https://disqus.com/admin/create/ Indica el nombre de tu sitio (SITE NAME) y una DISQUS_URL. Este último será tu shortname. Finalmente obtendrás algo como esto: http://short_name.disqus.com/admin/settings
* AddThis: necesitas Profile ID, lo puedes crear desde settings: https://www.addthis.com/settings/publisher
* Google Analytics: necesitas de un "identificador", si no lo tienes, entra a Google Analytics y crea una nueva propiedad. Desde Admin/Property obtendrás un identificador de la forma: UA-XXXX-YYYY

Ahora agrega las siguientes líneas en `pelicanconf.py` y `publishconf.py`
```python
DISQUS_SITENAME = "tu_short_name"
GOOGLE_ANALYTICS = "UA-XXXXXX-1"
ADDTHIS_PROFILE = 'ra-XXXXXXXXXXXXXXXX'
```

Más información en:

* [Howto Setup Comments with Disqus in Pelican](http://querbalken.net/howto-setup-comments-with-disqus-in-pelican-en.html)

## Configurando dominio propio
* Crea un archivo `CNAME` y dentro escribe tu dominio, por ejemplo: tudominio.com
* Guarda el archivo `CNAME` en la carpeta output
* Entra al panel de control de tu proveedor de dominio y crea un registro CNAME que apunte a tu_usuario.github.io o un registro A añadiendo los siguientes IP `192.30.252.153` y `192.30.252.154`. En mi caso Strato solo me déjo agregar un IP e igual funciona.

Más info:
* [Ayuda de Github para crear un registro CNAME](https://help.github.com/articles/tips-for-configuring-a-cname-record-with-your-dns-provider/)
* [Ayuda de Github para crear un registro A](https://help.github.com/articles/tips-for-configuring-an-a-record-with-your-dns-provider/)

## Escribiendo artículos en reStructuredText(rST) y Markdown(md)

Creamos un archivo con la extensión .rst o .md y lo guardamos en la carpeta content.

#### Ejemplo en reStructuredTex
~~~
Mi primer post
##############

:date: 2015-03-01 15:43
:tags: test, prueba
:category: python
:slug: mi-primer-post
:author: TuNombre
:summary: Versión corta para el índice y feeds
~~~
#### Ejemplo en Markdown
```md
Title: My super title
Date: 2010-12-03 10:20
Tags: thats, awesome
Category: yeah
Slug: my-super-post
Author: Alexis Metaireau
Summary: Short version for index and feeds

This is the content of my super blog post.
```

## Automatizar creación de archivos

Para poder crear más rápido los posts podemos hacer uso de un script:

* Para rST: `make_entry.py`, de Nafiul Islam [Descárgalo aquí](http://nafiulis.me/making-a-static-blog-with-pelican.html#automation).
* Para md: `make_entrymd.py`, modifiqué el archivo para que funcione con md. [Descárgalo aquí](https://github.com/italofarfan)

Para ejecutarlo nos ubicamos en el directorio principal:
```bash
 $ python make_entrymd.py "Nueva Entrada"
```
El resultado será:
```bash
File created -> content/2015_02_31_nueva-entrada.md
```

Se creará un archivo similar al siguiente:
```md
Title: Nueva Entrada
Date: 2015-15-03 12:20
Tags: 
Category: 
Slug: nueva-entrada
Author: 
Summary: 
status: draft 
```
El status `draft` te permite crear artículos en estado borrador. Muy útil si aún no deseas publicar o quieres que otra persona ĺo revise. Pelican no mostrará tu artículo hasta que  borres la línea `status: draft` o la cambies por `status: published` . Hasta entonces lo guardará en la carpeta `drafts`.


## Posts con la forma: /año/mes/dia/nombre-de-post.html

Agregamos al archivo `pelicanconf.py` lo siguiente:
```python
# Formating URLs
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
```
## Generando nuestra web

Ahora ya tienes todo para escribir tus artículos y generar tu web. ¡Adelante!

#### Crea un post (si usas el script `make_entry/md.py`)
```bash
 $ python make_entrymd.py "Nombre de tu nuevo post"
```
#### Escribe un artículo
Entra a la carpeta `content`, abre el archivo que acabas de crear y escribe un artículo. Yo estoy usando [Haroopress](http://pad.haroopress.com/user.html) un procesador para Markdown que te permite ver los cambios en tiempo real mientras escribes. También puedes usar Vim, Emacs o SublimeText.

#### Genera tu web
```bash
$ cd blog
$ make devserver
```
Puedes ver los cambios en tu blog entrando en: http://localhost:8000 

Y para salir escribe:

```bash
$ make stopserver
```
#### Empuja los cambios a tu repositorio
Recuerda hacerlo desde la carpeta output
```bash
$ cd output
$ git add --all
$ git commit -m "commit message"
$ git push origin master
```
Visita tu web.

# FIN

## Comandos extras en caso de accidentes

#### Inicializar repositorio 
```bash
$ cd output
$ git init
$ git remote add origin https://github.com/username/username.github.io.git
```

####Restaurar repositorio
```bash
$ cd blog
$ git clone https://github.com/username/username.github.io.git output
$ pelican content
$ cd output
$ git add --all
$ git commit -m "commit message"
$ git push origin master
```

## Referencias
* [Observa el archivo pelicancof.py y publishconf.py de DandyDev creador de plantilla Booostrap3](https://github.com/DandyDev/dandydev.net)
* [Cheat Sheet para Markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
* [Amy Hanlon, Migrating to Github Pages using Pelican](http://mathamy.com/migrating-to-github-pages-using-pelican.html).
* [Pelican Boostrap3 Theme](https://github.com/DandyDev/pelican-bootstrap3)












