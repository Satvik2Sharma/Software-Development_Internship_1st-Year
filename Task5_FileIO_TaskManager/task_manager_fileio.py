# 💾 ADVANCED TASK MANAGER WITH FILE I/O
# Internship Task 5
# 👨‍💻 Developed by: Satvik Sharma

from datetime import datetime
import json
import os

# 📌 FILE NAME
FILE_NAME = "tasks.json"

# 📌 TASK CLASS
class Task:
    def __init__(self, title, description, priority):
        self.title = title
        self.description = description
        self.priority = priority
        self.status = "⏳ Pending"
        self.created_at = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    def display(self, index):
        print(f"""
=========================================
📋 Task #{index}

📝 Title       : {self.title}
📄 Description : {self.description}
⚡ Priority    : {self.priority}
📌 Status      : {self.status}
🕒 Created At  : {self.created_at}
=========================================
""")

# 📂 TASK STORAGE
tasks = []

# 💾 SAVE TASKS
def save_tasks():
    data = []
    for task in tasks:
        data.append({
            "title": task.title,
            "description": task.description,
            "priority": task.priority,
            "status": task.status,
            "created_at": task.created_at
        })
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"\n❌ Error saving tasks: {e}")

# 📂 LOAD TASKS
def load_tasks():
    if not os.path.exists(FILE_NAME):
        return
    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)
            for item in data:
                task = Task(
                    item["title"],
                    item["description"],
                    item["priority"]
                )
                task.status = item["status"]
                task.created_at = item["created_at"]
                tasks.append(task)
    except Exception as e:
        print(f"\n❌ Error loading tasks: {e}")

# ➕ ADD TASK
def add_task():
    print("\n========== ➕ ADD TASK ==========\n")
    title = input("📝 Enter task title: ")
    description = input("📄 Enter task description: ")
    priority = input("⚡ Enter priority: ")
    task = Task(title, description, priority)
    tasks.append(task)
    save_tasks()
    print("\n✅ Task added successfully!\n")

# 📖 VIEW TASKS
def view_tasks():
    print("\n========== 📖 TASK LIST ==========\n")
    if not tasks:
        print("❌ No tasks available.\n")
        return
    for index, task in enumerate(tasks, start=1):
        task.display(index)

# 🗑️ DELETE TASK
def delete_task():
    view_tasks()
    if not tasks:
        return
    try:
        task_number = int(input("🔢 Enter task number to delete: "))
        if 1 <= task_number <= len(tasks):
            removed = tasks.pop(task_number - 1)
            save_tasks()
            print(f"\n🗑️ Deleted task: {removed.title}\n")
        else:
            print("\n❌ Invalid task number.\n")
    except ValueError:
        print("\n❌ Enter valid number.\n")

# 🏠 MAIN MENU
def main():
    load_tasks()
    while True:
        print("""
========================================
💾 TASK MANAGER WITH FILE STORAGE
========================================
1️⃣  Add Task
2️⃣  View Tasks
3️⃣  Delete Task
4️⃣  Exit
========================================
""")
        choice = input("👉 Enter your choice: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("\n👋 Exiting program...\n")
            break
        else:
            print("\n❌ Invalid choice.\n")

# ▶️ START PROGRAM
if __name__ == "__main__":
    main()