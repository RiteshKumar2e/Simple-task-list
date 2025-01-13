# Task Manager 

A simple command-line application for managing tasks, powered by Python and basic machine learning. This tool allows you to add, remove, list, and recommend tasks based on priority.

# Features

This application simplifies task management by combining traditional task operations with machine learning capabilities for smart recommendations.

Add Tasks: Add new tasks with descriptions and priority levels.

Remove Tasks: Delete tasks by their description.

List Tasks: Display all tasks in the list.

Task Recommendation: Recommends a high-priority task using a basic machine learning model.

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
