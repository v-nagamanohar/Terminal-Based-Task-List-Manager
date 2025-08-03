# ✅ Task List Manager (Console-based To-Do App)

A simple command-line task manager built with Python. It allows users to add, view, mark, and delete tasks with persistent storage using a local `tasks.txt` file. Great for beginners to learn file I/O, conditionals, and list management in Python.

---

## 📋 Features

- ✅ Add a new task  
- 📄 View all tasks  
- ✔️ Mark tasks as complete  
- ❌ Delete tasks  
- 💾 Task persistence using `tasks.txt`  
- 📌 Status: done ✅ or not done ⬜

---

## 🧠 Concepts Used

- File handling (`open`, `read`, `write`)  
- Data persistence with a `.txt` file  
- Dictionaries & lists  
- Exception handling (`try-except`)  
- `match-case` pattern (Python 3.10+)  
- Basic string operations and formatting  

---

## 📂 File Format

Each task is saved in the following format in `tasks.txt`:
```
Task Text Here||done
Another Task||not_done
```

---

## 🚀 How to Run

1. Make sure you have Python 3.10+ installed.
2. Save the code in a file called `task_manager.py`.
3. Open terminal/command prompt and run:
   ```bash
   python task_manager.py
   ```
4. Choose from the menu:
   - `1`: Add Task
   - `2`: View Tasks
   - `3`: Mark Task as Complete
   - `4`: Delete Task
   - `5`: Exit

---

## 🖥 Sample Output

```
---------Task List Manager----------
1. Add Task
2. View Task
3. Mark Task as complete
4. Delete Task
5. Exit
Choose an option (1-5): 2

1.[✅] Buy groceries
2.[ ] Study for exam
```

---

