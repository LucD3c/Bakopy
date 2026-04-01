# 🗂️ Bakopy
**Backup simple e inteligente — sin complicaciones.**

Bakopy es una herramienta gratuita y de código abierto que copia y organiza
tus archivos importantes en una carpeta segura dentro de tu propia computadora.
Sin configuraciones complejas, sin cuentas, sin internet. Solo seleccionás las
carpetas que querés respaldar y Bakopy hace el resto.

---

## ¿Para qué sirve?

¿Tenés fotos, documentos, proyectos o música dispersos por toda la computadora?
Bakopy los reúne en un solo lugar, organizados por tipo, con la fecha y hora
exacta de cada backup. Si algo sale mal, sabés exactamente dónde están tus archivos
y cuándo fueron respaldados.

**Todo ocurre dentro de tu propia PC. Nada sale a internet.**

---

## ¿Cómo funciona?

1. Abrís Bakopy y creás una carpeta donde se guardarán todos tus backups
2. Seleccionás las carpetas que querés respaldar
3. Bakopy verifica que tenés espacio suficiente en disco
4. Copia y organiza todo automáticamente por tipo de archivo
5. Cada backup queda guardado con fecha y hora exacta

Resultado en tu disco:
```
MisBackups/
├── 2026-03-31_19-45-00/
│   ├── Documentos/    ← PDF, Word, Excel, TXT...
│   ├── Imagenes/      ← JPG, PNG, GIF, RAW...
│   ├── Videos/        ← MP4, AVI, MKV...
│   ├── Musica/        ← MP3, FLAC, WAV...
│   ├── Codigo/        ← PY, JS, HTML, SQL...
│   ├── Comprimidos/   ← ZIP, RAR, 7Z...
│   └── Otros/         ← Todo lo demás
└── 2026-04-01_10-20-00/
    └── ...
```

---

## Requisitos

| Sistema | Requisito |
|---|---|
| Windows | Python 3.8 o superior |
| Linux | Python 3.8 o superior + python3-venv |

**¿Cómo saber si tenés Python instalado?**

- Windows: abrí PowerShell y escribí `python --version`
- Linux: abrí terminal y escribí `python3 --version`

Si no lo tenés:
- Windows: descargalo desde https://www.python.org/downloads/
  Durante la instalación marcá **"Add Python to PATH"**
- Linux (Ubuntu/Debian): `sudo apt install python3 python3-venv`

---

## Instalación en Windows

### Paso 1 — Descargar Bakopy

**Opción A — Con Git:**
```
git clone https://github.com/LucD3c/Bakopy.git
```

**Opción B — Sin Git (recomendada para usuarios nuevos):**
1. Entrá a https://github.com/LucD3c/Bakopy
2. Hacé clic en el botón verde **Code**
3. Seleccioná **Download ZIP**
4. Descomprimí el archivo descargado donde quieras

### Paso 2 — Iniciar Bakopy

Abrí la carpeta `Bakopy` y hacé **doble clic** en:
```
Iniciar Bakopy.bat
```

La primera vez que lo ejecutás:
- Se crea automáticamente el entorno de Python
- Se instala Flask (la única dependencia)
- Se abre el navegador con Bakopy listo para usar

Las veces siguientes simplemente abre el navegador directamente.

> Si Windows muestra una advertencia de seguridad al ejecutar el .bat,
> hacé clic en **"Más información"** y luego en **"Ejecutar de todas formas"**.
> Esto es normal para archivos descargados de internet.

### Paso 3 — Usar Bakopy

El navegador se abre automáticamente en `http://localhost:5099`.
Desde ahí podés crear y gestionar todos tus backups.

### Paso 4 — Cerrar Bakopy

Cuando termines, hacé doble clic en:
```
Detener Bakopy.bat
```

Esto cierra el servicio completamente. También podés simplemente
cerrar la ventana negra que se abrió al iniciar.

---

## Instalación en Linux (Ubuntu / Debian)

### Paso 1 — Clonar el repositorio
```bash
git clone https://github.com/LucD3c/Bakopy.git
cd Bakopy
```

O descargá el ZIP desde GitHub y descomprimilo.

### Paso 2 — Crear el entorno virtual
```bash
python3 -m venv venv
```

### Paso 3 — Activar el entorno virtual
```bash
source venv/bin/activate
```

Verás que el prompt cambia a `(venv)` — eso indica que el entorno está activo.

### Paso 4 — Instalar Flask
```bash
pip install flask
```

### Paso 5 — Iniciar Bakopy
```bash
python bakopy.py
```

Abrí tu navegador y entrá a:
```
http://localhost:5099
```

> Si accedés desde otra computadora en la misma red local, usá la IP
> de la máquina donde corre Bakopy: `http://IP_DEL_SERVIDOR:5099`
> Podés obtener la IP con el comando `hostname -I`

### Cerrar Bakopy

Volvé a la terminal donde está corriendo y presioná `CTRL+C`.

---

## Uso de la herramienta

### Primera vez — Configuración inicial

Al abrir Bakopy por primera vez verás la pantalla de bienvenida:

1. **Nombre de la carpeta:** escribí el nombre que le querés dar a tu
   carpeta de backups. Ejemplo: `MisBackups`, `Respaldos`, `Backup2026`

2. **Ubicación:** hacé clic en "Seleccionar ubicación" y navegá hasta
   donde querés crear esa carpeta. Puede ser:
   - Tu disco principal (C:\ en Windows, /home en Linux)
   - Un disco externo
   - Una carpeta de red

3. Hacé clic en **"Crear carpeta y empezar"**

Bakopy crea la carpeta automáticamente y no te vuelve a pedir esto.

---

### Crear un backup

1. **Agregá carpetas:** hacé clic en **+ Agregar carpeta** y navegá
   hasta la carpeta que querés respaldar. Podés agregar tantas como quieras.

2. **Verificá el espacio:** Bakopy muestra automáticamente cuánto espacio
   necesita el backup y cuánto tenés disponible:
   - 🟢 Verde: espacio suficiente
   - 🟡 Amarillo: espacio justo
   - 🔴 Rojo: espacio insuficiente — el botón queda desactivado

3. **Creá el backup:** hacé clic en **"Crear backup ahora"** y esperá
   a que termine. No cierres el navegador mientras está copiando.

4. **Resultado:** al terminar verás un resumen con la cantidad de archivos
   copiados, el tamaño total y las categorías encontradas.

---

### Historial de backups

Hacé clic en la pestaña **Historial** para ver todos tus backups anteriores.
Por cada backup podés:

- Ver fecha, hora, cantidad de archivos y tamaño
- Ver en qué carpeta están guardados los archivos
- **Eliminar registro:** borra solo el registro del historial,
  los archivos del backup quedan intactos en tu disco
- **Eliminar registro y archivos:** borra el registro y todos
  los archivos de ese backup para liberar espacio

---

### Llevar el backup a un pendrive o disco externo

La carpeta de backups es una carpeta normal en tu disco. Para llevarla:

1. Conectá tu pendrive o disco externo
2. Copiá o mové la carpeta `MisBackups` al dispositivo
3. Listo — tenés tu backup portable y organizado

---

## Preguntas frecuentes

**¿Mis archivos salen a internet?**
No. Bakopy funciona 100% en local. No se conecta a ningún servicio externo.

**¿Puedo cerrar el navegador mientras hace el backup?**
No. El navegador es la interfaz de Bakopy. Cerrarlo durante un backup
puede dejar la copia incompleta.

**¿Qué pasa si ya existe un archivo con el mismo nombre?**
Bakopy lo renombra automáticamente. Por ejemplo: `foto.jpg` → `foto_1.jpg`.
Ningún archivo se sobreescribe ni se pierde.

**¿Puedo respaldar carpetas de un disco externo?**
Sí. Conectá el disco, hacé clic en "+ Agregar carpeta" y navegá
hasta las carpetas que querés respaldar.

**¿Dónde se guarda la configuración?**
En el archivo `data/bakopy.db` dentro de la carpeta del proyecto.
Si lo borrás, Bakopy te pedirá configurar la carpeta de backups
nuevamente la próxima vez.

**¿Puedo tener varios perfiles de backup?**
En esta versión no. Toda la configuración apunta a una sola carpeta
de destino. Esta funcionalidad está planificada para versiones futuras.

---

## Estructura del proyecto
```
Bakopy/
├── Iniciar Bakopy.bat     ← Windows: doble clic para iniciar
├── Detener Bakopy.bat     ← Windows: doble clic para cerrar
├── bakopy.py              ← Punto de entrada principal
├── core/
│   ├── backup.py          ← Motor de copia y organización
│   ├── space.py           ← Cálculo de espacio en disco
│   └── scanner.py         ← Clasificación de archivos por tipo
├── data/
│   ├── db.py              ← Base de datos SQLite
│   └── bakopy.db          ← Historial y configuración (se crea automáticamente)
├── ui/
│   ├── app.py             ← Servidor Flask y endpoints
│   └── templates/
│       └── index.html     ← Interfaz de usuario
├── requirements.txt       ← Dependencias (solo Flask)
└── README.md              ← Este archivo
```

---

## Licencia

MIT — libre para usar, modificar y compartir.
