# Task Tracker CLI

**Task Tracker CLI** es una herramienta de línea de comandos para gestionar tareas. Te permite agregar, actualizar, eliminar y listar tareas, así como cambiar su estado (`todo`, `in-progress`, `done`). Las tareas se almacenan en un archivo JSON (`tasks.json`) para su persistencia.

Este proyecto está basado en el reto **Task Tracker** de [roadmap.sh](https://roadmap.sh/projects/task-tracker), diseñado para practicar habilidades de desarrollo de software.

---

## Requisitos

- Python 3.x instalado en tu sistema.

---

## Instalación

1. Clona este repositorio o descarga el archivo `taskTracker.py`.
2. Asegúrate de que Python esté instalado en tu sistema. Puedes verificarlo ejecutando:
   ```bash
   python --version
   ```
3. No se requieren dependencias adicionales.

---

## Uso

Ejecuta el script `taskTracker.py` desde la terminal con los siguientes comandos:

### **1. Agregar una tarea**

Agrega una nueva tarea con una descripción.

**Sintaxis:**

```bash
python taskTracker.py add "Descripción de la tarea"
```

**Ejemplo:**

```bash
python taskTracker.py add "Comprar comida"
```

---

### **2. Actualizar una tarea**

Actualiza la descripción de una tarea existente usando su ID.

**Sintaxis:**

```bash
python taskTracker.py update <id> "Nueva descripción"
```

**Ejemplo:**

```bash
python taskTracker.py update 1 "Comprar comida y bebida"
```

---

### **3. Eliminar una tarea**

Elimina una tarea usando su ID.

**Sintaxis:**

```bash
python taskTracker.py delete <id>
```

**Ejemplo:**

```bash
python taskTracker.py delete 1
```

---

### **4. Marcar una tarea como 'en progreso'**

Cambia el estado de una tarea a "en progreso" usando su ID.

**Sintaxis:**

```bash
python taskTracker.py mark-in-progress <id>
```

**Ejemplo:**

```bash
python taskTracker.py mark-in-progress 2
```

---

### **5. Marcar una tarea como 'hecha'**

Cambia el estado de una tarea a "hecha" usando su ID.

**Sintaxis:**

```bash
python taskTracker.py mark-done <id>
```

**Ejemplo:**

```bash
python taskTracker.py mark-done 2
```

---

### **6. Listar tareas**

Muestra todas las tareas o filtra por estado (`todo`, `in-progress`, `done`).

**Sintaxis:**

```bash
python taskTracker.py list [estado]
```

**Ejemplos:**

- Listar todas las tareas:
  ```bash
  python taskTracker.py list
  ```
- Listar tareas en progreso:
  ```bash
  python taskTracker.py list in-progress
  ```
- Listar tareas hechas:
  ```bash
  python taskTracker.py list done
  ```

---

### **7. Ayuda**

Muestra una lista de comandos disponibles.

**Sintaxis:**

```bash
python taskTracker.py
```

---

## Estructura del archivo de tareas

Las tareas se almacenan en un archivo JSON (`tasks.json`) con el siguiente formato:

```json
[
  {
    "id": 1,
    "description": "Comprar comida",
    "status": "todo",
    "createdAt": "2023-10-01T12:00:00.000000",
    "updatedAt": "2023-10-01T12:00:00.000000"
  }
]
```

- **id**: Identificador único de la tarea.
- **description**: Descripción de la tarea.
- **status**: Estado de la tarea (`todo`, `in-progress`, `done`).
- **createdAt**: Fecha y hora de creación de la tarea.
- **updatedAt**: Fecha y hora de la última actualización.

---

## Ejemplo de flujo de trabajo

1. Agregar una tarea:

   ```bash
   python taskTracker.py add "Comprar comida"
   ```
2. Listar tareas:

   ```bash
   python taskTracker.py list
   ```
3. Marcar una tarea como "en progreso":

   ```bash
   python taskTracker.py mark-in-progress 1
   ```
4. Actualizar una tarea:

   ```bash
   python taskTracker.py update 1 "Comprar comida y bebida"
   ```
5. Marcar una tarea como "hecha":

   ```bash
   python taskTracker.py mark-done 1
   ```
6. Eliminar una tarea:

   ```bash
   python taskTracker.py delete 1
   ```

---

## Basado en el reto Task Tracker de roadmap.sh

Este proyecto está inspirado en el reto **Task Tracker** de [roadmap.sh](https://roadmap.sh/projects/task-tracker), una plataforma que ofrece desafíos prácticos para mejorar tus habilidades de desarrollo de software. El reto original consiste en construir una aplicación de seguimiento de tareas, y esta CLI es una implementación simplificada en Python.
