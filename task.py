import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import random
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

class TaskManager:
    def __init__(self):
        self.tasks = pd.DataFrame(columns=['description', 'priority'])
        try:
            self.tasks = pd.read_csv('tasks.csv')
        except FileNotFoundError:
            pass
        if not self.tasks.empty:
            self.train_model()

    def save_tasks(self):
        self.tasks.to_csv('tasks.csv', index=False)

    def train_model(self):
        self.vectorizer = CountVectorizer()
        self.clf = MultinomialNB()
        self.model = make_pipeline(self.vectorizer, self.clf)
        if not self.tasks.empty:
            self.model.fit(self.tasks['description'], self.tasks['priority'])

    def add_task(self, description, priority):
        new_task = pd.DataFrame({'description': [description], 'priority': [priority]})
        self.tasks = pd.concat([self.tasks, new_task], ignore_index=True)
        self.save_tasks()
        self.train_model()
        messagebox.showinfo("Success", f"Task added: {description} with priority {priority}")

    def remove_task(self, description):
        self.tasks = self.tasks[self.tasks['description'] != description]
        self.save_tasks()
        messagebox.showinfo("Success", f"Task removed: {description}")

    def list_tasks(self):
        if self.tasks.empty:
            messagebox.showinfo("Tasks", "No tasks available.")
        else:
            tasks_str = self.tasks.to_string(index=False)
            messagebox.showinfo("Tasks", tasks_str)

    def recommend_task(self):
        if not self.tasks.empty:
            high_priority_tasks = self.tasks[self.tasks['priority'] == 'High']
            if not high_priority_tasks.empty:
                random_task = random.choice(high_priority_tasks['description'].tolist())
                messagebox.showinfo("Recommendation", f"Recommended task: {random_task} - Priority: High")
            else:
                messagebox.showinfo("Recommendation", "No high-priority tasks available for recommendation.")
        else:
            messagebox.showinfo("Recommendation", "No tasks available for recommendations.")


def main():
    manager = TaskManager()

    def add_task():
        description = simpledialog.askstring("Input", "Enter task description:")
        if description:
            priority = simpledialog.askstring("Input", "Enter task priority (Low/Medium/High):").capitalize()
            if priority in ["Low", "Medium", "High"]:
                manager.add_task(description, priority)
            else:
                messagebox.showerror("Error", "Invalid priority. Please enter Low, Medium, or High.")

    def remove_task():
        description = simpledialog.askstring("Input", "Enter task description to remove:")
        if description:
            manager.remove_task(description)

    def list_tasks():
        manager.list_tasks()

    def recommend_task():
        manager.recommend_task()

    def exit_app():
        root.destroy()
    root = tk.Tk()
    root.title("Task Management App")
    root.state('zoomed')  

    tk.Button(root, text="Add Task", command=add_task, width=20, height=2).pack(pady=20)
    tk.Button(root, text="Remove Task", command=remove_task, width=20, height=2).pack(pady=20)
    tk.Button(root, text="List Tasks", command=list_tasks, width=20, height=2).pack(pady=20)
    tk.Button(root, text="Recommend Task", command=recommend_task, width=20, height=2).pack(pady=20)
    tk.Button(root, text="Exit", command=exit_app, width=20, height=2).pack(pady=20)

    root.mainloop()


if __name__ == "__main__":
    main()
