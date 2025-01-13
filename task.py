import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import random

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
        print(f"Task added: {description} with priority {priority}")

    def remove_task(self, description):
        self.tasks = self.tasks[self.tasks['description'] != description]
        self.save_tasks()
        print(f"Task removed: {description}")

    def list_tasks(self):
        if self.tasks.empty:
            print("No tasks available.")
        else:
            print(self.tasks)

    def recommend_task(self):
        if not self.tasks.empty:
            high_priority_tasks = self.tasks[self.tasks['priority'] == 'High']

            if not high_priority_tasks.empty:
                random_task = random.choice(high_priority_tasks['description'].tolist())
                print(f"Recommended task: {random_task} - Priority: High")
            else:
                print("No high-priority tasks available for recommendation.")
        else:
            print("No tasks available for recommendations.")
if __name__ == "__main__":
    manager = TaskManager()

    while True:
        print("\nTask Management App")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. List Tasks")
        print("4. Recommend Task")
        print("5. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            description = input("Enter task description: ")
            priority = input("Enter task priority (Low/Medium/High): ").capitalize()
            manager.add_task(description, priority)

        elif choice == "2":
            description = input("Enter task description to remove: ")
            manager.remove_task(description)

        elif choice == "3":
            manager.list_tasks()

        elif choice == "4":
            manager.recommend_task()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please select a valid option.")
