from datetime import datetime
from scheduler import Scheduler
from periodicites import EveryDayAt
from heures import FakeClock

def test_ajout_taches():
    
    heure = FakeClock(datetime(2026, 1, 18, 2, 0))
    scheduler = Scheduler(heure)
    scheduler.set_task("backup", EveryDayAt(3, 0), lambda: None)
    
    assert "backup" in scheduler.get_scheduled_tasks()

def test_supprimer_tache():
    
    heure = FakeClock(datetime(2026, 1, 18, 2, 0))
    scheduler = Scheduler(heure)

    scheduler.set_task("backup", EveryDayAt(3, 0), lambda: None)
    scheduler.remove_task("backup")

    assert "backup" not in scheduler.get_scheduled_tasks()
