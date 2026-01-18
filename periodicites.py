class EveryDayAt:
    def __init__(self, hour: int, minute: int):
        self.hour = hour
        self.minute = minute

    def a_executer(self, temps_actuel):
        
        return (
            temps_actuel.hour == self.hour
            and temps_actuel.minute == self.minute
        )
        
class EveryMinute:
    def a_executer(self, temps_actuel):
        return True  
