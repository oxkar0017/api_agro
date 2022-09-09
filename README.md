# api_agro

API que permite el ingreso, impresión, actualización y borrado de registros de temperatura y humedad que registran unos sensores.

## CRUD

- Para realizar un `GET` de todos los registros:
   ```cmd
   >> curl https://api-agro-ok.herokuapp.com/registros
   ```
- Para realizar un `GET` de un registro `<id_registro>`:
   ```cmd
   >> curl https://api-agro-ok.herokuapp.com/registros/<id_registro>
   ```
- Para realizar un `PUT` especificanfo un registro `<id_registro>`, un valor `<valor>` y un tipo asociado al valor `<tipo>`, ya sea temperatura o humedad:
   ```cmd
   >> curl -X PUT https://api-agro-ok.herokuapp.com/registros/<id_registro>?valor=<mi_valor>"&"tipo=<mi_temperatura>
   ```
- Para realizar un `POST` de un registro nuevo de un valor `<valor>` y un tipo asociado al valor `<tipo>`, ya sea temperatura o humedad:
   ```cmd
   >> curl -X POST https://api-agro-ok.herokuapp.com/registros?valor=<mi_valor>"&"tipo=<mi_temperatura>
   ```
- Para realizar un `DELETE` de un registro `<id_registro>`:
   ```cmd
   >> curl -X DELETE https://api-agro-ok.herokuapp.com/registros/<id_registro>
   ```

## Problemas

Durante la prueba de realizar creaciones y actualizaciones continuas, se evidencia en el `GET` que la información no se almacena de manera adecuada, en un momento se muestran registros nuevos y en otros momentos desaparecen.
