from datetime import datetime, timedelta

class FakeClock:
    def __init__(self, start_time: datetime):
        self._current_time = start_time

    def advance_minutes(self, minutes: int):
        self._current_time += timedelta(minutes=minutes)

    def now(self) -> datetime:
        return self._current_time
