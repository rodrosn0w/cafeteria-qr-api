#  SmartMenu QR - Punto Café (API Backend)

> **Estatus del Proyecto:** En Desarrollo (MVP Funcional)  
> **Área:** Ingeniería de Software / Backend Development

##  Contexto y Problema
Este proyecto nace de una necesidad real: digitalizar la gestión de pedidos de una cafetería. El problema principal era el flujo de pedido: el cliente debe ir hasta mostrador para hacer el pedido, muchas personas no tenían conocimiento de esto por lo que, sentado en su mesa esperando al mozo, pasaba el tiempo y nadie lo atendía. Esto hacía que el cliente se retirara del local, perdiendo ventas y recibiendo reseñas negativas en Google.

**La Solución:** Una API REST robusta que centraliza la carta, permite el autoservicio mediante códigos QR y garantiza que el cliente haga el pedido desde la comodidad de su mesa.

## 🚀 Flujo completo de un pedido

1. Dueño crea mesa con `POST /mesas/` → obtiene QR con `GET /mesas/{id}/qr`
2. QR impreso se pega en la mesa física
3. Cliente escanea → su celular abre el frontend con `?token=abc123`
4. Frontend llama `GET /menu/?token=abc123` → muestra el menú
5. Cliente elige productos → `POST /pedidos/?token=abc123`
6. El panel del mostrador recibe notificación WS instantánea
7. Mostrador cambia estado: `PATCH /pedidos/{id}/estado` → `en_preparacion`
8. Cuando está listo: `→ listo`, llevan a la mesa, `→ entregado`
9. Si pagó con efectivo al terminar: `PATCH /pedidos/{id}/pagar`

## 🛠️ Stack Tecnológico

Para garantizar un sistema de alta disponibilidad y bajo tiempo de respuesta, utilicé las siguientes herramientas:

* **FastAPI (Python 3.12+):** Elegido por su rendimiento asíncrono y la validación de datos automática mediante **Pydantic**.
* **MySQL & SQLAlchemy (ORM):** Implementación de una base de datos relacional para asegurar la integridad referencial entre pedidos y productos.
* **Uvicorn:** Servidor ASGI de alto rendimiento para el despliegue de la API.
* **Python-dotenv:** Gestión de seguridad para desacoplar las credenciales de la base de datos del código fuente mediante archivos `.env`.
*  **Pydantic:** Motor de validación de datos que garantiza la integridad de la información entrante y saliente, definiendo contratos claros entre el frontend y el backend.

## 🏛️ Decisiones de Arquitectura

el proyecto se estructuró bajo los siguientes pilares:

* **Arquitectura en Capas:** Separación estricta de responsabilidades entre el modelo de datos (`models.py`), los esquemas de validación (`schemas.py`) y la lógica de negocio en los endpoints (`main.py`).
* **Normalización de Datos:** Diseño de una base de datos relacional que vincula Mesas, Productos y Pedidos mediante tablas intermedias (`order_items`), evitando la redundancia y permitiendo reportes detallados.
* **Validación de Contratos:** Implementación de esquemas de Pydantic para asegurar que la API solo procese datos que cumplan con los tipos y formatos requeridos, reduciendo errores en tiempo de ejecución.



## 📋 Documentación de la API (Endpoints)
La API cuenta con documentación automática en `/docs`. Algunos endpoints clave son:
* `GET /menu`: Devuelve solo los productos con `stock_status: True`.
* `POST /orders` (En desarrollo): Procesará pedidos vinculando productos con IDs de mesa.

## 🚀 Instalación y Uso
1. **Clonación:** `git clone https://github.com/rodrosn0w/cafeteria-qr-api.git`
2. **Entorno:** `python -m venv venv` y activación con `.\venv\Scripts\activate`.
3. **Dependencias:** `pip install -r requirements.txt`.
4. **Base de Datos:** Configurar el archivo `.env` con las credenciales de MySQL local.
5. **Ejecución:** `uvicorn main:app --reload`.

---
**Desarrollado por Rodrigo** * Backend  Developer*
