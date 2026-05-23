# 🚀 ADVANCED TASK MANAGER CRUD APPLICATION
# First Task oriented Internship project.
# Task 3: Create a console application for basic CRUD operations on a list of tasks.

# 👨‍💻 Developed by: Satvik Sharma

from datetime import datetime
import os

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

# 🧹 CLEAR SCREEN
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# ➕ ADD TASK
def add_task():
    print("\n========== ➕ ADD NEW TASK ==========\n")
    title = input("📝 Enter task title: ")
    description = input("📄 Enter task description: ")
    priority = input("⚡ Enter priority (High/Medium/Low): ")
    task = Task(title, description, priority)
    tasks.append(task)
    print("\n✅ Task added successfully!\n")

# 📖 VIEW TASKS
def view_tasks():
    print("\n========== 📖 TASK LIST ==========\n")
    if not tasks:
        print("❌ No tasks available.\n")
        return
    for index, task in enumerate(tasks, start=1):
        task.display(index)

# ✏️ UPDATE TASK
def update_task():
    print("\n========== ✏️ UPDATE TASK ==========\n")
    if not tasks:
        print("❌ No tasks available.\n")
        return
    view_tasks()

    try:
        task_number = int(input("🔢 Enter task number to update: "))

        if 1 <= task_number <= len(tasks):
            task = tasks[task_number - 1]
            print("""
1️⃣ Update Title
2️⃣ Update Description
3️⃣ Update Priority
4️⃣ Update Status
""")
            choice = input("👉 Enter choice: ")
            if choice == "1":
                task.title = input("📝 Enter new title: ")
                print("\n✅ Title updated successfully!\n")
            elif choice == "2":
                task.description = input("📄 Enter new description: ")
                print("\n✅ Description updated successfully!\n")
            elif choice == "3":
                task.priority = input("⚡ Enter new priority: ")
                print("\n✅ Priority updated successfully!\n")
            elif choice == "4":
                print("""
1️⃣ Pending
2️⃣ Completed
""")
                status_choice = input("👉 Choose status: ")
                if status_choice == "1":
                    task.status = "⏳ Pending"
                elif status_choice == "2":
                    task.status = "✅ Completed"
                else:
                    print("\n❌ Invalid status choice.\n")
                    return
                print("\n✅ Status updated successfully!\n")
            else:
                print("\n❌ Invalid choice.\n")
        else:
            print("\n❌ Invalid task number.\n")
    except ValueError:
        print("\n❌ Please enter a valid number.\n")

# 🗑️ DELETE TASK
def delete_task():
    print("\n========== 🗑️ DELETE TASK ==========\n")
    if not tasks:
        print("❌ No tasks available.\n")
        return
    view_tasks()
    try:
        task_number = int(input("🔢 Enter task number to delete: "))
        if 1 <= task_number <= len(tasks):
            deleted_task = tasks.pop(task_number - 1)
            print(f"\n🗑️ Task '{deleted_task.title}' deleted successfully!\n")
        else:
            print("\n❌ Invalid task number.\n")
    except ValueError:
        print("\n❌ Please enter a valid number.\n")

# 🔍 SEARCH TASK
def search_task():
    print("\n========== 🔍 SEARCH TASK ==========\n")
    keyword = input("🔎 Enter keyword to search: ").lower()
    found = False
    for index, task in enumerate(tasks, start=1):
        if keyword in task.title.lower():
            task.display(index)
            found = True
    if not found:
        print("\n❌ No matching tasks found.\n")

# 📊 TASK STATISTICS
def task_statistics():
    total = len(tasks)
    completed = sum(task.status == "✅ Completed" for task in tasks)
    pending = total - completed
    print("\n========== 📊 TASK STATISTICS ==========\n")
    print(f"📌 Total Tasks      : {total}")
    print(f"✅ Completed Tasks  : {completed}")
    print(f"⏳ Pending Tasks    : {pending}\n")


# 🏠 MAIN MENU
def main():
    while True:
        print("""
=================================================
🚀        ADVANCED TASK MANAGER SYSTEM
=================================================

1️⃣  Add Task
2️⃣  View Tasks
3️⃣  Update Task
4️⃣  Delete Task
5️⃣  Search Task
6️⃣  Task Statistics
7️⃣  Exit

=================================================
""")
        choice = input("👉 Enter your choice: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            search_task()
        elif choice == "6":
            task_statistics()
        elif choice == "7":
            print("\n👋 Thank you for using Task Manager!\n")
            break
        else:
            print("\n❌ Invalid choice. Please try again.\n")

# ▶️ PROGRAM START
if __name__ == "__main__":
    clear_screen()
    main()