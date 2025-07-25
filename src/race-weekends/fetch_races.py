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
    Returns a list of dictionaries with year as key and a list of rounds as keys.
    """
    season_schedules = glob.glob(os.path.join(season_calender, "*.csv"))
    # print(season_schedules)
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

def get_race_results(championship_year, round_number):
    """
    Gives race results and weekend information from taking 
    a year and round number. Returns a pandas dataframe of 
    the race results and weekend information.
    """
    event = fastf1.get_event(championship_year, round_number)
    weekend = pd.DataFrame(event).transpose().reset_index()
    weekend.drop(columns=["F1ApiSupport", "index"], inplace=True)

    # print(f"Event: {event}")
    race_session = event.get_race()
    print(f"Race Session: {race_session}")
    race_session.load()
    # print(race_session.results)
    race_results = race_session.results


    race_results["Event"] = race_session
    race_results.drop(columns=["HeadshotUrl", "BroadcastName",
                               "FirstName", "LastName",
                               "Q1", "Q2", "Q3"], inplace=True)
    # print(race_results["Time"].dtype)

    return race_results, weekend

if __name__ == "__main__":
#     print(parse_number_of_rounds())
    results, race_weekend = get_race_results(2022, 5)
    # print(results.columns)
    # print(results.head())
    print(race_weekend)
    # results.to_csv(f"results.csv", index=False)
    race_weekend.to_csv(f"weekend_info.csv", index=False)