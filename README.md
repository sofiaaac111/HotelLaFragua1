# Hotel La Fragua – ERP
Proyecto académico para la digitalización de los procesos administrativos y operativos del Hotel La Fragua, basado en una arquitectura de microservicios utilizando FastAPI, JWT, MySQL y un frontend web.

---

## Descripción General
Este sistema permite gestionar:

- Usuarios y autenticación
- Clientes
- Habitaciones
- Reservas
- Facturación
- Empleados
- Reportes
- Frontend web

Cada módulo funciona como un microservicio independiente, comunicándose mediante API REST.

---
## Arquitectura del Sistema
Arquitectura basada en microservicios:

    Frontend Web
        |
        v
  Auth Service (JWT)
        
        |
        v

| Clientes Service |

| Habitaciones Service |

| Reservas Service |

| Facturación Service |

| Empleados Service |

| Reportes Service |

---
## Seguridad y Autenticación (JWT)
El sistema utiliza JWT (JSON Web Token) para la autenticación.

Flujo:
1. El usuario se registra en auth-service
2. Inicia sesión
3. Recibe un access_token
4. Usa el token para acceder a los demás servicios
5. Cada servicio valida el token

Header:
Authorization: Bearer <token>


El token contiene:
- id del usuario
- correo
- rol
- fecha de expiración

---

## Microservicios

### 🔹 Auth Service (Puerto 8086)
Gestión de usuarios y autenticación.

Funciones:
- Registro de usuarios
- Login
- Generación de JWT
- Roles (admin, cliente, empleado)

---

### Clientes Service (Puerto 8081)
Gestión de información personal de clientes.

Funciones:
- Crear cliente usando JWT
- Asociar cliente con usuario_id del token
- CRUD de clientes

---

### Habitaciones Service (Puerto 8082)
Gestión de habitaciones.

Funciones:
- Crear habitaciones
- Listar habitaciones
- Cambiar estado (disponible / ocupada)
- Consultar precios

---

### Reservas Service (Puerto 8083)
Gestión de reservas.

Funciones:
- Crear reservas
- Verificar disponibilidad
- Cambiar estado de habitación
- Scheduler para finalizar reservas automáticamente

---

### Facturación Service (Puerto 8084)
Gestión de facturación.

Funciones:
- Generar facturas
- Calcular totales
- Asociar factura a reserva

---

### Empleados Service (Puerto 8085)
Gestión de empleados.

Funciones:
- Crear empleados
- Control de jornada laboral
- Estado activo/inactivo

---

### Reportes Service (Futuro)
Generación de reportes:
- Ingresos
- Reservas
- Ocupación
- Clientes

---

## Base de Datos
Motor: MySQL

Tablas principales:
- usuarios (auth-service)
- clientes (clientes-service)
- habitaciones (habitaciones-service)
- reservas (reservas-service)
- facturas (facturacion-service)
- empleados (empleados-service)

Relación principal:
usuarios.id → clientes.usuario_id
usuarios.id → empleados.usuario_id
usuarios.id → reservas.usuario_id


---

## Tecnologías Usadas
- Python 3.9+
- FastAPI
- SQLAlchemy
- MySQL
- JWT (python-jose)
- Passlib (bcrypt)
- Uvicorn
- Docker (opcional)
- GitHub
- Frontend (HTML/CSS/JS o React)

---

## Ejecución del Proyecto

1. Clonar el repositorio:

    ```bash
    git clone https://github.com/sofiaaac111/HotelLaFragua1.git

2. Crear entorno virtual:

        python -m venv .venv
        source .venv/bin/activate

3. Instalar dependencias:

        pip install -r requirements.txt

4. Ejecutar microservicio:

        uvicorn app.main:app --reload --port 8081


Puertos:

    Servicio	    Puerto
    Auth	        8086
    Clientes	    8081
    Habitaciones	8082
    Reservas	    8083
    Facturación	    8084
    Empleados	    8085


## Estructura del Proyecto

    HotelLaFragua/
    │
    ├── auth-service/
    ├── clientes-service/
    ├── habitaciones-service/
    ├── reservas-service/
    ├── facturacion-service/
    ├── empleados-service/
    ├── front-web/
    ├── README.md
    └── .gitignore

## Comunicación entre los servicios

    Los servicios se comunican mediante HTTP:
    requests.get("http://localhost:8082/habitaciones/1")


 
## Autores

Melany Sofía Gordillo Puentes 

Keiry Lucía Olaya Noguera

Sara Sofía Correales Mosquera


Ingeniería de Software

Proyecto académico de grado – Hotel La Fragua
