import os
from test_formulario import probar_formulario_web
from test_rest_api import probar_servicio_rest


def generar_reporte_html(resultados_web, resultados_api):
    os.makedirs("reportes", exist_ok=True)

    # Filas de la tabla para pruebas Web
    filas_web = "".join(
        [
            f"<tr><td>{r['paso']}</td><td class='{r['estado'].lower()}'>{r['estado']}</td><td>{r['detalle']}</td></tr>"
            for r in resultados_web
        ]
    )

    # Filas de la tabla para pruebas API
    filas_api = "".join(
        [
            f"<tr><td>{r['paso']}</td><td class='{r['estado'].lower()}'>{r['estado']}</td><td>{r['detalle']}</td></tr>"
            for r in resultados_api
        ]
    )

    # Estructura del documento HTML
    html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Reporte de Pruebas</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; }}
        h1 {{ color: #333; }}
        h2 {{ color: #555; margin-top: 30px; }}
        table {{ border-collapse: collapse; width: 100%; margin-top: 10px; }}
        th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
        th {{ background-color: #f2f2f2; }}
        .pasó {{ color: green; font-weight: bold; }}
        .falló {{ color: red; font-weight: bold; }}
    </style>
</head>
<body>
    <h1>Reporte de Ejecución de Pruebas Automatizadas (AA1 - Unidad 2)</h1>
    <p><strong>Asignatura:</strong> Pruebas y Calidad del Software</p>

    <h2>1. Resultados Pruebas de Formulario Web (UI)</h2>
    <table>
        <thead>
            <tr>
                <th>Paso de Prueba</th>
                <th>Estado</th>
                <th>Detalle de Validación</th>
            </tr>
        </thead>
        <tbody>
            {filas_web}
        </tbody>
    </table>

    <h2>2. Resultados Pruebas de Servicio REST (API)</h2>
    <table>
        <thead>
            <tr>
                <th>Endpoint / Operación</th>
                <th>Estado</th>
                <th>Detalle / Respuesta</th>
            </tr>
        </thead>
        <tbody>
            {filas_api}
        </tbody>
    </table>
</body>
</html>"""

    ruta_reporte = os.path.abspath("reportes/reporte_pruebas.html")
    with open(ruta_reporte, "w", encoding="utf-8") as f:
        f.write(html_content)

    print("\n==================================================")
    print("✅ ¡PRUEBAS FINALIZADAS CON ÉXITO!")
    print(f"📷 Capturas guardadas en la carpeta: evidencias/")
    print(f"🌐 Reporte HTML generado en: {ruta_reporte}")
    print("==================================================\n")


if __name__ == "__main__":
    print("Ejecutando pruebas de Formulario Web...")
    res_web = probar_formulario_web()

    print("Ejecutando pruebas de Servicio REST...")
    res_api = probar_servicio_rest()

    generar_reporte_html(res_web, res_api)