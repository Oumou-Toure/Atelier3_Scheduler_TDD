import calendar

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


class EveryXHours:
    def __init__(self, interval: int):
        self.interval = interval  
        self.last_run = None

    def a_executer(self, temps_actuel):
        if self.last_run is None:
            self.last_run = temps_actuel
            return False  

        delta_hours = (temps_actuel - self.last_run).total_seconds() / 3600
        if delta_hours >= self.interval:
            self.last_run = temps_actuel
            return True
        return False

class EveryXMonthsAtHourMinute:
    def __init__(self, interval: int, hour: int, minute: int):
        self.interval = interval
        self.hour = hour
        self.minute = minute
        self.last_run_month = None
        self.last_run_year = None

    def a_executer(self, temps_actuel):
        if self.last_run_month is None:
            
            self.last_run_month = temps_actuel.month
            self.last_run_year = temps_actuel.year
            return True

        delta_months = (temps_actuel.year - self.last_run_year) * 12 + (temps_actuel.month - self.last_run_month)
        if delta_months >= self.interval and temps_actuel.hour == self.hour and temps_actuel.minute == self.minute:
            self.last_run_month = temps_actuel.month
            self.last_run_year = temps_actuel.year
            return True

        return False


class LastDayOfMonth:
    def a_executer(self, temps_actuel):
        last_day = calendar.monthrange(temps_actuel.year, temps_actuel.month)[1]
        return temps_actuel.day == last_day



