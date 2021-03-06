# Bar Power

[![CircleCI Tests Status](https://circleci.com/gh/alexespana/barpower.svg?style=svg)](https://circleci.com/gh/alexespana/barpower)
[![readme workflow](https://github.com/alexespana/barpower/actions/workflows/sync.yml/badge.svg)](https://github.com/alexespana/barpower/actions/workflows/sync.yml)
[![docker workflow](https://github.com/alexespana/barpower/actions/workflows/build.yml/badge.svg)](https://github.com/alexespana/barpower/actions/workflows/build.yml)
[![versions workflow](https://github.com/alexespana/barpower/actions/workflows/versions.yml/badge.svg)](https://github.com/alexespana/barpower/actions/workflows/versions.yml)

## Descripción general del proyecto :memo:
La idea de este proyecto será desarrollar un software para ayudar a maximizar la productividad, y por lo tanto la competitividad de los locales
donde se sirva comida, ya sea bares, cafeterías, pizzerías, etc.

A través de las visitas que se vayan realizando al bar, la aplicación irá registrando las comidas, meriendas o cenas que se produzcan, almacenando 
datos como la hora del pedido, el pedido realizado y su precio, con lo que se podrá ofrecer al dueño del bar datos objetivos sobre qué ofrecer y 
mejorar las ganancias del bar.

Se entiende por maximizar las ganancias del bar como vender el mayor número de productos (a ser posible los más caros) en el menor tiempo posible, siempre
por medio de la detección de la aplicación del momento en el que éstas se pueden maximizar atendiendo al tipo de pedidos que se realizan y la clasificación 
que se hace de los clientes.
 
En definitiva, se trata de aumentar el margen de beneficio que los dueños de los bares suelen tener.

---

## ¿Por qué hacer este proyecto? :bulb:
Esta idea ha venido motivada principalmente porque en numerosas ocasiones he visto que bares, cafeterías, pizzerías, etc.., no 
tenían una afluencia adecuada de clientes, no porque sirvieran mala comida sino porque no se preguntaban, ¿qué es lo que a 
nuestros clientes les gusta?, ¿cuáles son los tipos de clientes con los que obtenemos mayor beneficio?. 
Con este proyecto dichos problemas podrían reducirse, aumentando así la productividad y competitividad de estos lugares.

---

## Historias de usuario :busts_in_silhouette:
Enlaces a las distintas historias de usuario (HU):
* [[HU1]. Anotar clientes y comandas](https://github.com/alexespana/BarPower/issues/9)
* [[HU2]. Predicción de jóvenes](https://github.com/alexespana/BarPower/issues/10)
* [[HU3]. Productos más consumidos en función del cliente](https://github.com/alexespana/BarPower/issues/3)
* [[HU4]. Predicción de ancianos](https://github.com/alexespana/BarPower/issues/4)

---

## Task runners y gestores de dependencias
Para este proyecto se ha decidido utilizar **poethepoet** como gestor de tareas y **poetry** como gestor de dependencias. La justificación
de la elección se puede ver reflejada en la documentación adicional al final del documento.

### Poetry
Para la instalación de poetry en Linux debes abrir una terminal y ejecutar el siguiente comando:

    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

Si quieres comprobar que se ha instalado correctamente, abre una nueva terminal y ejecuta:

    poetry --version

Comandos obtenidos de la [documentación](https://python-poetry.org/docs/#installation) de poetry.

### Poethepoet
Para que poethepoet funcione dentro del entorno de poetry es necesario abrir una terminal y ejecutar el siguiente comando:

    poetry add --dev poethepoet

Para la instalación de poethepoet en tu entorno de python por defecto debes abrir una terminal y ejecutar el siguiente comando:

    pip install poethepoet

Si quieres comprobar que se ha instalado correctamente ejecuta en la terminal:

    poe --version

Comandos obtenidos de la [documentación](https://pypi.org/project/poethepoet/) de poethepoet.


### Clase Visits
Esta clase almacenará la información relativa a las visitas que realizan los clientes a lo largo del día en el local. Almacenará los 
tipos de clientes que estén en un momento dado en el bar junto a las horas de llegada, además, almacenará las distintas comandas 
que se realizan por parte de los clientes junto a las horas que se realizan. Esta clase será la encargada de dar toda la lógica de 
negocio de la aplicación, realizando predicciones(usando un teorema probabilístico de Bayes) acerca de la futura presencia de 
determinados tipos de clientes y generando informes sobre los productos más consumidos según tipo de cliente.

Para instalar la clase debes ejecutar:

    poe install

Para instalar las dependencias necesarias ejecutar:
    
    poe installdeps

Para comprobar que el resultado de la ejecución es correcto ejecutar:

    poe test

Para comprobar la sintaxis de esta clase debes ejecutar:
    
    poe check

Si desea visualizar las tareas disponibles puede ejecutar:

    poe --help

### ¿Por qué usar pytest para testear?
A la hora de la elección del marco de pruebas se planteó la elección de unittest, sin embargo, este marco de prueba tiene una sintaxis más compleja 
y menos legible en comparación con pytest. En el caso de unittest, para testear tendría que crearse una subclase de unittest.TestCase (es decir, que 
heredase de ella), por lo que tendríamos que depender de ello.

El marco de prueba **pytest** tiene una sintaxis más simple, incluye mayor información en el caso de fallo de los tests, y además incluye lo que se 
denominan **fixtures**, que son objetos que si no se crean correctamente, indican que algo va mal, pero si se crean correctamente, se usan como base 
para los tests posteriores. Con respecto a la biblioteca de aserciones se ha decidido usar la de pytest, que comprueba que la expresión pasada como 
argumento es cierta con simplemente hacer **assert <expresion lógica>**

### Fases de test: setup, test y teardown
En este caso, se va a testear la clase Visits. Voy a explicar el procedimiento que seguiremos para realizar los test:
* **Setup**: en esta fase se crean los objetos necesarios para llevar a cabo los test. En nuestro caso, se crea un fixture que será **visits** 
en la función visits(). Si la creación de este objeto se realiza correctamente, será la base para los test siguientes.
* **Tests**: sobre el fixture creado en la fase de setup se llevarán a cabo los tests. Recordar que estos test son independientes de la 
implementación, por lo que debe comprobar comportamiento.
* **Teardown**: en esta fase se eliminan todos los archivos temporales(\__pycache__, .pytest_cache) y se deja al sistema en el estado inicial, para
ello se puede usar la orden **poe clean**.

Como hemos indicado anteriormente, para realizar los test hay que ejecutar:

    poe test

---

## Contenedor para pruebas
Para la creación de nuestro contenedor de pruebas se han seguido una serie de pasos reflejados en la creación del archivo Dockerfile. Como contenedor 
base se ha elegido el oficial de python, en la versión 3.8, ya que es la última versión de python que no está en [modo de corrección de errores](https://devguide.python.org/devcycle/) 
(lo que la hace una versión estable). Lo primero que necesitamos para realizar los test correctamenete dentro de la imagen es tener instaladas las 
herramientas necesarias para ello, por lo que hemos instalado el task runner y el gestor de dependencias (poetthepoet y poetry respectivamente). Además, 
necesitamos que el archivo **pyproject.toml** esté incluido en una carpeta de la imagen, ya que de aquí obtendrá las dependencias (como pytest) que hagan
falta para ejecutar los test. Posteriormente, como acabamos de mencionar, instalamos los módulos/bibliotecas de test a través del task runner. Finalmente, 
ejecutamos los test a través del task runner. 

Al crear la imagen del contenedor he observado que el tamaño de ésta era excesivamente grande (992MB), por lo que he optado por usar una variante contenedor 
base de python más ligera, **python slim**, consiguiendo reducir el tamaño de la imagen significativamente (204MB), haciéndola más ligera.

### ¿Cómo probarlo?
Para probar el correcto funcionamiento del contenedor deberemos descargar este repositorio  y ejecutar dentro de la carpeta raíz del mismo lo siguiente:

    docker run -t -v `pwd`:/app/test alexespana/barpower

En este comando, la opción -t indica cómo Unix/Linux maneja el acceso a la terminal y la opción -v concretamente lo que hace es montar el directorio
local en el que se encuentra a la carpeta /app/test de la imagen, es por esta razón que no ha sido necesario incluir ningún fichero de test ni código fuente 
en la creación de la imagen. La imagen se encuentra almacenada en Dockerhub y puedes acceder a ella [aquí](https://hub.docker.com/r/alexespana/barpower).

---

## Sistema de integración continua
Nuestros sistemas de integración continua deben de cumplir con una serie de **requisitos** para su aceptación:
* Que sean sencillos de configurar, tanto para pasar los tests automáticamente como para probar con distintas versiones del lenguaje la aplicación.
* Que el checks API pueda ser configurado fácilmente
* Que no se requiera introducir una tarjeta de crédito.

Hoy en día existe una gran variedad de sistemas de integración continua que pueden usarse para nuestros proyectos, entre los que se pueden encontrar los siguientes:
* Github Actions
* Travis
* Circle CI
* Semaphore CI
* AppVeyor
* Jenkins

Teniendo en cuenta ésto, vamos a realizar una **búsqueda parametrizada** de los sistemas de integración continua que cumplen los requisitos especificados más arriba.
Comenzaremos eligiendo el necesario para pasar los tests automáticamente y posteriormente el segundo sistema de CI, necesario para testear la aplicación con 
distintas versioens del lenguaje.

1. Atendiendo a la facilidad de uso y lo estándar que es el sistema, **Travis** es probablemente el más recomendado de usar, ya que permite ver el resultado de la integración 
continua en la misma página de Github (**checks API**) de manera muy sencilla. Sin embargo, dado que para darse de alta exigen tarjeta de crédito (lo cual no todo el mundo posee), 
se ha descartado como opción. Dado que en el objetivo anterior se usó **Github Actions** para configurar la sincronización del README y la actualización del docker, he decidido 
descartar usarlos ya que en los tests de la asignatura se comprobará que se haya configurado un sistema de integración continua distinto a Github Actions (que es un falso 
positivo). Siguiendo con la comparativa de los sistemas de CI disponibles, si tuviéramos que elegir entre **Circle CI** y **Semaphore CI**, Circle CI es más aceptado por la comunidad.
Además de ésto se ha comprobado cuál de los dos es el más utilizado actualmente mediante distintos rankings como [este](https://cprimestudios.com/blog/top-cicd-tools-2021-most-complete-guide-33-best-picks-devops) o [este](https://www.slant.co/topics/799/~best-continuous-integration-tools), en el que CircleCI se
encuentra en la 3ª posición y SemaphoreCI en la 16ª y en el que CircleCI está en la 5ª posición y SemaphoreCI en la 10ª, respectivamente. Con respecto al resto de sistemas de CI (AppVeyor y Jenkins), decir que **Jenkins** es el más popular actualmente, sin embargo, no es sólo un sistema de integración continua sino que además es un sistema de entrega/implementación continua, por lo que se ha descartado como opción.

    Tras esta comparación, he decidido usar como primer sistema de integración continua **CircleCI** ya que es sencillo de usar, fácilmente configurable, permitiendo incluir fácilmente 
el [checks API](https://circleci.com/docs/2.0/enable-checks/), de forma que se puedan ver los resultados de la integración continua en Github. Además, nos permite crear y editar el archivo de configuración de la integración continua, llamado **config.yml** desde su interfaz web, corrigiendo errores sintácticos y permitiendo hacer commits del archivo directamente a la rama en la que nos encontremos.

2. Otro de los puntos a cubrir de la integración continua es comprobar con qué versiones del lenguaje funciona nuestra aplicación. Para ello, he decidido usar como segundo sistema de CI las 
Github Actions de Github, entre otras cosas porque al buscar un poco de información sobre el uso de la **matrix** he podido comprobar que la configuración es muy sencilla, pudiendo 
encontrar una muy buena documentación respecto al tema en estas páginas oficiales de Github: [referencia 1](https://docs.github.com/es/actions/learn-github-actions/managing-complex-workflows) y 
[referencia 2](https://docs.github.com/es/actions/learn-github-actions/workflow-syntax-for-github-actions#jobsjob_idstrategymatrix). Además, es obvia la gran integración que tienen con 
Github, no necesitando ningún tipo de configuración previa para poder ver el resultado de los workflows.

Para más información acerca de la configuración de los sistemas de integración continua, visite la documentación adicional incluida al final de este archivo.

---

## Servicios esenciales en la nube
### Registro de actividad (logger)
Añadir un sistema de logs a una aplicación es algo fundamental para poder controlar los eventos que se van sucediendo en ésta, ya sea para comprobar el funcionamiento normal de la aplicación
o el posible funcionamiento erróneo de la misma.

Teniendo ésto en cuenta, debemos añadir un servicio de logs a la aplicación que cumpla los siguientes requisitos a ser posible:
* Que permita modificar fácilmente el formato de los mensajes mostrados.
* Que permita redirigir los mensajes a un fichero de logs.
* Que permita distinguir entre distintos tipos de mensajes de logs (niveles).
* Que el software sea habitualmente mantenido por la comunidad.
* Que sea fácil de integrar y configurar con python.

Tras realizar una búsqueda en profundidad de los distintos sistemas de logs disponibles para python, no he encontrado una gran variedad, se planteó usar una versión de
[pinojs](https://github.com/pinojs/pino) versionada para python, [pino.py](https://github.com/CoorpAcademy/pino.py), sin embargo, no es una buena opción ya que es un prototipo en construcción 
y la API podría cambiar, además de que no cumple con el requisito de que sea habitualmente mantenida (último commit hace más de un año).

En algunos lenguajes como python, existen facilidades para el registro de logs incluidas directamente en la librería básica. Python incluye un módulo [**logging**](https://docs.python.org/es/3.8/howto/logging.html) para el registro de actividad, proporcionando distintas funciones que se usan de acuerdo al nivel de los eventos que se suceden en la aplicación. Teniendo por lo tanto cuatro niveles posibles: DEBUG, INFO, WARNING, ERROR y CRITICAL, ordenados en orden creciente de gravedad. Además de lo mencionado, permite una gran flexibilidad para modificar el formato de los mensajes de logs. Por último, permite redirigir los mensajes de logs fácilmente a un fichero incluyendo en el método de configuración (**basicConfig**) un parámetro **filename** que indica el ficho al que redirigir el registro de actividad.

Teniendo en cuenta lo mencionado anteriormente se ha decidido usar como sistema de logs el módulo **logging** de python, éste cumple con todos los requisitos que hemos especificado
al inicio, además de que sigue siendo software mantenido y realmente fácil de configurar.

### Servicio de configuración remota
Otro de los puntos a tener en cuenta para nuestra aplicación es tener un sistema de configuración distribuida. En este caso, el único requisito que necesito para este sistema de configuración
distribuida es que sea sencillo de configurar. 

Actualmente no hay muchas alternativas (como bien dice [aquí](http://jj.github.io/CC/documentos/temas/Configuracion_microservicios)), teniendo por un lado **etcd3** y **consul**. Etcd3 es un sistema de almacenamiento clave/valor que permite configurar aplicaciones de una forma sencilla funcionando sobre un puerto conocido y accesible, mientras que consul es una herramienta bastante más compleja de 
configurar. Por esta razón se ha decidido usar **etcd3** directamente, como se nos recomendó en clase de teoría. Es importante tener en cuenta que en esta fase estamos realizando la configuración del cliente, por lo que la petición al servidor fallará al intentar obtener las variables del servidor, teniendo que utilizar por lo tanto un módulo en caso de excepción que se describe a continuación.

Además del sistema de configuración distribuida, la configuración necesita usar las variables de configuración y los ficheros de entorno que igualmente siguen el formato clave/valor en el caso en el que el servidor no esté configurado, por lo que será necesario usar un módulo como **dotenv**, que permita cargar las variables de entorno que estén escritas en un fichero **.env**. 

## Documentación adicional :books:
[Enlace a documentación](docs/documentacion.md)