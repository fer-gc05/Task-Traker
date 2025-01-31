import sys
import json
import os
from datetime import datetime


TASKS_FILE = "tasks.json"

def init_tasks():
    if not os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "w") as f:
            json.dump([], f)

def read_tasks():
    with open(TASKS_FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(description):
    tasks = read_tasks()
    task_id = max([task["id"] for task in tasks], default=0) + 1
    now = datetime.now().isoformat()
    new_task = {"id": task_id, "description": description, "status": "todo", "createdAt": now, "updatedAt": now}
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Tarea agregada con éxito (ID: {task_id})")

def update_task(task_id, new_description):
    tasks = read_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print("Tarea actualizada con éxito.")
            return
    print("Error: Tarea no encontrada.")

def delete_task(task_id):
    tasks = read_tasks()
    tasks = [task for task in tasks if task["id"] != task_id]
    save_tasks(tasks)
    print("Tarea eliminada con éxito.")

def mark_task(task_id, status):
    if status not in ["in-progress", "done"]:
        print("Estado no válido.")
        return
    tasks = read_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = status
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Tarea marcada como {status}.")
            return
    print("Error: Tarea no encontrada.")

def list_tasks(status=None):
    tasks = read_tasks()
    filtered_tasks = tasks if status is None else [t for t in tasks if t["status"] == status]
    if not filtered_tasks:
        print("No hay tareas.")
        return
    for task in filtered_tasks:
        print(f"[{task['id']}] ({task['status']}) {task['description']} (Creada: {task['createdAt']}, Actualizada: {task['updatedAt']})")

def main():
    init_tasks()
    if len(sys.argv) < 2:
        print("Uso: task-cli <comando> [argumentos]")
        print("Comandos disponibles:")
        print("  add <descripción> - Agrega una nueva tarea")
        print("  update <id> <nueva_descripción> - Actualiza la descripción de una tarea")
        print("  delete <id> - Elimina una tarea")
        print("  mark-in-progress <id> - Marca una tarea como 'en progreso'")
        print("  mark-done <id> - Marca una tarea como 'hecha'")
        print("  list [status] - Lista todas las tareas o filtra por estado (todo, in-progress, done)")
        return

    command = sys.argv[1]
    if command == "add" and len(sys.argv) > 2:
        add_task(" ".join(sys.argv[2:]))
    elif command == "update" and len(sys.argv) > 3:
        update_task(int(sys.argv[2]), " ".join(sys.argv[3:]))
    elif command == "delete" and len(sys.argv) > 2:
        delete_task(int(sys.argv[2]))
    elif command == "mark-in-progress" and len(sys.argv) > 2:
        mark_task(int(sys.argv[2]), "in-progress")
    elif command == "mark-done" and len(sys.argv) > 2:
        mark_task(int(sys.argv[2]), "done")
    elif command == "list":
        status = sys.argv[2] if len(sys.argv) > 2 else None
        list_tasks(status)
    else:
        print("Comando no reconocido.")

if __name__ == "__main__":
    main()