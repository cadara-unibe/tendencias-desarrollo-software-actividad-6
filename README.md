# Actividad 6 – Ejemplo en Selenium (Python)

Automatización mínima con Selenium WebDriver en Python: abre un navegador, visita una URL y valida el título de la página.

## 1) Requisitos previos
- **Python 3.10+** (recomendado)
- **Navegador** instalado (ideal: Google Chrome)
- **pip** actualizado

> Desde Selenium 4.6+ se usa **Selenium Manager**, que descarga el driver automáticamente si tienes un navegador compatible instalado.

## 2) Clonar el repositorio
```bash
git clone https://github.com/cadara-unibe/tendencias-desarrollo-software-actividad-6.git --depth 1
cd tendencias-desarrollo-software-actividad-6
````

## 3) (Opcional) Crear y activar entorno virtual

**macOS / Linux**

```bash
python -m venv .venv
source .venv/bin/activate
```

**Windows (PowerShell)**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

## 4) Instalar dependencias

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## 5) Configurar el script (opcional)

Abre `test_selenium_title.py` y, si quieres, cambia:

```python
url = "https://www.example.com"
expected_title = "Example Domain"
```

Quita `--headless=new` en las opciones de Chrome si deseas ver el navegador.

## 6) Ejecutar la prueba

```bash
python test_selenium_title.py
```

**Resultado esperado:**

```
✅ La prueba pasó: el título de la página es correcto.
```

o, en caso de fallo, un mensaje indicando el título esperado y el obtenido.

## 7) Solución de problemas

* **No tengo Chrome**: instala Chrome o usa Firefox/Edge y ajusta el script para ese navegador.
* **El driver no se descarga**: verifica tu conexión o proxy; actualiza Selenium:
  `pip install -U selenium`
* **Permisos en Linux**: evita ejecutar con `sudo`. Usa un entorno virtual.
* **Entorno virtual no activa en Windows**: ejecuta PowerShell como admin y habilita scripts:
  `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser`

## 8) Estructura del proyecto

```
tendencias-desarrollo-software-actividad-6/
├─ README.md
├─ requirements.txt
├─ .gitignore
└─ test_selenium_title.py
```

```
```

```
En caso de aviso es **Gatekeeper** de macOS bloqueando `chromedriver` por no estar “notarizado”. Tienes tres formas rápidas de resolverlo (elige 1):
```

## Opción A — Permitirlo desde Preferencias del Sistema (la más simple)

1. Ejecuta tu script una vez para que aparezca el aviso.
2. Ve a ** > System Settings > Privacy & Security**.
3. Baja hasta **Security** y verás “*chromedriver was blocked*” → pulsa **Allow Anyway**.
4. Vuelve a correr el script; te saldrá un diálogo “Open/Cancel” → elige **Open**.

## Opción B — Quitar la cuarentena con `xattr` (línea de comandos)

### Si lo instalaste con Homebrew

1. Localiza el binario real:

   ```bash
   which chromedriver
   ls -l /opt/homebrew/bin/chromedriver          # mira a dónde apunta el symlink
   ```
2. Quita la cuarentena **en el binario real** (no solo en el symlink). Por ejemplo:

   ```bash
   xattr -dr com.apple.quarantine /opt/homebrew/Caskroom/chromedriver/*/*/chromedriver
   ```
3. Verifica que ya no tenga el atributo:

   ```bash
   xattr -l /opt/homebrew/Caskroom/chromedriver/*/*/chromedriver
   ```
4. Ejecuta de nuevo tu prueba.

### Si Selenium (4.6+) descargó el driver automáticamente

1. Busca el binario en la caché de Selenium (suele estar en tu home):

   ```bash
   find ~/Library/Caches/selenium -name chromedriver
   ```
2. Quita la cuarentena:

   ```bash
   xattr -dr com.apple.quarantine ~/Library/Caches/selenium/**/chromedriver
   ```
3. Ejecuta tu prueba otra vez.

## Opción C — Evitar `chromedriver` manual y usar **Selenium Manager** (recomendado)

1. Asegúrate de tener Selenium reciente:

   ```bash
   pip install -U selenium
   ```
2. Usa tu script **sin** rutas de driver:

   ```python
   from selenium import webdriver
   from selenium.webdriver.chrome.options import Options

   opts = Options()
   opts.add_argument("--headless=new")  # opcional
   driver = webdriver.Chrome(options=opts)  # Selenium Manager gestiona el driver
   ```
3. Si aún aparece el aviso, aplica **A** o **B** sobre el binario que Selenium descarga (ruta en `~/Library/Caches/selenium/...`).

---

### Tips rápidos

* En Apple Silicon (M1/M2), usa el `chromedriver` **arm64** (Homebrew ya instala arm64 por defecto).
* Si ves el mismo aviso otra vez, es porque macOS aplicó la cuarentena al **binario efectivo**; asegúrate de quitarla **en el destino real del symlink**.
* Alternativa: usa **Firefox** (`geckodriver`) o **Edge** si tu entorno lo permite (mismo patrón con `xattr`).
