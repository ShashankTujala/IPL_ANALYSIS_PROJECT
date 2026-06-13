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
    Top_Scorers.plot(kind='bar', color='skyblue')
    plt.title('Top 10 Scorers in IPL History')
    plt.xlabel('Player')
    plt.ylabel('Total Runs')
    plt.xticks(rotation=90)
    plt.show()

def Most_4s(data):
    Most_4s = data.sort_values(by='4s', ascending=False).head(10)
    plt.bar(Most_4s['Player'], Most_4s['4s'], color='green')
    plt.title('Top 10 Players with Most Fours in IPL History')
    plt.xlabel('Player')
    plt.xticks(rotation=90)
    plt.ylabel('Total Fours')
    plt.show()

def Most_sr(data):
    Most_sr = data.sort_values(by='SR', ascending=False).head(10)
    plt.bar(Most_sr['Player'], Most_sr['SR'], color='orange')
    plt.title('Top 10 Players with Highest Strike Rate in IPL History')
    plt.xlabel('Player')
    plt.xticks(rotation=90)
    plt.ylabel('Strike Rate')
    plt.show()

def Most_6s(data):
    Most_6s = data.sort_values(by='6s', ascending=False).head(10)
    plt.bar(Most_6s['Player'], Most_6s['6s'], color='red')
    plt.title('Top 10 Players with Most Sixes in IPL History')
    plt.xlabel('Player')
    plt.xticks(rotation=90)
    plt.ylabel('Total Sixes')
    plt.show()

def Best_avg(data):
    Best_avg = data.sort_values(by='Avg', ascending=False).head(10)
    plt.bar(Best_avg['Player'], Best_avg['Avg'], color='purple')
    plt.title('Top 10 Players with Best Batting Average in IPL History')
    plt.xlabel('Player')
    plt.xticks(rotation=90)
    plt.ylabel('Batting Average')
    plt.show()

def Most_wkts(data):
    Most_wkts = data.sort_values(by='Wkts', ascending=False).head(10)
    plt.scatter(Most_wkts['Player'], Most_wkts['Wkts'], color='brown')
    plt.title('Top 10 Bowlers with Most Wickets in IPL History')
    plt.xlabel('Player')
    plt.xticks(rotation=90)
    plt.ylabel('Total Wickets')
    plt.show()

def Best_bowl_avg(data):
    Best_bowl_avg = data.sort_values(by='Avg', ascending=True).head(10)
    plt.scatter(Best_bowl_avg['Player'], Best_bowl_avg['Avg'], color='cyan')
    plt.title('Top 10 Bowlers with Best Bowling Average in IPL History')
    plt.xlabel('Player')
    plt.xticks(rotation=90)
    plt.ylabel('Bowling Average')
    plt.show()

def Best_Econ(data):
    Best_Econ = data.sort_values(by='Econ', ascending=True).head(10)
    plt.scatter(Best_Econ['Player'], Best_Econ['Econ'], color='magenta')
    plt.title('Top 10 Bowlers with Best Economy Rate in IPL History')
    plt.xlabel('Player')
    plt.xticks(rotation=90)
    plt.ylabel('Economy Rate')
    plt.show()

def Most_4wkts(data):
    Most_4wkts = data.sort_values(by='4w', ascending=False).head(10)
    plt.bar(Most_4wkts['Player'], Most_4wkts['4w'], color='yellow')
    plt.title('Top 10 Bowlers with Most 4 Wicket Hauls in IPL History')
    plt.xlabel('Player')
    plt.xticks(rotation=90)
    plt.ylabel('Total 4 Wicket Hauls')
    plt.show()

def Most_5wkts(data):
    Most_5wkts = data.sort_values(by='5w', ascending=False).head(10)
    plt.bar(Most_5wkts['Player'], Most_5wkts['5w'], color='grey')
    plt.title('Top 10 Bowlers with Most 5 Wicket Hauls in IPL History')
    plt.xlabel('Player')
    plt.xticks(rotation=90)
    plt.ylabel('Total 5 Wicket Hauls')
    plt.show()

def Best_bowl_sr(data):
    Best_bowl_sr = data.sort_values(by='SR', ascending=True).head(10)
    plt.scatter(Best_bowl_sr['Player'], Best_bowl_sr['SR'], color='lime')
    plt.title('Top 10 Bowlers with Best Strike Rate in IPL History')
    plt.xlabel('Player')
    plt.xticks(rotation=90)
    plt.ylabel('Bowling Strike Rate')
    plt.show()

def sr_vs_avg(bowl):
    sns.scatterplot(
    data=bowl,
    x='SR',
    y='Avg'
    )
    plt.title('Strike Rate vs Average')
    plt.show()
def corrheatmap(data):
    numeric_cols = data.select_dtypes(include='number')

    plt.figure(figsize=(10,8))

    sns.heatmap(
        numeric_cols.corr(),
        annot=True,
        cmap='coolwarm'
    )

    plt.title('IPL Dataset Correlation Heatmap')
    plt.show()