from ORM_util import Race_Results 
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import pandas as pd

engine = create_engine("sqlite:///db/f1-test.db", echo=True)
results = pd.read_csv("results.csv")
wk_info = pd.read_csv("weekend_info.csv")
# print(data.head())

with Session(engine) as session:
    wk_info.to_sql("Weekend_Info", con=engine, if_exists="replace", index=False)
    results.to_sql("Race_Results", con=engine, if_exists="replace", index=False)

    session.commit()