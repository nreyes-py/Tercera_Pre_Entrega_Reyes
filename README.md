# ProyectoCuentos

ProyectoCuentos es una aplicación web desarrollada en Django que permite a los usuarios compartir y leer cuentos. Este archivo README proporciona una guía sobre cómo navegar y probar las funcionalidades de la aplicación.

## Configuración Inicial

Para comenzar a utilizar la aplicación, sigue estos pasos:

1. Clona el repositorio a tu máquina local.
2. Instala las dependencias necesarias usando `pip install -r requirements.txt`.
3. Ejecuta las migraciones con `python manage.py migrate` para configurar la base de datos.
4. Crea un superusuario con `python manage.py createsuperuser` y sigue las instrucciones.
5. Inicia el servidor de desarrollo con `python manage.py runserver`.

## Funcionalidades y Cómo Probarlas

A continuación, se describe el orden recomendado para probar las funcionalidades de la aplicación:

### Inicio

- **URL:** `/`
- **Descripción:** Página de inicio que muestra una bienvenida y enlaces a las principales secciones del sitio.

### Cuentos

- **URL:** `/cuentos/`
- **Descripción:** Lista todos los cuentos disponibles. Aquí puedes seleccionar un cuento para ver detalles o agregar un nuevo cuento.
- **Cómo probar:** Haz clic en 'Leer más' para ver los detalles de un cuento o en 'Agregar un cuento' para publicar uno nuevo.

### Detalles del Cuento

- **URL:** `/cuentos/<id>/`
- **Descripción:** Muestra los detalles completos de un cuento específico.
- **Cómo probar:** Desde la lista de cuentos, selecciona 'Leer más' en cualquier cuento.

### Perfil de Usuario

- **URL:** `/perfil/`
- **Descripción:** Muestra el perfil del usuario y una lista de sus cuentos publicados.
- **Cómo probar:** Debes estar autenticado para ver tu perfil.

### Sobre Nosotros

- **URL:** `/sobre_nosotros/`
- **Descripción:** Proporciona información sobre la misión y visión del proyecto.
- **Cómo probar:** Accede a través del enlace 'Sobre Nosotros' en la navegación.

### Administración

- **URL:** `/admin/`
- **Descripción:** Interfaz de administración de Django para gestionar usuarios, cuentos y otras entidades.
- **Cómo probar:** Debes estar autenticado como superusuario para acceder a la administración.

### Funcionalidades Adicionales

- **Agregar Cuento:** Permite a los usuarios añadir nuevos cuentos.
- **Editar Cuento:** Los usuarios pueden editar sus propios cuentos.
- **Eliminar Cuento:** Los usuarios pueden eliminar sus propios cuentos.
- **Historias Comunes:** Funcionalidad para crear una historia común a partir de cuentos seleccionados (disponible próximamente).

Recuerda que para probar las funcionalidades que requieren autenticación, debes haber iniciado sesión con tu usuario y contraseña.

## Contacto

Si tienes alguna pregunta o encuentras algún problema, por favor abre un issue en el repositorio de GitHub o contacta al equipo de desarrollo.
