import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
def batsman_data():
    data = pd.read_csv('C:\\Users\\shash\\OneDrive\\IPL Analysis Project\\datasets\\All-Time-Best-Batsman.csv')
    data["HS"] = data["HS"].str.replace("*", "", regex=False).astype(int)
    data.dropna(inplace=True)
    return data

def bowler_data():
    bowl = pd.read_csv('C:\\Users\\shash\\OneDrive\\IPL Analysis Project\\datasets\\All-Time-Best-Bowlers.csv')
    bowl.dropna(inplace=True)
    return bowl

def Top_Scorers(data):
    Top_Scorers = data.sort_values(by='Runs', ascending=False).head(10)
    fig = px.bar(Top_Scorers, x = 'Player', y ='Runs',color = 'Runs', title = 'Top Scorers')
    fig.update_layout(xaxis_title='Player',yaxis_title='Runs')
    fig.update_traces(textposition='outside')
    return fig

def Most_4s(data):
    Most_4s = data.sort_values(by='4s', ascending=False).head(10)
    fig = px.bar(Most_4s, x = 'Player', y ='4s',color = '4s', title = 'Most fours')
    return fig

def Most_sr(data):
    Most_sr = data.sort_values(by='SR', ascending=False).head(10)
    fig = px.bar(Most_sr, x = 'Player', y ='SR',color = 'SR', title = 'Top Strike Rate')
    return fig

def Most_6s(data):
    Most_6s = data.sort_values(by='6s', ascending=False).head(10)
    fig = px.bar(Most_6s, x = 'Player', y ='6s',color = '6s', title = 'Most Sixes')
    return fig

def Best_avg(data):
    Best_avg = data.sort_values(by='Avg', ascending=False).head(10)
    fig = px.bar(Best_avg , x = 'Player', y ='Avg',color = 'Avg', title = 'Best Average')
    return fig

def Most_wkts(data):
    Most_wkts = data.sort_values(by='Wkts', ascending=False).head(10)
    fig = px.scatter(Most_wkts, x = 'Player', y='Wkts', color = 'Wkts', title = 'Most Wickets')
    return fig

def Best_bowl_avg(bowl):
    Best_bowl_avg = bowl.sort_values(by='Avg', ascending=True).head(10)
    fig = px.scatter(Best_bowl_avg, x = 'Player', y='Avg', color = 'Avg', title = 'Best Bowling Average')
    return fig

def Best_Econ(data):
    Best_Econ = data.sort_values(by='Econ', ascending=True).head(10)
    fig = px.scatter(Best_Econ, x = 'Player', y='Econ', color = 'Econ', title = 'Best Economy')
    return fig

def Most_4wkts(data):
    Most_4wkts = data.sort_values(by='4w', ascending=False).head(10)
    fig = px.scatter(Most_4wkts, x = 'Player', y='4w', color = '4w', title = 'Most 4 wicket Haul')
    return fig

def Most_5wkts(data):
    Most_5wkts = data.sort_values(by='5w', ascending=False).head(10)
    fig = px.scatter(Most_5wkts, x = 'Player', y='5w', color = '5w', title = 'Most 5 Wicket Haul')
    return fig

def Best_bowl_sr(data):
    Best_bowl_sr = data.sort_values(by='SR', ascending=True).head(10)
    fig = px.scatter(Best_bowl_sr, x = 'Player', y='SR', color = 'SR', title = 'Best Strike Rate')
    return fig

def sr_vs_avg(bowl):
    fig = px.scatter(Best_bowl_sr, x = 'SR', y='Avg', color = 'Avg', title = 'Strike Rate VS Average')
    return fig

def corrheatmap(data):
    numeric_cols = data.select_dtypes(include='number')
    corr_matrix = numeric_cols.corr()
    fig = px.imshow(corr_matrix, text_auto = True, aspect = 'auto', color_continuous_scale = 'RdBu_r', title = 'IPL Correlation Heatmap')
    fig.update_layout( height=700,width=900)
    return fig

def metriccorr(data, metric1, metric2):
    fig = px.scatter(data, x=metric1, y=metric2, hover_name="Player", trendline="ols", title=f"{metric1} vs {metric2}")
    return fig

def playercompare(data,player1,player2,stats):
    player1_data = data[data["Player"] == player1].iloc[0]
    player2_data = data[data["Player"] == player2].iloc[0]
    comparision_df = pd.DataFrame({
        "statistics": stats,
        player1 : [player1_data[stat] for stat in stats],
        player2 : [player2_data[stat] for stat in stats]
    })
    comparision_df = comparision_df.set_index("statistics")
    normalized = comparision_df.copy()

    for stat in normalized.index:
        max_val = normalized.loc[stat].max()
        normalized.loc[stat] = normalized.loc[stat] / max_val * 100
    normalized = normalized.reset_index()

    fig = px.bar(
        normalized,
        x=[player1, player2],
        y="statistics",
        barmode="group",
        orientation='h',
        title=f"{player1} vs {player2} (Normalized)"
    )
    return fig

def total_runs(data):
    return data['Runs'].sum()
def highest_run_scorer(data):
    return data.loc[data['Runs'].idxmax(), 'Player']
def highest_avg(data):
    return data.loc[data['Avg'].idxmax(), 'Player']
def total_4s(data):
    return data['4s'].sum()
def total_6s(data):
    return data['6s'].sum()
def highest_sr(data):
    return data.loc[data['SR'].idxmax(),'Player']
def total_wickets(bowl): 
    return bowl['Wkts'].sum()
def highest_wickets(bowl):
    return bowl.loc[bowl['Wkts'].idxmax(), 'Player']
def best_econ_player(bowl):
    return bowl.loc[bowl['Econ'].idxmin()]
def best_bowl_avg_player(bowl):
    return bowl.loc[bowl['Avg'].idxmax(), 'Player']
def best_bowling_sr(bowl):
    return bowl.loc[bowl['SR'].idxmax(), 'Player']
def best_bbi_score(bowl):
    return bowl.loc[bowl['BBI'].idxmax(), 'Player']