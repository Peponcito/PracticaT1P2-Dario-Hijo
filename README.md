# PracticaT1P2-Dario-Hijo
> En esta práctica se nos pedía desarrollar una aplicación utilizando python que genere una copia del proceso en ejecución y que tenga el siguiente comportamiento:
> - El proceso padre debe preguntar al usuario cuántos procesos hijos debe ejecutar, en función del 
valor introducido por el usuario, el proceso padre se replicará tantas veces como sea necesario.
> - El proceso hijo debe mostrar su PID, esperar 5 segundos mostrar un mensaje indicando que se va a terminar y acabar su ejecución.
### Funcioanmiento de del programa:
- Cree dos funcion llamada apdre e hijo
- Dentro de la función padre se crear una variable llamda num, la cual pide al usuario el número de porcesos hijos que quiere crear, y se hace un for
que repetirá el código la veces que el usuario diga. En dicho código se creará una variable llamada newPid y se le guarda un PID, si ese pid es distinto de 0
entrará por el else y llamará la función hijo.
- En la función hijo se indica cuando se creó. Se crea un print con un mensaje y el PID que tiene. Después un sleep de 5, que hace que tarde 5 segundos
en salir el siguiente print, el cual nos dice cuando muere el hijo.
