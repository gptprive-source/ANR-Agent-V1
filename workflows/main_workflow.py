class WorkflowManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_name, **kwargs):
        self.tasks.append((task_name, kwargs))

    def run(self, agent):
        from utils.helpers import log
        log("Workflow started")
        for task_name, kwargs in self.tasks:
            agent.run_task(task_name, **kwargs)
        log("Workflow finished")

