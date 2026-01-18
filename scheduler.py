from typing import Callable, Dict, List

class Scheduler:
    def __init__(self, clock):
        self._tasks: Dict[str, 'Task'] = {}
        self._clock = clock

    def set_task(self, name: str, schedule, action: Callable):
        self._tasks[name] = Task(name, schedule, action)

    def get_scheduled_tasks(self) -> List[str]:
        return list(self._tasks.keys())
    

class Task:
    def __init__(self, name: str, schedule, action: Callable):
        self.name = name
        self.schedule = schedule
        self.action = action
        
        
