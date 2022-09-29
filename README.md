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
  }
}
```


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
  }
}
```
