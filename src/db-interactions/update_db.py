from ORM_util import Race_Results 
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import pandas as pd

engine = create_engine("sqlite:///db/f1-test.db", echo=True)
race_results = pd.read_csv("results.csv")
weekend_info = pd.read_csv("weekend_info.csv")
# print(data.head())
def update_database(wk_info, results, engine = engine):
    with Session(engine) as session:
        wk_info.to_sql("Weekend_Info", con=engine, index=False)
        results.to_sql("Race_Results", con=engine, index=False)

        session.commit()

if __name__ == "__main__":
    update_database(weekend_info, race_results)