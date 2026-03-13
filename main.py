import random

class AIGo:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        """
        Add a task to the AI tool.
        :param task: A string representing the task to be performed.
        """
        self.tasks.append(task)

    def perform_random_task(self):
        """
        Perform a random task from the list of tasks.
        """
        if not self.tasks:
            return "No tasks available."
        task = random.choice(self.tasks)
        return f'Performing task: {task}'

if __name__ == '__main__':
    ai_tool = AIGo()
    ai_tool.add_task('Analyze data')
    ai_tool.add_task('Generate report')
    print(ai_tool.perform_random_task())