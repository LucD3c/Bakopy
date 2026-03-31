# 🗂️ Bakopy
### Backup simple e inteligente — sin instalación, sin complicaciones.

Bakopy es una herramienta gratuita y de código abierto que te permite hacer
backups de tus carpetas de forma ordenada y segura. Seleccionás las carpetas,
elegís dónde guardar, y Bakopy copia y organiza todo automáticamente.

**Todo ocurre dentro de tu propia computadora. Nada sale a internet.**

---

## ¿Qué hace Bakopy?

- Copia las carpetas que vos elegís a una ubicación segura dentro de tu PC
- Organiza los archivos automáticamente por tipo (Documentos, Imágenes, Videos, etc.)
- Crea una carpeta por cada backup con la fecha y hora exacta
- Verifica que tenés espacio suficiente antes de copiar
- Lleva un historial de todos tus backups
- Funciona igual en Windows y Linux

---

## Requisitos

- **Python 3.8 o superior**
  - Windows: descargalo desde https://www.python.org/downloads/
  - Linux (Ubuntu/Debian): ya viene instalado. Si no: `sudo apt install python3 python3-venv`
- Nada más.

---

## Instalación y uso

### En Windows

**1. Descargá el repositorio**

Opción A — Con Git:
```
git clone https://github.com/TU_USUARIO/Bakopy.git
```

Opción B — Sin Git:
Hacé clic en el botón verde **Code** en GitHub y seleccioná **Download ZIP**.
Descomprimí el archivo descargado.

**2. Abrí una terminal dentro de la carpeta**

Hacé clic derecho dentro de la carpeta `Bakopy` y seleccioná
"Abrir en Terminal" o "PowerShell aquí".

**3. Creá el entorno virtual**
```
python -m venv venv
```

**4. Activá el entorno virtual**
```
venv\Scripts\activate
```

**5. Instalá Flask**
```
pip install flask
```

**6. Iniciá Bakopy**
```
python bakopy.py
```

Se abrirá automáticamente tu navegador con la aplicación lista para usar.

---

### En Linux (Ubuntu / Debian)

**1. Cloná el repositorio**
```bash
git clone https://github.com/TU_USUARIO/Bakopy.git
cd Bakopy
```

**2. Creá el entorno virtual**
```bash
python3 -m venv venv
```

**3. Activá el entorno virtual**
```bash
source venv/bin/activate
```

**4. Instalá Flask**
```bash
pip install flask
```

**5. Iniciá Bakopy**
```bash
python bakopy.py
```

Abrí tu navegador y entrá a: `http://localhost:5099`

> Si accedés desde otra computadora en la misma red, usá la IP
> de la máquina donde corre Bakopy: `http://IP_DEL_SERVIDOR:5099`

---

## Cómo usar Bakopy paso a paso

### Primer uso — Configuración inicial

La primera vez que abrís Bakopy verás la pantalla de bienvenida.

**1. Ingresá un nombre para tu carpeta de backups**

Escribí el nombre que quieras darle a la carpeta donde se guardarán
todos tus backups. Por ejemplo: `MisBackups`, `Respaldos`, `Backup2026`.

**2. Seleccioná dónde crear esa carpeta**

Hacé clic en "Seleccionar ubicación" y navegá hasta la carpeta donde
querés guardar tus backups. Puede ser:
- Una carpeta dentro de tu disco principal
- Un disco externo conectado a tu PC
- Una carpeta compartida en red

**3. Hacé clic en "Crear carpeta y empezar"**

Bakopy crea la carpeta automáticamente y quedás listo para usar la herramienta.

---

### Crear un nuevo backup

Una vez configurada la herramienta verás la pantalla principal con dos secciones:
**Nuevo backup** e **Historial**.

**1. Agregá las carpetas que querés respaldar**

Hacé clic en **+ Agregar carpeta** y navegá hasta la carpeta que querés
incluir en el backup. Podés agregar tantas carpetas como quieras.

Ejemplos de carpetas útiles para respaldar:
- Documentos
- Escritorio
- Fotos
- Música
- Proyectos de trabajo

**2. Verificá el espacio disponible**

Al agregar carpetas, Bakopy muestra automáticamente:
- Cuánto espacio necesita el backup
- Cuánto espacio disponible tenés en disco
- Una barra de color que indica si hay espacio suficiente

  - 🟢 Verde: hay espacio de sobra
  - 🟡 Amarillo: hay espacio pero justo
  - 🔴 Rojo: no hay espacio suficiente

Si no hay espacio, el botón "Crear backup ahora" queda desactivado
y te informa exactamente cuánto espacio falta.

**3. Hacé clic en "Crear backup ahora"**

Bakopy empieza a copiar los archivos. Mientras trabaja verás una barra
de progreso. **No cierres la aplicación ni el navegador** hasta que termine.

**4. Resultado del backup**

Al terminar verás un resumen con:
- Cantidad de archivos copiados
- Tamaño total del backup
- Categorías de archivos encontrados
- Advertencias si algún archivo no pudo copiarse (por permisos, etc.)

---

### ¿Cómo se organizan los archivos?

Cada backup se guarda en una subcarpeta con la fecha y hora exacta:
```
MisBackups/
└── 2026-03-31_19-45-00/
    ├── Documentos/       ← PDF, Word, Excel, TXT, CSV...
    ├── Imagenes/         ← JPG, PNG, GIF, RAW...
    ├── Videos/           ← MP4, AVI, MKV, MOV...
    ├── Musica/           ← MP3, FLAC, WAV, AAC...
    ├── Codigo/           ← PY, JS, HTML, SQL...
    ├── Comprimidos/      ← ZIP, RAR, 7Z, TAR...
    └── Otros/            ← Todo lo que no entra en las categorías anteriores
```

Si hacés otro backup mañana, se crea una nueva carpeta:
```
MisBackups/
├── 2026-03-31_19-45-00/
└── 2026-04-01_10-20-00/
```

Cada backup es completamente independiente del anterior.

---

### Historial de backups

Hacé clic en la pestaña **Historial** para ver todos tus backups anteriores.

Por cada backup podés ver:
- Fecha y hora en que se realizó
- Estado (Completado / Con errores)
- Cantidad de archivos copiados
- Tamaño total
- Cuántas carpetas origen se incluyeron
- Desglose por categoría de archivos
- Ruta donde están guardados los archivos

#### Eliminar un backup

Tenés dos opciones:

- **Eliminar registro**: borra solo el registro del historial. Los archivos
  del backup siguen en tu disco y podés acceder a ellos normalmente.

- **Eliminar registro y archivos**: borra el registro del historial
  Y todos los archivos de ese backup. Útil para liberar espacio.

---

### Llevar el backup a un pendrive o disco externo

La carpeta de backups que creaste al inicio es una carpeta normal en tu disco.
Podés copiarla o moverla a donde quieras:

1. Conectá tu pendrive o disco externo
2. Copiá la carpeta `MisBackups` (o el nombre que le hayas dado) al dispositivo
3. Listo — tenés tu backup portable

---

## Estructura del proyecto
```
Bakopy/
├── bakopy.py          ← Punto de entrada. Ejecutá este archivo para iniciar
├── core/
│   ├── backup.py      ← Motor de copia y organización de archivos
│   ├── space.py       ← Cálculo de espacio disponible en disco
│   └── scanner.py     ← Clasificación de archivos por tipo
├── data/
│   ├── db.py          ← Base de datos SQLite (historial y configuración)
│   └── bakopy.db      ← Archivo de base de datos (se crea automáticamente)
├── ui/
│   ├── app.py         ← Servidor Flask con todos los endpoints
│   └── templates/
│       └── index.html ← Interfaz de usuario completa
├── venv/              ← Entorno virtual Python (no se sube a GitHub)
├── requirements.txt   ← Dependencias del proyecto
└── README.md          ← Este archivo
```

---

## Preguntas frecuentes

**¿Mis archivos salen a internet?**
No. Bakopy funciona 100% en local. El servidor Flask solo escucha en tu
red local y no se conecta a ningún servicio externo.

**¿Puedo cerrar el navegador mientras hace el backup?**
No. El navegador es la interfaz de Bakopy. Si lo cerrás durante un backup
en progreso, la copia podría quedar incompleta.

**¿Qué pasa si ya existe un archivo con el mismo nombre?**
Bakopy lo renombra automáticamente agregando un número al final.
Por ejemplo: `foto.jpg` → `foto_1.jpg`. Ningún archivo se sobreescribe.

**¿Puedo respaldar carpetas de un disco externo?**
Sí. Conectá el disco externo, hacé clic en "+ Agregar carpeta" y
navegá hasta las carpetas del disco externo.

**¿Dónde se guarda la configuración?**
En el archivo `data/bakopy.db` dentro de la carpeta del proyecto.
Si borrás ese archivo, Bakopy te pedirá configurar la carpeta de
backups nuevamente la próxima vez que lo abras.

---

## Licencia

MIT — libre para usar, modificar y compartir.
