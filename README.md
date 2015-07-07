Para realizar este pequeño proyecto se ha utilizado Tweepy (http://www.tweepy.org), una librería de Python para acceder al api de Twitter.

Es necesario dar de alta la aplicación en Twitter Apps (https://apps.twitter.com), para obtener las keys necesarias para modificarlas en el código fuente.

Se ha programado la ejecución del script cada hora, utilizando el administrador de procesos cron de Linux. Lo único necesario es editar el crontab y añadir la tarea que queremos automatizar.

crontab -e

Y añadir la siguiente línea:

0 * * * * /usr/bin/python /*ruta del script*/pidecimal.py

Esto ejecutará el programa cada hora en punto. Más información sobre cron y crontab:

https://help.ubuntu.com/community/CronHowto
