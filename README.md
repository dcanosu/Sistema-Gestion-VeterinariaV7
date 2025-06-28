# Sistema-Gestion-VeterinariaV7
# Sprint 12: Interfaz Web con Django (MVT) y su ORM
## Contexto
Como un paso más en el desarrollo de su aplicación, la clínica veterinaria desea expandir una experiencia de usuario satisfactoria. Para ello, han decidido dar luz verde a una mayor implementación de su interfaz web utilizando el framework Django, tanto con su arquitectura MVT como con su ORM.

La interfaz web facilitará las tareas más sencillas relacionadas con la clínica. Y aunque sigue siendo un prototipo en construcción, se espera que tenga las funcionalidades con las que se contaba en la interfaz de línea de comandos.

## Objetivos del ejercicio
Cada equipo deberá crear una aplicación web sencilla usando Django, siguiendo estrictamente el patrón arquitectónico **Modelo-Vista-Plantilla (MVT)** y usando su ORM, con las siguientes características:

- Definir claramente las rutas (URLs) y vistas asociadas.
- Crear las páginas web (algunas ya deberían de estar creadas) que lleven a la aplicación, al menos, al estado descrito a continuación:
1. Cuenta con una página de bienvenida (inicio).
2. Cuenta con una página para mostrar información estática básica sobre servicios veterinarios (puede usar texto ficticio, imágenes libres, etc.).
3. Cuenta con una página que permite gestionar la información de las mascotas de la clínica.
4. Cuenta con una página que permite gestionar la información de los dueños de las mascotas.
5. Cuenta con una página que permite gestionar las citas de la clínica.

- Uso obligatorio de plantillas (templates) HTML sencillas para mostrar contenido.
- Se deben, consecuentemente, contar ya con los modelos correspondientes a Mascotas, Propietarios y Citas.
  
## Requisitos técnicos
- Estructura clara siguiendo la arquitectura MVT:
 - Views: Manejo de solicitudes HTTP y lógica básica. Usar las vistas basadas en funciones (FBV) o vistas basadas en clases (CBV), según prefiera el equipo.
 - Templates: Archivos HTML con placeholders para contenido dinámico.
 - Urls: Rutas bien definidas y organizadas.
- Modelos claramente definidos utilizando Django ORM.
- Aplicar migraciones correctamente para la creación de tablas.
- Panel de administración activado con superusuario inicial creado.

- Manejo básico de archivos estáticos (CSS simple opcional, pero recomendado).

## Entrega
- Código fuente bien organizado en un repositorio Git.
- Archivo requirements.txt actualizado con dependencias necesarias.
- Archivo README.md breve explicando cómo ejecutar la aplicación localmente, incluyendo instrucciones específicas para:
 - Configuración de la base de datos (SQLite por defecto).
 - Realización de migraciones iniciales.
 - Creación del superusuario inicial.

## Integrantes
- Daniel Cano Suarez
- Miguel Cerquera Arias
- Esteban Eusse Munera
