from datetime import datetime
from scheduler import Scheduler
from periodicites import EveryDayAt, EveryMinute, EveryHourAtMinute, EveryDayAtMinute, EveryWeekAtDayHourMinute, MultipleDaysAtHourMinute, EveryXMinutes
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
    

def test_execution_tache_a_heure_prevue():
    
    heure = FakeClock(datetime(2026, 1, 18, 2, 59))
    scheduler = Scheduler(heure)

    executed = []

    scheduler.set_task(
        "backup",
        EveryDayAt(3, 0),
        lambda: executed.append("done")
    )

    scheduler.update()
    assert executed == []  

    heure.advance_minutes(1)
    scheduler.update()
    assert executed == ["done"]  
    
def test_execution_taches_toutes_les_minutes():
    
    heure = FakeClock(datetime(2026, 1, 18, 2, 0))
    scheduler = Scheduler(heure)

    executed = []

    scheduler.set_task(
        "minute_task",
        EveryMinute(),
        lambda: executed.append("done")
    )

    scheduler.update()
    assert executed == ["done"]  

    heure.advance_minutes(1)
    scheduler.update()
    assert executed == ["done", "done"]  


def test_execution_une_tache_toutes_les_heures_a_une_minute_précise():
    
    heure = FakeClock(datetime(2026, 1, 18, 2, 14))
    scheduler = Scheduler(heure)

    executed = []

    scheduler.set_task(
        "hour_minute_task",
        EveryHourAtMinute(15),  
        lambda: executed.append("done")
    )

    scheduler.update()
    assert executed == [] 

    heure.advance_minutes(1)
    scheduler.update()
    assert executed == ["done"]  

def test_execution_tous_les_jours_a_une_minute_precise_independant_de_heure():
    
    heure = FakeClock(datetime(2026, 1, 18, 2, 14))
    scheduler = Scheduler(heure)

    executed = []

    scheduler.set_task(
        "daily_minute_task",
        EveryDayAtMinute(15),
        lambda: executed.append("done")
    )

    scheduler.update()
    assert executed == []  

    heure.advance_minutes(1)  
    scheduler.update()
    assert executed == ["done"]  

    heure.advance_minutes(60)  
    scheduler.update()
    assert executed == ["done", "done"]


def test_execution_tache_un_jour_precis():

    heure = FakeClock(datetime(2026, 1, 19, 9, 59))  
    scheduler = Scheduler(heure)

    executed = []

    scheduler.set_task(
        "weekly_task",
        EveryWeekAtDayHourMinute(0, 10, 0),  
        lambda: executed.append("done")
    )

    scheduler.update()
    assert executed == [] 

    heure.advance_minutes(1)  
    scheduler.update()
    assert executed == ["done"]  
    

def test_execution_plusieurs_jours_a_heure_minute_precise():
    
    heure = FakeClock(datetime(2026, 1, 19, 14, 29))  
    scheduler = Scheduler(heure)
    executed = []


    scheduler.set_task(
        "multi_day_task",
        MultipleDaysAtHourMinute([0, 2, 4], 14, 30),
        lambda: executed.append("done")
    )

    scheduler.update()
    assert executed == []  

    heure.advance_minutes(1)  
    scheduler.update()
    assert executed == ["done"]

    heure.advance_minutes(24*60) 
    scheduler.update()
    assert executed == ["done"]  

    
    heure.advance_minutes(24*60)  
    scheduler.update()
    assert executed == ["done", "done"]

    
    heure.advance_minutes(2*24*60)  
    scheduler.update()
    assert executed == ["done", "done", "done"]


def test_execution_tache_toutes_les_X_minutes():
    
    heure = FakeClock(datetime(2026, 1, 18, 2, 0))
    scheduler = Scheduler(heure)

    executed = []

    scheduler.set_task(
        "every_3_minutes_task",
        EveryXMinutes(3),
        lambda: executed.append("done")
    )

    scheduler.update()
    assert executed == []

    heure.advance_minutes(2)
    scheduler.update()
    assert executed == []

    heure.advance_minutes(1)
    scheduler.update()
    assert executed == ["done"]

    heure.advance_minutes(3)
    scheduler.update()
    assert executed == ["done", "done"]
