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

Primero, crea la carpeta del proyecto y su entorno virtual aislado.

```bash
cd projects

mkdir analisis_panaderia

cd analisis_panaderia

python3 -m venv entorno_pana
```

Activa el entorno virtual e instala las dependencias necesarias. Es importante instalar también `ipykernel`, ya que permitirá registrar el entorno como un Kernel de Jupyter.

```bash
source entorno_pana/bin/activate

pip install ipykernel pandas numpy matplotlib seaborn scikit-learn
```

---

## ✨ La Magia del Kernel

Con el entorno virtual aún activo, ejecuta el siguiente comando para registrar el Kernel en Jupyter.

```bash
python -m ipykernel install --user --name=entorno_pana --display-name="Python (analisis pana)"
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
2. Selecciona **Python (analisis pana)**.
3. Guarda el archivo `.ipynb` dentro de la carpeta del proyecto.

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

Si únicamente vas a trabajar desde Jupyter Notebook, **ya no necesitas volver a activar el entorno virtual**.

Simplemente navega hasta el proyecto.

```bash
cd ~/projects/analisis_panaderia
```

Inicia Jupyter.

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

Únicamente cuando necesites instalar una nueva librería en un proyecto existente.

Por ejemplo, si olvidaste instalar `matplotlib`:

```bash
source entorno_pana/bin/activate

pip install matplotlib

jupyter notebook
```

Después de instalar la librería, el Kernel seguirá utilizando automáticamente la nueva dependencia.

---

## 📁 Gestión de Archivos (CSV)

El explorador de archivos de Jupyter funciona en tiempo real.

Puedes copiar o arrastrar archivos `.csv` directamente dentro de la carpeta `analisis_panaderia` utilizando el gestor de archivos de tu sistema operativo.

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
cd proyecto
      │
      ▼
jupyter notebook
      │
      ▼
El Kernel correcto se carga automáticamente
```
