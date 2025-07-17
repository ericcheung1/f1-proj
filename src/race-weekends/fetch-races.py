import os
import glob
import pandas as pd
import re
import fastf1

project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
season_calender = os.path.join(project_root, "data/season-calendar")
# print(project_root)
# print(season_calender)

def parse_number_of_rounds():
    """
    Tells you the number of rounds from a particular F1 season using schedule csv.
    """
    season_schedules = glob.glob(os.path.join(season_calender, "*.csv"))
    print(season_schedules)
    season_dicts = []

    for file in season_schedules:
        # print(file)
        schedule = pd.read_csv(file)
        rounds_list = list(schedule.iloc[:, 0])
        rounds_list.remove(0)
        # print(rounds_list)
        file_name = str(file)
        season_year = re.search(r"\b(\d{4})\b", file_name).group(1) # type: ignore
        season_dicts.append({season_year: rounds_list})
    
    return season_dicts

# event1 = fastf1.get_event(2024, 1)
# race1 = event1.get_race()
# race1.load()
# print(race1.results)
# race1.results.to_csv("race_results.csv", index=False)

if __name__ == "__main__":
    print(parse_number_of_rounds())