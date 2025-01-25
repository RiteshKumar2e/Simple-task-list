# Task Manager 

This application is a task management tool that allows users to manage their tasks with a simple and intuitive graphical user interface (GUI) built using Python's tkinter. The app enables users to add, remove, list, and get recommendations for tasks.

# Features

This application simplifies task management by combining traditional task operations with machine learning capabilities for smart recommendations.

1. Add Task
Allows users to input a detailed task description in a large text area.
Users can set a priority for the task (Low, Medium, or High).
Validates the priority input and ensures that both the description and priority are entered before adding the task.
The task is saved in a local CSV file (tasks.csv) for persistence.
2. Remove Task
Users can remove a task by entering its description.
The app checks for the specified task and removes it from the task list.
3. List Tasks
Displays a list of all tasks, including their descriptions and priorities, in a formatted popup window.
4. Recommend Task
Recommends a random high-priority task if available.
Provides an alert if there are no high-priority tasks or if the task list is empty.
5. Exit
Safely exits the application.

# How It Works

The application uses:

Pandas: To manage and store tasks in a CSV file.

Scikit-learn: For a machine learning pipeline that trains a Naive Bayes classifier on task descriptions and priorities.

CSV Persistence: All tasks are saved in a tasks.csv file for persistent storage.

# Prerequisites

Make sure you have Python installed along with the required libraries:
```bash
pip install pandas 

pip install scikit-learn

```

# GUI Overview
The GUI consists of a main window with the following buttons:

Add Task: Opens a new window with a text box for entering task descriptions and a field for specifying the priority.
Remove Task: Directly prompts the user to input the task description for removal.
List Tasks: Shows all tasks in a pop-up dialog box.
Recommend Task: Recommends a high-priority task in a pop-up dialog box.
Exit: Closes the application.

# Output 

![image](https://github.com/user-attachments/assets/47b4664e-97c4-4a06-8505-60cf5b5de38b)

![image](https://github.com/user-attachments/assets/123905e4-bf78-4e7b-b49e-3cb4226eee14)

![image](https://github.com/user-attachments/assets/33aab7ce-0be3-44db-a768-ecd7bafad065)

