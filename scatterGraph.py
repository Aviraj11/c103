import pandas as pd
import plotly.express as px

df = pd.read_csv("./data_py.csv")
fig = px.scatter(df, x= "date", y= "cases", color = "country", title = "COVID Cases Chart")
fig.show()