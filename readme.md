# 📝 My Simple CLI Task Manager

Hey! Welcome to my CLI Task Manager. I built this because I wanted a quick, no-distraction way to jot down my to-dos straight from the terminal. Big apps can be too slow, so this is just a simple Python script that gets straight to the point. 

It uses a basic JSON file to save everything, so you don't have to mess around with setting up a database or anything complicated. 

## ✨ What can it do?
* **Says Hello:** It asks for your name when you boot it up just to make things a little more personal.
* **Quick Task Entry:** Just type what you need to do. The app automatically slaps the exact date and time on it for you.
* **Clean Viewing:** Shows all your active tasks in a simple, numbered list.
* **Easy Deletion:** Finished a task? Just type its number and it's gone.
* **Auto-Saves Everything:** Every time you add or remove something, it instantly saves to a local JSON file. You won't lose your list if you close the terminal.

## 📂 What's inside the folder?
* `main.py`: This is the star of the show. It's the only file you actually need to run!
* `db.py`: The behind-the-scenes worker that handles saving, loading, and deleting data from the JSON file.
* `Task.py`, `display_file.py` & `Report.py`: A few helper files I made to keep the code organized and handle specific parts of the app (like the menus).
* `tasks_data.json`: The actual file where all your tasks and timestamps are stored.

## 🚀 How to run it
1. Make sure you have Python installed on your computer.
2. Open up your terminal or command prompt.
3. Run this command: `python main.py`
4. Boom, you're in! Just follow the on-screen menu to manage your day.