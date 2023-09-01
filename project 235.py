import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_object as go
import plotly.express as px
dataset=pd.read_csv('projectC234_EPL.csv')
football_club=dataset['Club'].value_counts().head(20)
print("top 20 clubs with maximum penalty accuracy premier league \n,football_club")
club_fig=go.Figure(data=[go.Pie(labels=football_club.index,value=football_club.value,hole=0.5)])
club_fig.show()