# Actividad 6 – Ejemplo en Selenium (Python)

Automatización mínima con Selenium WebDriver en Python: abre un navegador, visita una URL y valida el título de la página.

## 1) Requisitos previos
- **Python 3.10+** (recomendado)
- **Navegador** instalado (ideal: Google Chrome)
- **pip** actualizado

> Desde Selenium 4.6+ se usa **Selenium Manager**, que descarga el driver automáticamente si tienes un navegador compatible instalado.

## 2) Clonar el repositorio
```bash
git clone <URL_DE_TU_REPO>
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
