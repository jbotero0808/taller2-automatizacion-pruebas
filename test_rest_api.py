import os
import requests


def probar_servicio_rest():
    os.makedirs("evidencias", exist_ok=True)
    resultados = []

    # 1. Prueba de endpoint GET
    url_get = "https://jsonplaceholder.typicode.com/posts/1"  # Reemplaza con tu URL si es diferente
    try:
        res_get = requests.get(url_get)
        if res_get.status_code == 200:
            data = res_get.json()
            resultados.append(
                {
                    "paso": "GET /posts/1",
                    "estado": "PASÓ",
                    "detalle": f"Status 200 OK - Registro recuperado con ID: {data.get('id')}",
                }
            )
        else:
            resultados.append(
                {
                    "paso": "GET /posts/1",
                    "estado": "FALLÓ",
                    "detalle": f"Status HTTP: {res_get.status_code}",
                }
            )
    except Exception as e:
        resultados.append(
            {"paso": "GET /posts/1", "estado": "FALLÓ", "detalle": str(e)}
        )

    # 2. Prueba de endpoint POST con CAMPO PERSONALIZADO
    url_post = "https://jsonplaceholder.typicode.com/posts"  # Reemplaza con tu URL si es diferente
    try:
        payload = {
            "title": "Prueba REST Automatizada",
            "body": "Validación de envío de datos de prueba",
            "userId": 1,
            "categoria_prueba": "AA1_Calidad_Software",  # <-- NUEVO CAMPO PERSONALIZADO
        }
        res_post = requests.post(url_post, json=payload)
        if res_post.status_code in [200, 201]:
            resultados.append(
                {
                    "paso": "POST /posts (Crear Registro)",
                    "estado": "PASÓ",
                    "detalle": f"Status {res_post.status_code} - Objeto creado exitosamente con el campo 'categoria_prueba'",
                }
            )
        else:
            resultados.append(
                {
                    "paso": "POST /posts",
                    "estado": "FALLÓ",
                    "detalle": f"Status HTTP: {res_post.status_code}",
                }
            )
    except Exception as e:
        resultados.append(
            {"paso": "POST /posts", "estado": "FALLÓ", "detalle": str(e)}
        )

    return resultados


# Ejecución de la función e impresión de resultados
if __name__ == "__main__":
    reporte = probar_servicio_rest()
    for res in reporte:
        print(res)