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

class EveryHourAtMinute:
    def __init__(self, minute: int):
        self.minute = minute

    def a_executer(self, temps_actuel):
        return temps_actuel.minute == self.minute

class EveryDayAtMinute:
    def __init__(self, minute: int):
        self.minute = minute

    def a_executer(self, temps_actuel):
        return temps_actuel.minute == self.minute

class EveryWeekAtDayHourMinute:
    def __init__(self, day: int, hour: int, minute: int):
        self.day = day        
        self.hour = hour
        self.minute = minute

    def a_executer(self, temps_actuel):
        return (
            temps_actuel.weekday() == self.day and
            temps_actuel.hour == self.hour and
            temps_actuel.minute == self.minute
        )

class MultipleDaysAtHourMinute:
    def __init__(self, jours: list[int], hour: int, minute: int):
        
        self.jours = jours
        self.hour = hour
        self.minute = minute

    def a_executer(self, temps_actuel):
        return (
            temps_actuel.weekday() in self.jours
            and temps_actuel.hour == self.hour
            and temps_actuel.minute == self.minute
        )

class EveryXMinutes:
    def __init__(self, interval: int):
        self.interval = interval
        self.last_run = None

    def a_executer(self, temps_actuel):
        if self.last_run is None:
            
            self.last_run = temps_actuel
            return False  

        delta = (temps_actuel - self.last_run).total_seconds() / 60
        if delta >= self.interval:
            self.last_run = temps_actuel
            return True
        return False

