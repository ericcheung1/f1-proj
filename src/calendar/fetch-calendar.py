import fastf1
import pandas as pd

def fetching_calendar(starting_season):
    while True:
        schedule = fastf1.get_event_schedule(starting_season)
        print(schedule.head())

        if not schedule.empty:
            schedule.to_csv(f"data/season-calendar/f1-schedule-{starting_season}.csv", index=False)
        
        starting_season += 1
        
        if schedule.empty:
            print(f"breaking loop!")
            break