# TaixTracking

<p align="center">
  <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRLsF83YwtuOkgdqu3fU2UE5v57k4L_NgWjhw&usqp=CAU" alt="Implementation currently under development"/>
</p>

## Available languages
* <img src="https://cleandye.com/wp-content/uploads/2020/01/English-icon.png" height="10px" /> [English](#english)
* <img src="https://cdn-icons-png.flaticon.com/512/323/323365.png" height="10px" /> [Spanish](#castellano)

<a name="english"></a>
## <img src="https://cleandye.com/wp-content/uploads/2020/01/English-icon.png" height="15px" /> English
Tracking app for AliExpress orders

### Configuration file
The application can be configured from a configuration file in the format **json*, this file must be added as an 
environment variable under the key `CONFIG_FILE_TAIXTRACKING`.

In case the environment variable is not defined, the application will give the error `No se ha definido la variable 
de entorno CONFIG_FILE_TAIXTRACKING` has not been defined and will stop. If such a variable exists, but the file is 
not found, the error will be `No se encuentra el fichero de configuración "<filepath>"` is not found and will also stop.

Format of the configuration file:
```json
{
  "telegram": {
    "token": "xxx"
  },
  "application": {
    "users": {
      "allow_new_users": true,
      "default_allow": true
    }
  },
  "bbdd": {
    "system": "sqlite",
    "filepath": "taixTracking.db"
  }
}
```

### Telegram commands
If we have the telegram token well configured, it is possible to interact with the application through the messaging 
app. Here is a list of available commands:
* `/aliexpress`: allows us to obtain the status of an AliExpress order through its tracking code.

### Database manager
Currently the only database manager that is supported is SQLite. To configure it is as simple as adding the `bbdd`
section to the configuration, in the `system` field indicate `sqlite` and in the `filepath` field indicate the path
where the BBDD file is located (if it does not exist, create it).


<a name="castellano"></a>
## <img src="https://cdn-icons-png.flaticon.com/512/323/323365.png" height="15px" /> Castellano
Aplicación de seguimiento para pedidos de AliExpress

### Archivo de configuración
La aplicación se puede configurar desde un archivo de configuración con el formato **json**, dicho archivo se tiene que
añadir como una variable de entorno bajo la clave `CONFIG_FILE_TAIXTRACKING`.

En el caso de que la variable de entorno no se encuentre definida, la aplicación dará el error `No se ha definido la 
variable de entorno CONFIG_FILE_TAIXTRACKING` y se detendrá. En el caso de existir dicha variable, pero no encontrarse 
el fichero, el error será `No se encuentra el fichero de configuración "<dirección del fichero>"` y también se detendrá.

Formato del fichero de configuración:
```json
{
  "telegram": {
    "token": "xxx"
  },
  "application": {
    "users": {
      "allow_new_users": true,
      "default_allow": true
    }
  },
  "bbdd": {
    "system": "sqlite",
    "filepath": "taixTracking.db"
  }
}
```

### Comandos de Telegram
Si tenemos el token de telegram bien configurado, es posible interactuar con la aplicación a través de la aplicación
de mensajería. Esta es una lista de los comandos disponibles:
* `/aliexpress`: nos permite obtener el estado de un pedido de AliExpress a través de su código de seguimiento.

### Gestor de base de datos
Actualmente el único gestor de base de datos que está soportado es SQLite. Para configurarlo es tan sencillo como 
añadir a la configuración el apartado `bbdd`, en el campo `system` indicar `sqlite` y en el campo `filepath` indicar
la ruta donde se encuentra (si no existe lo crea) el fichero de BBDD.
