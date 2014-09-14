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

Estamos en la etapa de diseño, nos concentramos en la documentación de
[casos de uso](https://github.com/absorto/tianguis_django/tree/master/doc/casos_de_uso).

Se trata de descripciones más o menos detalladas de las acciones que
el usuario puede llevar a cabo en el sistema. Por ejemplo "publicar
oferta": el usuario crea una lista de productos en venta, sugiere un
lugar y hora, puede basarse en una plantilla, etc.

Los casos se documentan de manera aislada considerando que:
1. diferentes usuarios pueden darle diferentes usos al sistema,
   combinando casos a su gusto
2. aislar la funcionalidad permitirá a los programadores dividirse el
   trabajo enfocar sus esfuerzos por separado

Con un buen diseño buscaremos implementaciones. Escribir una
aplicación web parece una buena dirección, pero tal vez después sea
hasta mejor hacer una aplicación p2p, con anonimidad, encripción y
todas las bonanzas.
