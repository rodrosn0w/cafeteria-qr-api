# ☕ SmartMenu QR - Punto Café (API Backend)

> **Estatus del Proyecto:** En Desarrollo (MVP Funcional)  
> **Área:** Ingeniería de Software / Backend Development

## 🎯 Contexto y Problema
Este proyecto nace de una necesidad real: digitalizar la gestión de pedidos de un emprendimiento de pastelería artesanal. El problema principal era la demora en la atención en mesa y la dificultad para actualizar precios y stock en menús físicos de papel. 

**La Solución:** Una API REST robusta que centraliza la carta, permite el autoservicio mediante códigos QR y garantiza que el cliente solo vea productos con stock disponible en tiempo real.

## 🛠️ Stack Tecnológico y Decisiones de Arquitectura
Para este desarrollo, elegí un stack moderno enfocado en la velocidad de respuesta y la integridad de los datos:

* **FastAPI (Python):** Seleccionado por su alto rendimiento (basado en Starlette/Pydantic) y la capacidad de autogenerar documentación interactiva (Swagger), lo que acelera el testeo.
* **MySQL & SQLAlchemy (ORM):** Implementé un modelo relacional para asegurar la consistencia entre mesas, productos y pedidos. El uso de un ORM me permitió mantener el código limpio y facilitar futuras migraciones.
* **Uvicorn:** Servidor ASGI para manejar peticiones asíncronas de forma eficiente.
* **Python-dotenv:** Gestión estandarizada de variables de entorno para seguridad de credenciales.

## 🧠 Desafíos Técnicos y Aprendizajes
Durante el desarrollo, me enfrenté a retos que pusieron a prueba mi capacidad de resolución:

1.  **Sincronización de Entornos:** El desafío más reciente fue estandarizar el esquema de la base de datos entre diferentes máquinas de desarrollo (PC y Notebook). Lo resolví mediante la unificación de modelos en SQLAlchemy y la configuración de una política de ejecución de scripts en PowerShell para entornos virtuales.
2.  **Mapeo Objeto-Relacional:** Ajusté la convención de nombres (Singular vs Plural) para alinear el código Python con las tablas existentes en MySQL, garantizando la paridad del sistema.

## 📋 Documentación de la API (Endpoints)
La API cuenta con documentación automática en `/docs`. Algunos endpoints clave son:
* `GET /menu`: Devuelve solo los productos con `stock_status: True`.
* `POST /orders` (En desarrollo): Procesará pedidos vinculando productos con IDs de mesa.

## 🚀 Instalación y Uso
1. Clonar el repositorio.
2. Crear entorno virtual: `python -m venv venv`.
3. Activar y ejecutar: `.\venv\Scripts\activate` y `pip install -r requirements.txt`.
4. Configurar `.env` con la URL de tu MySQL local.
5. Iniciar: `uvicorn main:app --reload`.

---
**Desarrollado por Rodrigo** *Estudiante de Ingeniería en Informática (UADE) | Enfocado en Backend & Data Analytics*
