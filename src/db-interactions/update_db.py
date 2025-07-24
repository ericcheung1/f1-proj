from ORM_util import Race_Results 
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import pandas as pd

engine = create_engine("sqlite:///db/f1-test.db", echo=True)
data = pd.read_csv("results.csv")
# print(data.head())

with Session(engine) as session:
    data.to_sql("Race_Results", con=engine, if_exists="fail", index=False)

    session.commit()