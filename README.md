# Scheduler TDD – TP Programmation Python

## 1. Objectif

Développer un **scheduler** capable de gérer l’exécution de tâches planifiées en Python (le choix du lnagage), avec différentes périodicités et en suivant une approche **TDD** (Test Driven Development).  


## 2. Périodicités implémentées

- **EveryMinute** → chaque minute  
- **EveryDayAt(hour, minute)** → tous les jours à une heure précise  
- **EveryHourAtMinute(minute)** → toutes les heures à une minute précise  
- **EveryDayAtMinute(minute)** → chaque jour à une minute précise  
- **EveryWeekAtDayHourMinute(day, hour, minute)** → jours précis de la semaine à heure et minute données  
- **MultipleDaysAtHourMinute(jours, hour, minute)** → plusieurs jours à heure et minute précises  
- **EveryXMinutes(interval)** → toutes les X minutes, avec gestion du drift  
- **EveryXHours(interval)** → toutes les X heures, avec gestion du drift  
- **EveryXMonthsAtHourMinute(interval, hour, minute)** → tous les X mois à heure et minute précises  
- **LastDayOfMonth** → dernier jour du mois  
- **LastFridayOfMonth** → dernier vendredi du mois  
- **OrPeriodicity(periodicities)** → combinaison “OR” de plusieurs périodicités  


## 3. Tests TDD

- Les tests utilisent **FakeClock** pour simuler le temps et garantir des résultats déterministes.  
- Chaque périodicité dispose d’un test vérifiant :  
  - que la tâche s’exécute au bon moment,  
  - qu’elle ne s’exécute pas hors période,  
  - que la répétition se fait correctement selon l’intervalle.  


## 4. Refactor

Pendant le refactor, le code a été amélioré pour :

- **La centralisation et la simplification de la logique** des périodicités : chaque classe gère uniquement sa propre logique d’exécution.  
- **La gestion de drift** pour `EveryXMinutes`, `EveryXHours`, et `EveryXMonthsAtHourMinute` : même si `update()` est appelé avec un retard, la tâche s’exécute correctement.  
- **Faciliter l’extension** : l’ajout de nouvelles périodicités ou combinaisons (comme `OrPeriodicity`) ne nécessite pas de modification du scheduler principal.  
- **L'amélioration de la lisibilité et la maintenance** : le code a été rendu plus modulaire et clair, les tests sont inchangés après le refactor.
