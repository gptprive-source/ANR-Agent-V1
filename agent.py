from workflows.main_workflow import WorkflowManager
from modules import interphone, relais_colis
from utils.helpers import log

class ANRAgent:
    def __init__(self):
        self.workflow_manager = WorkflowManager()
        self.modules = {
            "interphone": interphone,
            "relais_colis": relais_colis
        }

    def run_task(self, task_name, **kwargs):
        log(f"Running task: {task_name}")
        if task_name in self.modules:
            self.modules[task_name].execute(**kwargs)
        else:
            log(f"Task {task_name} not found in modules.")

    def start(self):
        log("ANR-Agent started")
        self.workflow_manager.run(self)

if __name__ == "__main__":
    agent = ANRAgent()
    agent.start()

