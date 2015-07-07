Script simple que utiliza el API de Twitter para twittear cada hora 100 decimales de PI.

Los decimales se pueden calcular fácilmente mediante un algoritmo, pero para no reinventar la rueda se ha usado un fichero de texto que contiene los primeros 10 millones de decimales. El fichero ha sido generado con el programa PiFast32, y se llama pi.txt.

Para realizar este pequeño proyecto se ha utilizado Tweepy (http://www.tweepy.org), una librería de Python para acceder al API de Twitter.

Es necesario dar de alta la aplicación en Twitter Apps (https://apps.twitter.com), para obtener las keys necesarias para modificarlas en el código fuente.

Se ha programado la ejecución del script cada hora, utilizando el administrador de procesos cron de Linux. Lo único necesario es editar el crontab y añadir la tarea que queremos automatizar.

*crontab -e*

Y añadir la siguiente línea:

0 * * * * *ruta_de_python* *ruta_del_script*

Por ejemplo:

0 * * * * /usr/bin/python /home/usuario/pidecimal.py

Esto ejecutará el programa cada hora en punto. Más información sobre cron y crontab:

https://help.ubuntu.com/community/CronHowto

El programa está funcionando sobre un VPS y publicando decimales en la cuenta de Twitter:

http://www.twitter.com/pidecimal

Se calcula que llegará al decimal 10 millones en 4166 días.
