# Tarea 3 Bases de datos | INF-239 | Grupo 40

# Ares Galaxy (Penquify para terminos comerciales)

# Miembros

## José Llanos | ROL: 202073103-9
## Kirk Heim | ROL: 201903009-4

# Link GitHub
`GitHub` : <https://github.com/jllanosg/tarea3bbdd>


# ❗  Importante ❗
## Se debe crear un archivo credenciales.py con el siguiente formato:
```python
usuario = ""
clave = ""
nombre_bd = ""
```
Donde cada string contenga la credencial que le corresponda para conectarse a la base de datos.

# Link Postman
`Postman` : <https://documenter.getpostman.com/view/21979254/UzQvu5mS>


# Supuestos
- Las consultas HTTP en json siempre van a contener todos los atributos necesarios.
- Para el top global no se consideran las canciones sin reproducciones, ya que complicaría la consulta.

# Dificultades y tiempos

- Lidiar con el dolor de espalda.

## To-do
- [X] Reparar mensajes de estado 404 (not found) y 400 (bad request).
- [ ] En endpoint moroso, que verifique que el usuario exista.
- [ ] Publicar **bien** la documentación final en postman.
- [ ] Agregar dump final a la entrega.
## Extras
- Se agregó un endpoint que consulta a la BBDD sobre la cantidad de usuarios y canciones, para ser mostradas en PowerBI.
