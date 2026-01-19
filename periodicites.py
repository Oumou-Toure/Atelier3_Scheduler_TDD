import calendar
from datetime import datetime

class HourMinutePeriodicity:
    def __init__(self, hour: int, minute: int):
        self.hour = hour
        self.minute = minute

    def matches_time(self, temps_actuel: datetime) -> bool:
        return temps_actuel.hour == self.hour and temps_actuel.minute == self.minute


class EveryDayAt(HourMinutePeriodicity):
    def a_executer(self, temps_actuel: datetime):
        return self.matches_time(temps_actuel)


class EveryMinute:
    def a_executer(self, temps_actuel: datetime):
        return True


class EveryHourAtMinute:
    def __init__(self, minute: int):
        self.minute = minute

    def a_executer(self, temps_actuel: datetime):
        return temps_actuel.minute == self.minute


class EveryDayAtMinute:
    def __init__(self, minute: int):
        self.minute = minute

    def a_executer(self, temps_actuel: datetime):
        return temps_actuel.minute == self.minute


class EveryWeekAtDayHourMinute(HourMinutePeriodicity):
    def __init__(self, day: int, hour: int, minute: int):
        super().__init__(hour, minute)
        self.day = day

    def a_executer(self, temps_actuel: datetime):
        return temps_actuel.weekday() == self.day and self.matches_time(temps_actuel)


class MultipleDaysAtHourMinute(HourMinutePeriodicity):
    def __init__(self, jours: list[int], hour: int, minute: int):
        super().__init__(hour, minute)
        self.jours = jours

    def a_executer(self, temps_actuel: datetime):
        return temps_actuel.weekday() in self.jours and self.matches_time(temps_actuel)


class EveryXBase:
    def __init__(self, interval: int):
        self.interval = interval
        self.last_run = None

    def should_run(self, delta: float, temps_actuel: datetime):
        if self.last_run is None:
            self.last_run = temps_actuel
            return False
        if delta >= self.interval:
            self.last_run = temps_actuel
            return True
        return False


class EveryXMinutes(EveryXBase):
    def a_executer(self, temps_actuel: datetime):
        delta = (temps_actuel - self.last_run).total_seconds() / 60 if self.last_run else 0
        return self.should_run(delta, temps_actuel)


class EveryXHours(EveryXBase):
    def a_executer(self, temps_actuel: datetime):
        delta_hours = (temps_actuel - self.last_run).total_seconds() / 3600 if self.last_run else 0
        return self.should_run(delta_hours, temps_actuel)


class EveryXMonthsAtHourMinute(HourMinutePeriodicity):
    def __init__(self, interval: int, hour: int, minute: int):
        super().__init__(hour, minute)
        self.interval = interval
        self.last_run_month = None
        self.last_run_year = None

    def a_executer(self, temps_actuel: datetime):
        if self.last_run_month is None:
            self.last_run_month = temps_actuel.month
            self.last_run_year = temps_actuel.year
            return True

        delta_months = (temps_actuel.year - self.last_run_year) * 12 + (temps_actuel.month - self.last_run_month)
        if delta_months >= self.interval and self.matches_time(temps_actuel):
            self.last_run_month = temps_actuel.month
            self.last_run_year = temps_actuel.year
            return True

        return False


class LastDayOfMonth:
    def a_executer(self, temps_actuel: datetime):
        last_day = calendar.monthrange(temps_actuel.year, temps_actuel.month)[1]
        return temps_actuel.day == last_day


class LastFridayOfMonth:
    def a_executer(self, temps_actuel: datetime):
        last_day = calendar.monthrange(temps_actuel.year, temps_actuel.month)[1]
        is_friday = temps_actuel.weekday() == 4
        is_last_friday = temps_actuel.day + 7 > last_day
        return is_friday and is_last_friday


class OrPeriodicity:
    def __init__(self, periodicities):
        self.periodicities = periodicities

    def a_executer(self, temps_actuel: datetime):
        return any(p.a_executer(temps_actuel) for p in self.periodicities)
