# Shopo - Tienda Online en Django

Este es un proyecto de tienda online desarrollado con Django y Tailwind CSS para aprender sobre desarrollo web y frameworks modernos.

## Características
- Gestión de productos y categorías
- Autenticación de usuarios (registro e inicio de sesión)
- Diseño responsivo con Tailwind CSS
- Panel de administración con Django Admin

## Requisitos previos
Asegúrate de tener instalados los siguientes programas:
- Python 3.x
- Django
- Pipenv o virtualenv (opcional pero recomendado)

## Instalación
1. Clona el repositorio:
   ```sh
   git clone https://github.com/tu_usuario/shopo.git
   cd shopo
   ```
2. Crea un entorno virtual (opcional pero recomendado):
   ```sh
   python -m venv env
   source env/bin/activate  # En Windows: env\Scripts\activate
   ```
3. Instala las dependencias:
   ```sh
   pip install -r requirements.txt
   ```
4. Aplica las migraciones de la base de datos:
   ```sh
   python manage.py migrate
   ```
5. Crea un superusuario para acceder al panel de administración:
   ```sh
   python manage.py createsuperuser
   ```
6. Ejecuta el servidor:
   ```sh
   python manage.py runserver
   ```

## Uso
- Accede a la tienda en `http://127.0.0.1:8000/`
- Accede al panel de administración en `http://127.0.0.1:8000/admin/`

## Contribuciones
Si deseas contribuir, puedes hacer un fork del proyecto y enviar pull requests con mejoras o nuevas funcionalidades.

## Licencia
Este proyecto está bajo la licencia MIT. Puedes modificarlo y usarlo libremente.

---
**¡Gracias por visitar Shopo!** 🎉
