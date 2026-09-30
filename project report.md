# Project Report: CLI Task Manager

## Introduction

This project is a straightforward, Python-based terminal app that helps you keep track of your daily tasks. Instead of clicking around a heavy interface, you just type in what you need to do directly in the command line. I built this using standard built-in Python tools like `json`, `os`, and `datetime`. This means anyone can download and run the code immediately without having to install extra third-party packages or libraries. 

## How the Code is Structured

I split the code up into a few different files so it isn't just one massive, messy script. Here is how it works:

* **Handling the Data (`db.py`):** This file does all the heavy lifting for the files. When it runs, it checks if `tasks_data.json` exists. If it doesn't, it creates a blank list. It has a few simple functions that open the file, add new text and timestamps to it, delete items by their list number, and save it all back. 

* **The Main Menu (`main.py`):** This is the core of the app. When you run it, it asks for your name and then puts you into a loop with a clear menu: Display Tasks, Add Task, Remove Task, and Logout. I also added some basic checks in here, like making sure the app doesn't crash if you try to type letters when it asks for a task number, and stopping you from submitting an empty task.

* **Extra Modules (`Task.py`, `display_file.py`, `Report.py`):** These are helper files I made to keep things modular. For example, `Task.py` isolates the loop for adding tasks so you can quickly add multiple things in a row. The other files handle specific menus for just viewing tasks and logging out.

## How Data is Saved

To make sure your tasks aren't lost when you close the terminal, the app uses a standard JSON file. I went with JSON because it's lightweight and super easy to read. 

Every time you add a task, the app creates a small dictionary with two pieces of information: the `task` (whatever text you typed) and `created_at` (the current date and time). The sample data shows it easily handles everything from studying notes to reminders to grab food, all cleanly stamped with the exact time you added them. It’s a simple setup, but it works perfectly for an everyday to-do list.