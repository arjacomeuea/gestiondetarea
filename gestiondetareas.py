import tkinter as tk
from tkinter import messagebox

# Crear la ventana principal
root = tk.Tk()
root.title("Gestor de Tareas Pendientes")
root.geometry("400x400")

# Lista que contendrá las tareas
tasks = []

# Función para añadir una nueva tarea
def add_task(event=None):
    task = task_entry.get().strip()
    if task:
        tasks.append({"task": task, "completed": False})
        update_task_list()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Entrada Vacía", "Por favor ingrese una tarea.")

# Función para actualizar la lista de tareas en la interfaz
def update_task_list():
    task_list.delete(0, tk.END)
    for idx, task_data in enumerate(tasks):
        task_text = task_data["task"]
        if task_data["completed"]:
            task_text += " (completada)"
        task_list.insert(tk.END, task_text)

# Función para marcar una tarea como completada
def complete_task(event=None):
    try:
        selected_task_index = task_list.curselection()[0]
        tasks[selected_task_index]["completed"] = True
        update_task_list()
    except IndexError:
        messagebox.showwarning("Selecciona una tarea", "No has seleccionado ninguna tarea para completar.")

# Función para eliminar una tarea
def delete_task(event=None):
    try:
        selected_task_index = task_list.curselection()[0]
        del tasks[selected_task_index]
        update_task_list()
    except IndexError:
        messagebox.showwarning("Selecciona una tarea", "No has seleccionado ninguna tarea para eliminar.")

# Función para cerrar la aplicación
def close_app(event=None):
    root.quit()

# Crear la entrada de texto para nuevas tareas
task_entry = tk.Entry(root, width=35)
task_entry.pack(pady=10)
task_entry.focus()

# Crear el botón de añadir tarea
add_task_button = tk.Button(root, text="Añadir Tarea", command=add_task)
add_task_button.pack()

# Crear el Listbox para mostrar las tareas
task_list = tk.Listbox(root, width=50, height=10)
task_list.pack(pady=10)

# Crear el botón de marcar como completada
complete_task_button = tk.Button(root, text="Marcar como Completada", command=complete_task)
complete_task_button.pack(pady=5)

# Crear el botón de eliminar tarea
delete_task_button = tk.Button(root, text="Eliminar Tarea", command=delete_task)
delete_task_button.pack(pady=5)

# Asignar atajos de teclado
root.bind("<Return>", add_task)  # Enter para añadir tarea
root.bind("<c>", complete_task)  # "C" para marcar como completada
root.bind("<Delete>", delete_task)  # Suprimir para eliminar tarea
root.bind("<d>", delete_task)  # "D" para eliminar tarea
root.bind("<Escape>", close_app)  # Escape para cerrar la aplicación

# Ejecutar la aplicación
root.mainloop()
