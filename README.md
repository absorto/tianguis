Tianguis Virtual
===============

Una aplicación que sirva de soporte para redes de comercio solidario.

Permitirá a sus usuarios:
1. ofrecer cosas en venta
2. ordenar cosas para su compra
3. coordinar lugares y horas para la entrega/recepción de cosas
   vendidas y compradas

La visión que estamos forjando del futuro incluye cooperativas de
consumo que se acuerpan para tener mejores condiciones de negociación,
con pedidos grandes que además ayudan a los vendedores a minimizar sus
esfuerzos al distribuir productos y encontrar clientela.

¿Cómo es diferente de craiglist y otros sitios de comercio en línea?

Craiglist y esos sitios no se ocupan de coordinar lugares y fechas
para entrega-recepción. Al comprador le conviene saber que cerca de él
se estará entregando mercancía que él quiere, y sumarse a la compra en
masa para obtener mejores precios. Al vendedor le conviene consolidar
viajes y hacerse de nuevos clientes a través de los que ya atiende.

Igual que craiglist, no pretendemos ocuparnos de la parte monetaria.
Pero a diferencia de ellos sí permitiremos al usuario llevar un
registro de los productos que vende y compra, y algunas herramientas
de análisis que le permitan mejor planificar.



# Estado actual #

Documentamos varios 
[casos de uso](https://github.com/absorto/tianguis_django/tree/master/doc/casos_de_uso).

Se están implementando con W2UI y flask.

## Correr este software

Clona este repositorio:
```bash
git clone https://github.com/rgarcia-herrera/tianguis.git
cd tianguis/tiangflask
```

### Ambiente virtual
Recomiendo el uso de [virtualenv](https://virtualenv.pypa.io/en/stable/). Si usas docker, vagrant o guix tal vez quieras saltarte a la sección de Dependencias de Python.

Crear un ambiente virtual:

```bash
$ virtualenv -p python3 ~/environments/tiangflask
Running virtualenv 
[...]
Installing setuptools, pip...done.
```

Activarlo:
```bash
$ source ~/environments/tiangflask/bin/activate
(tiangflask)rodrigo@cranley:~$ 
```

### Instalar las dependencias de Python
```bash
pip install -r requirements.txt
```

### Instalar Nodejs y bower
Descarga de [Nodejs](https://nodejs.org/en/download/) el binario que corresponda a tu arquitectura.

```bash
sudo su
cd /usr/local
tar --strip-components 1 -xvJf /home/rmejia/Downloads/node-v6.9.1-linux-x64.tar.xz
npm install bower
```

### Instalar las dependencias de JavaScript con bower
```bash
mkdir static
cd static
bower install semantic
```

### Mongodb

views.py tiene la configuración de la base de datos Mongo.

## Servidor web

Para ver lo que llevamos:
```bash
python views.py
```

http://127.0.0.1:5000

# Cómo colaborar #

¿Leiste los
[casos de uso](https://github.com/absorto/tianguis_django/tree/master/doc/casos_de_uso)?
¿Puedes pensar más? ¿Les falta detalle? Con confianza un fork, o
[mándanos mail](mailto:absorto@sdf.org), quedamos y podemos chatear
por IRC o en un pad, ya veremos.

También ayudaría hacer algunos diagramas y mock-ups.

Si te aventuras a hacer mock-ups en html eso estaría buenísimo.


Por otro lado ando viendo la estrategia descrita acá: http://stackoverflow.com/a/5682031




