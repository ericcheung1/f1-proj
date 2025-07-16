import os
import pandas as pd
import fastf1

project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
season_calender = os.path.join(project_root, "data/season-calendar")
print(season_calender)

event1 = fastf1.get_event(2024, 1)
race1 = event1.get_race()
race1_info = race1.load()
print(race1_info)