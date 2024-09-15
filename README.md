# API de Festividades

Esta API ofrece información sobre los días festivos de Perú. Puedes obtener todas las festividades o consultar una festividad específica por su fecha.

## Endpoints

### 1. Obtener todas las festividades

**Endpoint:**  
`GET /festividades`

**Descripción:**  
Devuelve una lista con todas las festividades registradas.

**URL de producción:**  
[`https://api-drab-six.vercel.app/festividades`](https://api-drab-six.vercel.app/festividades)

**Ejemplo de respuesta:**
```json
[
  {"fecha": "2024-10-07", "nombre": "Día no laborable para el sector público"},
  {"fecha": "2024-10-08", "nombre": "Combate de Angamos"},
  {"fecha": "2024-11-01", "nombre": "Día de Todos los Santos"},
  {"fecha": "2024-12-06", "nombre": "Día no laborable para el sector público"},
  {"fecha": "2024-12-08", "nombre": "Inmaculada Concepción"},
  {"fecha": "2024-12-09", "nombre": "Batalla de Ayacucho"},
  {"fecha": "2024-12-23", "nombre": "Día no laborable para el sector público"},
  {"fecha": "2024-12-24", "nombre": "Día no laborable para el sector público"},
  {"fecha": "2024-12-25", "nombre": "Navidad"},
  {"fecha": "2024-12-30", "nombre": "Día no laborable para el sector público"},
  {"fecha": "2024-12-31", "nombre": "Día no laborable para el sector público"}
]
```

### 2. Obtener una festividad por fecha

**Endpoint:**  
`GET /festividad`

**Descripción:**  
Devuelve la información de una festividad específica según la fecha proporcionada.

**URL de producción:**  
[`https://api-drab-six.vercel.app/festividad`](https://api-drab-six.vercel.app/festividad)

**Parámetro:**  
- `fecha`: La fecha de la festividad en el formato `YYYY-MM-DD` (ejemplo: `2024-12-08`).

**Ejemplo de solicitud:**
```sh
curl "https://api-drab-six.vercel.app/festividad?fecha=2024-12-08"
```

**Ejemplo de respuesta:**
```json
{
  "fecha": "2024-12-08",
  "nombre": "Inmaculada Concepción"
}
```

Si la festividad no se encuentra para la fecha solicitada, devolverá un código `404` con un objeto vacío `{}`.

## Cómo correr este proyecto localmente

Si deseas clonar este proyecto y ejecutarlo localmente, sigue los siguientes pasos:

1. Clona el repositorio:

   ```sh
   git clone https://github.com/tu_usuario/nombre_del_repositorio.git
   cd nombre_del_repositorio
   ```

2. Instala las dependencias:

   ```sh
   pip install -r requirements.txt
   ```

3. Inicia el servidor localmente:

   ```sh
   flask run
   ```

4. Accede a los endpoints localmente:

   - `http://127.0.0.1:5000/festividades`
   - `http://127.0.0.1:5000/festividad?fecha=YYYY-MM-DD`

## Despliegue

Este proyecto está desplegado en Vercel y puede accederse a través de los enlaces proporcionados en los endpoints.

## Tecnologías usadas

- Python
- Flask
- Vercel para el despliegue
