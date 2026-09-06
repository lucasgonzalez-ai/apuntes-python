# Indicaciones i3 wm

## Instalación

```bash
sudo apt install i3
```
```bash
sudo apt install i3blocks
```

```bash
mkdir -p ~/.config/i3blocks
```

Reemplazar los archivos `config` tanto de i3 como de i3blocks, por los que tengo en este repositorio. Los mismos se encuentran en `~/.config`

Refrescar configuraciones.

## Instalar Feh (para gestionar el fondo de pantalla):

```bash
sudo apt install feh -y
```

Descargamos la imagen, ponemos en una carpeta, en este caso esta en home/Imagenes

```bash
feh --bg-scale ~/Imágenes/tu_imagen.jpg
```

*Nota: Al ejecutar esto, feh crea automáticamente un script oculto llamado ~/.fehbg que recuerda tu último fondo aplicado*

Abre tu archivo de configuración (nano ~/.config/i3/config) y agrega estas esta línea al final del documento

```bash
exec_always --no-startup-id ~/.fehbg
```


## Atajos de teclado

| Atajo | Acción |
|---|---|
| `CTRL + SUPER + L` | Bloqueo de pantalla |
| `SUPER + SHIFT + R` | Refrescar configuraciones |
| `SUPER + ENTER` | Abrir Terminal |
| `SUPER + 1/2/3` | Abrir/Moverse a espacios de trabajo |


## Documentacion

**(https://vivien.github.io/i3blocks)**

***(https://github.com/vivien/i3blocks-contrib)**

gaps 5 y 1 abajo

i3
├── dmenu       → lanzar comandos
├── dunst       → notificaciones
├── i3status    → información del sistema
├── i3bar       → barra
├── feh         → wallpaper
└── Ulauncher   → lanzador alternativo

