# 🚀 Workflow Profesional en Linux para Jupyter Notebook

Gestión eficiente de entornos virtuales y aislamiento de kernels para proyectos de Ciencia de Datos con Jupyter Notebook. Este flujo de trabajo permite mantener el sistema operativo limpio y los proyectos completamente organizados y aislados.

---

## 📑 Índice

- Las Fases del Flujo de Trabajo
- Setup Inicial y Dependencias
- La Magia del Kernel
- Ejecución y Trabajo Diario
- Finalización Segura
- El Flujo del "Día 2" (Retomar el Proyecto)
- Nuevas Instalaciones
- Gestión de Archivos (CSV)
- Resumen Rápido (Cheatsheet)

---

## 🧭 Las Fases del Flujo de Trabajo

Este workflow se divide en tres etapas principales:

- **Configuración:** creación del entorno virtual (`venv`) dentro del proyecto.
- **Vinculación:** registro del entorno como un Kernel de Jupyter.
- **Ejecución:** trabajo diario sin depender de activar manualmente el entorno virtual cada vez.

---

## 🛠️ Setup Inicial y Dependencias

Primero, crea la carpeta del proyecto y su entorno virtual aislado desde la Terminal.

```bash
cd projects

mkdir labs

cd labs
```

```bash
python3 -m venv env_labs
```


Activa el entorno virtual e instala las dependencias necesarias. Es importante instalar `ipykernel` despues, ya que permitirá registrar el entorno como un Kernel de Jupyter.

```bash
source env_labs/bin/activate
```

```bash
pip install ipykernel pandas numpy matplotlib seaborn scikit-learn pyjanitor fg-data-profiling --quiet
```

---

## ✨ La Magia del Kernel

Con el entorno virtual aún activo, ejecuta el siguiente comando para registrar el Kernel en Jupyter.

```bash
python -m ipykernel install --user --name=env_labs --display-name="Python (env_labs)"
```

### ¿Qué hace este comando?

- `--name`: identificador interno del Kernel. Se recomienda utilizar el nombre del entorno virtual.
- `--display-name`: nombre que aparecerá en el selector de Kernels dentro de Jupyter Notebook.

Una vez registrado, el Kernel quedará disponible de forma permanente hasta que sea eliminado manualmente.

---

## 💻 Ejecución y Trabajo Diario

Inicia Jupyter Notebook desde la terminal.

```bash
jupyter notebook
```

Luego:

1. Haz clic en **New**.
2. Selecciona **Python (env_labs)**.
3. Ya nos abre un ipynb nuevo listo para trabajar.

A partir de ese momento, todas las librerías instaladas en el entorno virtual estarán disponibles únicamente para ese proyecto.

---

## 🛑 Finalización Segura

Al finalizar el trabajo:

1. Guarda el notebook mediante **File → Save** o con el icono del disquete.
2. Cierra completamente la pestaña del navegador.
3. Detén el servidor de Jupyter presionando `Ctrl + C` en la terminal y confirma escribiendo `y`.

Finalmente, desactiva el entorno virtual.

```bash
deactivate
```

---

## 🔄 El Flujo del "Día 2" (Retomar el Proyecto)

Aquí es donde este workflow muestra su mayor ventaja.

Ya no necesitas instalar librerias pero si, **activa el entorno virtual para utilizar modo oscuro y configuraciones**.

Simplemente navega hasta el proyecto.

```bash
cd ~/projects/labs
```

```bash
source env_labs/bin/activate
```

```bash
jupyter notebook
```

Al abrir el archivo `.ipynb`, Jupyter cargará automáticamente el Kernel correcto, utilizando el entorno virtual asociado al proyecto.

### 🏆 Regla de Oro

> **1 Proyecto = 1 Entorno Virtual = 1 Kernel**

Cada proyecto debe tener su propio entorno virtual y su propio Kernel registrado. Esto evita conflictos entre versiones de librerías y mantiene los proyectos completamente aislados.

---

## 📦 Nuevas Instalaciones

### ¿Cuándo es necesario activar nuevamente el entorno?

Para instalar una nueva librería en un proyecto existente, y para trabajar con nuestro tema oscuro y configuraciones.

Por ejemplo, si olvidaste instalar `matplotlib`:

```bash
source nombre_entorno/bin/activate

pip install matplotlib

jupyter notebook
```

Después de instalar la librería, el Kernel seguirá utilizando automáticamente la nueva dependencia.
Otra forma podria ser %pip install scipy sin necesidad de activar el entorno pero si seleccionando el kernel creado.

---

## 📁 Gestión de Archivos (CSV)

El explorador de archivos de Jupyter funciona en tiempo real.

Puedes copiar o arrastrar archivos `.csv` directamente dentro de la carpeta `labs` utilizando el gestor de archivos de tu sistema operativo.

No importa si Jupyter Notebook ya está abierto; los archivos aparecerán automáticamente y podrán utilizarse inmediatamente con `pd.read_csv()`.

---

## ⚡ Resumen Rápido (Cheatsheet)

| Acción | Comando |
|---------|---------|
| Crear entorno virtual | `python3 -m venv nombre_entorno` |
| Activar entorno | `source nombre_entorno/bin/activate` |
| Registrar Kernel | `python -m ipykernel install --user --name=nombre_entorno --display-name="Python (Mi Proyecto)"` |
| Iniciar Jupyter | `jupyter notebook` |
| Detener Jupyter | `Ctrl + C` y luego `y` |
| Desactivar entorno | `deactivate` |

---

## ✅ Workflow Completo

```text
Nuevo Proyecto
      │
      ▼
Crear carpeta
      │
      ▼
Crear entorno virtual (venv)
      │
      ▼
Activar entorno
      │
      ▼
Instalar librerías
      │
      ▼
Registrar Kernel
      │
      ▼
Trabajar normalmente con Jupyter
      │
      ▼
Cerrar Jupyter
      │
      ▼
deactivate
      │
      ▼
Día siguiente
      │
      ▼
cd project/labs/
      │
      ▼
source env_labs/bin/activate
      │
      ▼
jupyter notebook
      │
      ▼
El Kernel correcto se carga automáticamente con las librerias y Configuracion
```

[*Material Adicional*](https://laboratoriolinux.es/index.php/-noticias-mundo-linux-/software/40224-como-crear-un-entorno-de-desarrollo-de-inteligencia-artificial-en-linux-con-python-jupyter-y-modelos-de-codigo-abierto.html)

---

## Cambiar a Modo Oscuro

Esto podiamos haber hecho antes de instalar librerias con el entorno virtual activo, o bien en otro momento pero activando el entorno virtual como en el paso Nuevas Instalaciones (si no activamos venv igualmente nos dara un error el comando de Temas).

```bash
pip install jupyterthemes

jt -t chesterish
```

```bash
jt -t chesterish -fs 14 -nfs 12 -T -N -kl
```

Lanzamos Jupyter Notebook luego vamos a Settings -> Theme -> Jupyterlab Dark.

jt -r   para restaurar al tema original

---

## Algunos trucos

https://www.dataquest.io/blog/jupyter-notebook-tips-tricks-shortcuts/

```bash
%autosave 30
```

%matplotlib inline al principio de la celda para armar el grafico y para ejecutar comandos de bash en la celda se usa !ls
