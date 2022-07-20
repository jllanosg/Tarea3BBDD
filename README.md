# Tarea 3 Bases de datos | INF-239 | Grupo 40

## Ares Galaxy (Penquify para terminos comerciales)

## Miembros

### José Llanos | ROL: 202073103-9

### Kirk Heim | ROL: 201903009-4

## Link GitHub

`GitHub` : <https://github.com/jllanosg/tarea3bbdd>

## ❗  Importante ❗

## Se debe crear un archivo credenciales.py con el siguiente formato

```python
usuario = ""
clave = ""
nombre_bd = ""
```

Donde cada string contenga la credencial que le corresponda para conectarse a la base de datos.

## Link Postman

`Postman` : <https://documenter.getpostman.com/view/21979254/UzQvu5mS>

## Supuestos

- Las consultas HTTP (POST y PUT) en json siempre van a contener todos los atributos necesarios en su body correspondiente, ya que en un caso real la lógica por lado del cliente (formulario de la página) realizaría esta tarea de forma preliminar. Los casos donde los datos ingresados fueran incorrectos (errores de syntax) si fueron considerados.
- Para el top global no se consideran las canciones sin reproducciones, ya que complicaría la consulta.

## Dificultades y tiempos

- Como grupo se nos dificulto el hecho de tener que comprender el funcionamiento de las nuevas librerias de python, a la vez que teniamos que aprender como integrarlas con las nuevas técnologias que por su puesto tambien suponieron un desafío a la hora de utilizarlas.
- Los tiempos de trabajo se dividieron de forma anormal durante el trabajo debido a que este no permitia al edición simultanea del mismo porque solo era un archivo, por lo que la modalidad por la que se opto fue recurrir al *compartir pantalla* de la aplicación *Discord*, en la cual uno trabajaba mientras el otro observaba como se realizaban las cosas y aportaba con ideas. Además llegado el momento se nos presento la oportunidad de poder trabajar simultaneamente debido a que mientras un integrante se dedicaba a la documentación de *PostMan* el otro podia preocuparse de continuar el desarrollo del código mismo. Finalmente en las etapas finales (debido a la altura del semestre en la que nos encontramos) cada uno avanzo en lo que pudo dentro de su tiempo libre, ya sea, avanzar con el reporte de *PowerBi*, documentación *PostMan*, revisar la base de datos en *PgAdmin* o simplemente desarrolando el código en *Visual Studio Code*. En resumen nos llevo un total aproximado de 2 a 3 días realizar esta entrega en su totalidad.
- Lidiar con el dolor de espalda.
- Deficit de dinero debido a la compra de café.

### Tiempos por persona

- José: 9 horas
- Kirk: 7.5 horas

## To-do

- [X] Reparar mensajes de estado 404 (not found) y 400 (bad request).
- [X] En endpoint moroso, que verifique que el usuario exista.
- [X] Publicar **bien** la documentación final en postman.
- [X] Agregar dump final a la entrega.

## Extras

- Se agregó un endpoint que consulta a la BBDD sobre la cantidad de usuarios y canciones, para ser mostradas en PowerBI.
