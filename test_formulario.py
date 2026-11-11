import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def probar_formulario_web():
    # Crear carpeta de evidencias si no existe
    os.makedirs("evidencias", exist_ok=True)

    # Configuración del navegador Chrome en modo headless (obligatorio para CI/CD)
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")  # Sin interfaz gráfica
    options.add_argument("--no-sandbox")  # Necesario en contenedores/VM de CI
    options.add_argument("--disable-dev-shm-usage")  # Evita fallos por /dev/shm reducido
    options.add_argument("--window-size=1280,800")

    try:
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()), options=options
        )
    except Exception:
        # Respaldo: Selenium Manager (incluido en Selenium >= 4.6) resuelve el driver
        driver = webdriver.Chrome(options=options)
    driver.set_window_size(1280, 800)

    resultados = []

    try:
        # 1. Abrir formulario de prueba pública
        url_formulario = "https://httpbin.org/forms/post"  # Sustituye con tu URL si es diferente
        driver.get(url_formulario)
        driver.save_screenshot("evidencias/01_formulario_abierto.png")
        resultados.append(
            {
                "paso": "Abrir Formulario Web",
                "estado": "PASÓ",
                "detalle": f"Página cargada: {url_formulario}",
            }
        )

        # 2. Llenar campos base y NUEVO CAMPO OBLIGATORIO (Teléfono)
        driver.find_element(By.NAME, "custname").send_keys("Estudiante Pruebas")
        driver.find_element(By.NAME, "custemail").send_keys(
            "estudiante@correo.com"
        )

        # --- CAMPO ADICIONAL PERSONALIZADO (Requisito del profesor) ---
        driver.find_element(By.NAME, "custtel").send_keys("3001234567")
        # -------------------------------------------------------------

        driver.save_screenshot("evidencias/02_campos_llenados.png")
        resultados.append(
            {
                "paso": "Llenar Campos (Nombre, Email, Teléfono)",
                "estado": "PASÓ",
                "detalle": "Campo adicional 'Teléfono' llenado correctamente",
            }
        )

        # 3. Seleccionar opción de tamaño
        size_large = driver.find_element(
            By.XPATH, "//input[@name='size'][@value='large']"
        )
        size_large.click()
        driver.save_screenshot("evidencias/03_opcion_seleccionada.png")
        resultados.append(
            {
                "paso": "Seleccionar Opción",
                "estado": "PASÓ",
                "detalle": "Opción Tamaño Grande seleccionada",
            }
        )

        # 4. Enviar formulario
        driver.find_element(By.TAG_NAME, "form").submit()
        time.sleep(1.5)
        driver.save_screenshot("evidencias/04_formulario_enviado.png")
        resultados.append(
            {
                "paso": "Enviar Formulario",
                "estado": "PASÓ",
                "detalle": "Formulario enviado correctamente al servidor",
            }
        )

    except Exception as e:
        driver.save_screenshot("evidencias/error_formulario.png")
        resultados.append(
            {"paso": "Ejecución Formulario", "estado": "FALLÓ", "detalle": str(e)}
        )

    finally:
        driver.quit()

    return resultados


# Ejecución de la función
if __name__ == "__main__":
    reporte = probar_formulario_web()
    for res in reporte:
        print(res)