import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
def batsman_data():
    data = pd.read_csv('C:\\Users\\shash\\OneDrive\\IPL Analysis Project\\datasets\\All-Time-Best-Batsman.csv')
    data.dropna(inplace=True)
    return data

def bowler_data():
    bowl = pd.read_csv('C:\\Users\\shash\\OneDrive\\IPL Analysis Project\\datasets\\All-Time-Best-Bowlers.csv')
    bowl.dropna(inplace=True)
    return bowl

def Top_Scorers(data):
    Top_Scorers = data.sort_values(by='Runs', ascending=False).head(10)
    fig, ax = plt.subplots()
    ax.bar(Top_Scorers['Player'], Top_Scorers['Runs'], color='blue')
    ax.set_title('Top 10 Scorers in IPL History')
    ax.set_xlabel('Player')
    ax.set_ylabel('Total Runs')
    ax.set_xticklabels(Top_Scorers['Player'], rotation=90)
    return fig

def Most_4s(data):
    Most_4s = data.sort_values(by='4s', ascending=False).head(10)
    fig, ax = plt.subplots()
    ax.bar(Most_4s['Player'], Most_4s['4s'], color='green')
    ax.set_title('Top 10 Players with Most Fours in IPL History')
    ax.set_xlabel('Player')
    ax.set_ylabel('Total Fours')
    ax.set_xticklabels(Most_4s['Player'], rotation=90)
    return fig

def Most_sr(data):
    Most_sr = data.sort_values(by='SR', ascending=False).head(10)
    fig, ax = plt.subplots()
    ax.bar(Most_sr['Player'], Most_sr['SR'], color='orange')
    ax.set_title('Top 10 Players with Highest Strike Rate in IPL History')
    ax.set_xlabel('Player')
    ax.set_ylabel('Strike Rate')
    ax.set_xticklabels(Most_sr['Player'], rotation=90)
    return fig

def Most_6s(data):
    Most_6s = data.sort_values(by='6s', ascending=False).head(10)
    fig, ax = plt.subplots()
    ax.bar(Most_6s['Player'], Most_6s['6s'], color='red')
    ax.set_title('Top 10 Players with Most Sixes in IPL History')
    ax.set_xlabel('Player')
    ax.set_ylabel('Total Sixes')
    ax.set_xticklabels(Most_6s['Player'], rotation=90)
    return fig

def Best_avg(data):
    Best_avg = data.sort_values(by='Avg', ascending=False).head(10)
    fig, ax = plt.subplots()
    ax.bar(Best_avg['Player'], Best_avg['Avg'], color='purple')
    ax.set_title('Top 10 Players with Best Batting Average in IPL History')
    ax.set_xlabel('Player')
    ax.set_ylabel('Batting Average')
    ax.set_xticklabels(Best_avg['Player'], rotation=90)
    return fig

def Most_wkts(data):
    Most_wkts = data.sort_values(by='Wkts', ascending=False).head(10)
    fig, ax = plt.subplots()
    ax.scatter(Most_wkts['Player'], Most_wkts['Wkts'], color='brown')
    ax.set_title('Top 10 Bowlers with Most Wickets in IPL History')
    ax.set_xlabel('Player')
    ax.set_ylabel('Total Wickets')
    ax.set_xticklabels(Most_wkts['Player'], rotation=90)
    return fig

def Best_bowl_avg(data):
    Best_bowl_avg = data.sort_values(by='Avg', ascending=True).head(10)
    fig, ax = plt.subplots()
    ax.scatter(Best_bowl_avg['Player'], Best_bowl_avg['Avg'], color='cyan')
    ax.set_title('Top 10 Bowlers with Best Bowling Average in IPL History')
    ax.set_xlabel('Player')
    ax.set_ylabel('Bowling Average')
    ax.set_xticklabels(Best_bowl_avg['Player'], rotation=90)
    return fig

def Best_Econ(data):
    Best_Econ = data.sort_values(by='Econ', ascending=True).head(10)
    fig, ax = plt.subplots()
    ax.scatter(Best_Econ['Player'], Best_Econ['Econ'], color='magenta')
    ax.set_title('Top 10 Bowlers with Best Economy Rate in IPL History')
    ax.set_xlabel('Player')
    ax.set_ylabel('Economy Rate')
    ax.set_xticklabels(Best_Econ['Player'], rotation=90)
    return fig

def Most_4wkts(data):
    Most_4wkts = data.sort_values(by='4w', ascending=False).head(10)
    fig, ax = plt.subplots()
    ax.bar(Most_4wkts['Player'], Most_4wkts['4w'], color='yellow')
    ax.set_title('Top 10 Bowlers with Most 4 Wicket Hauls in IPL History')
    ax.set_xlabel('Player')
    ax.set_ylabel('Total 4 Wicket Hauls')
    ax.set_xticklabels(Most_4wkts['Player'], rotation=90)
    return fig

def Most_5wkts(data):
    Most_5wkts = data.sort_values(by='5w', ascending=False).head(10)
    fig, ax = plt.subplots()
    ax.bar(Most_5wkts['Player'], Most_5wkts['5w'], color='grey')
    ax.set_title('Top 10 Bowlers with Most 5 Wicket Hauls in IPL History')
    ax.set_xlabel('Player')
    ax.set_ylabel('Total 5 Wicket Hauls')
    ax.set_xticklabels(Most_5wkts['Player'], rotation=90)
    return fig

def Best_bowl_sr(data):
    Best_bowl_sr = data.sort_values(by='SR', ascending=True).head(10)
    fig, ax = plt.subplots()
    ax.scatter(Best_bowl_sr['Player'], Best_bowl_sr['SR'], color='lime')
    ax.set_title('Top 10 Bowlers with Best Strike Rate in IPL History')
    ax.set_xlabel('Player')
    ax.set_ylabel('Bowling Strike Rate')
    ax.set_xticklabels(Best_bowl_sr['Player'], rotation=90)
    return fig

def sr_vs_avg(bowl):
    fig, ax = plt.subplots(figsize=(10,6))
    ax.scatter(bowl['SR'],bowl['Avg'])
    ax.set_title('Strike Rate vs Average')
    ax.set_xlabel('Strike Rate')
    ax.set_ylabel('Average')
    return fig

def corrheatmap(data):
    numeric_cols = data.select_dtypes(include='number')

    fig, ax = plt.subplots(figsize=(10,8))

    sns.heatmap(
        numeric_cols.corr(),
        annot=True,
        cmap='coolwarm'
    )

    ax.set_title('IPL Dataset Correlation Heatmap')
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