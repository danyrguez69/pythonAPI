# Modelo de regresión Logística para análisis de sentimiento de comentarios usando el conjunto de datos aplicaciones de Google Play Store


Este proyecto es una aplicación para análisis de sentimiento de comentarios. Utiliza una API Flask para realizar predicciones de clasificación de Machine Learning.

## Descripción

La API expone un endpoint `/predice` que acepta peticiones `POST` con un texto procesado y devuelve una predicción de supervivencia.
Se incluye en `/code` el fichero `Proyecto_M7.ipynb` donde esta el paso a paso como se realiza el modelo y el vectorizador

## Requisitos

- Python 3.7+
- Flask
- pandas
- joblib
- scikit-learn

## Instalación

1. Clona este repositorio:
    ```bash
    git clone https://github.com/tu_usuario/tu_repositorio.git
    ```
2. Navega al directorio del proyecto:
    ```bash
    cd tu_repositorio
    ```
3. Crea un entorno virtual:
    ```bash
    python -m venv venv
    ```
4. Activa el entorno virtual:
    - En Windows:
        ```bash
        venv\Scripts\activate
        ```
    - En Linux/MacOS:
        ```bash
        source venv/bin/activate
        ```
5. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

## Uso

### Ejecutar la Aplicación Localmente

1. Asegúrate de que el entorno virtual esté activado.
2. Ejecuta la aplicación Flask:
    ```bash
    python app.py
    ```

La aplicación estará disponible en `http://127.0.0.1:808`.

### Consumir la API

Para consumir la API desde otro cliente (por ejemplo, Postman o un script Python), sigue los pasos a continuación:

1. Envía una petición `POST` al endpoint `http://python.taskingweb.cl:808/predice`.
2. El cuerpo de la petición debe ser un JSON con el siguiente formato:
    ```json
    {
        "Processed_Review": "love game"
    }
    ```

### Ejemplo en API publicada para pruebas en internet

```bash
curl -X POST http://python.taskingweb.cl:808/predice -H "Content-Type: application/json" -d '{"Processed_Review": "love game"}'
```

### Ejemplo en interfaz visual (solo funciona por el protocolo no seguro HTTP por temas de certificado)

```bash
http://python.taskingweb.cl/'
```



