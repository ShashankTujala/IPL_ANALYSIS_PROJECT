import os
import sys
import streamlit as st 
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)
#print(os.getcwd())
#print(project_root)
from src.analysis import Top_Scorers
from src.analysis import batsman_data
from src.analysis import bowler_data
from src.analysis import Most_4s
from src.analysis import Most_sr    
from src.analysis import Most_6s
from src.analysis import Best_avg   
from src.analysis import Best_bowl_avg
from src.analysis import Best_Econ
from src.analysis import Most_4wkts
from src.analysis import Most_5wkts 
from src.analysis import Best_bowl_sr
from src.analysis import sr_vs_avg  
from src.analysis import corrheatmap
from src.analysis import Most_wkts
from src.analysis import total_runs
from src.analysis import highest_run_scorer
from src.analysis import highest_avg
from src.analysis import total_4s
from src.analysis import total_6s
from src.analysis import highest_sr
from src.analysis import total_wickets
from src.analysis import highest_wickets
from src.analysis import best_econ_player
from src.analysis import best_bowl_avg_player
from src.analysis import best_bowling_sr
from src.analysis import best_bbi_score

data = batsman_data()
bowl = bowler_data()
fig1 = Top_Scorers(data)
fig2 = Most_4s(data)
fig3 = Most_6s(data)
fig4 = Most_sr(data)
fig5 = Best_avg(data)
fig6 = Best_bowl_avg(bowl)
fig7 = Best_Econ(bowl)
fig8 = Most_4wkts(bowl)
fig9 = Most_5wkts(bowl)
fig10 = Best_bowl_sr(bowl)
fig11 = sr_vs_avg(bowl)
fig12 = corrheatmap(bowl)
fig13 = Most_wkts(bowl)  

st.title("IPL ANALYSIS DASHBOARD")

tab1, tab2, batterstab, bowlerstab = st.tabs(['Batting Analysis','Bowling Analysis','Batsman individual Analysis','bowlers individual Analysis'])
with tab1:
    st.pyplot(Top_Scorers(data))
    st.pyplot(Most_4s(data))
with tab2:
    st.pyplot(Most_wkts(bowl))
    st.pyplot(Best_Econ(bowl))
with batterstab:
    player_stat = st.selectbox("Select Player", data['Player'].unique())
    player_data = data[data['Player'] == player_stat].iloc[0]
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    with col1:
        st.metric('Represents Team', player_data['Team'] )
        st.metric('Matches played', player_data['Mat'] )
    with col2:    
        st.metric('Runs', player_data['Runs'])
        st.metric('Strike Rate', player_data['SR'])
        
    with col3:
        st.metric('4s', player_data['4s'] )
        st.metric('6s', player_data['6s'] ) 
    with col4:    
        st.metric('Batting Average', player_data['Avg']) 
        st.metric('Balls Faced', player_data['BF'] )
    with col5:
        st.metric('Innings played', player_data['Inns'])    
        st.metric('Highest score', player_data['HS'])
    with col6:
        st.metric('100s', player_data['100'])
        st.metric('50s', player_data['50'])
with bowlerstab:
    player_stat = st.selectbox("Select Player", bowl['Player'].unique())
    player_data = bowl[bowl['Player'] == player_stat].iloc[0]
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    with col1:
        st.metric('Represents Team', player_data['Team'] )
        st.metric('Matches Played', player_data['Mat'] )
    with col2:    
        st.metric('Wickets Taken', player_data['Wkts'])
        st.metric('Strike Rate', player_data['SR'])
    with col3:
        st.metric('4wkts Haul', player_data['4w'])
        st.metric('5wkts Haul', player_data['5w']) 
    with col4:    
        st.metric('Average', player_data['Avg']) 
        st.metric('Economy', player_data['Econ'])
    with col5:
        st.metric('Innings', player_data['Inns'])    
        st.metric('BBI', player_data['BBI'])
    with col6:
        st.metric('Overs Delivered', player_data['Ov'])
        st.metric('Runs conceded', player_data['Runs'])

st.subheader('Tournament Inights')
totruns , hruns = st.columns(2) 
with totruns:
    st.metric("Total Runs", total_runs(data))
with hruns:
    hrsno = data.loc[data['Player'] == highest_run_scorer(data), 'Runs'].values[0]
    st.metric("Highest Runs scored ", f"{highest_run_scorer(data)}")
    st.caption(f"{hrsno}")
hsr, havg = st.columns(2)
with hsr:
    hsrno = data.loc[data['Player'] == highest_sr(data), 'Runs'].values[0]
    st.metric('Highest Strike Rate', f"{highest_sr(data)}")
    st.caption(f"{hsrno}")
with havg:
    havgno = data.loc[data['Player'] == highest_avg(data), 'Avg'].values[0]
    st.metric('Highest Avg', f"{highest_avg(data)}")
    st.caption(f"{havgno}")
totfour, totsix = st.columns(2)
with totfour:
    st.metric("Total 4s", total_4s(data))
with totsix:
    st.metric("Total 6s", total_6s(data))

totwkts , hwkts = st.columns(2) 
with totwkts:
    st.metric("Total Wickets", total_wickets(bowl))
with hwkts:
    hwktsno = bowl.loc[bowl['Player'] == highest_wickets(bowl), 'Wkts'].values[0]
    st.metric("Highest wickets ", f"{highest_wickets(bowl)}" )
    st.caption(f"{hwktsno}")
hbowlsr, hbowlavg = st.columns(2)
with hbowlsr:
    hbowlsrno = bowl.loc[bowl['Player'] == best_bowling_sr(bowl), 'SR'].values[0]
    st.metric('Highest Bowling SR', f"{best_bowling_sr(bowl)}")
    st.caption(f"{hbowlsrno}")
with hbowlavg:
    hbowlavgno = bowl.loc[bowl['Player'] == best_bowl_avg_player(bowl), 'Avg'].values[0]
    st.metric('Highest Bowling Avg', f"{best_bowl_avg_player(bowl)}")
    st.caption(f"{hbowlavgno}")
bestecon, bestbbi = st.columns(2)
with bestecon:
    besteconno = best_econ_player(bowl)
    st.metric("Best Economy", f"{besteconno['Econ']}")
    st.caption(f"{besteconno['Player']}")
with bestbbi:
    bestbbino = bowl.loc[bowl['Player'] == best_bbi_score(bowl), 'BBI'].iloc[0]
    st.metric("Best BBI", f"{best_bbi_score(bowl)}")
    st.caption(f"{bestbbino}")


st.subheader("Top 10s Analysis")
options = st.sidebar.selectbox(
    "choose analysis", ["Top Scorers","Most Fours","Most Sixes","Strike Rate","Batting Average","Most Wickets","Bowling Average","Economy Rate","Bowling Strike Rate","Correlation Heatmap", "Strike Rate VS Average", "Most 4 wicket Haul", "Most 5 wicket Haul"]
)
if options == "Top Scorers":
    st.pyplot(fig1)

if options == "Most Fours":
    st.pyplot(fig2)

if options == "Most Sixes":
    st.pyplot(fig3)    

if options == "Strike Rate":
    st.pyplot(fig4)

if options == "Batting Average":
    st.pyplot(fig5)

if options == "Most Wickets":
    st.pyplot(fig13)

if options == "Bowling Average":
    st.pyplot(fig6)

if options == "Economy Rate":
    st.pyplot(fig7)

if options == "Bowling Strike Rate":
    st.pyplot(fig10)

if options == "Correlation Heatmap":
    st.pyplot(fig12)

if options == "Strike Rate VS Average":
    st.pyplot(fig11)

if options == "Most 4 wicket Haul":
    st.pyplot(fig8)

if options == "Most 5 wicket Haul":
    st.pyplot(fig9)
 
st.subheader("Datasets")
datasets = st.sidebar.selectbox("Datasets", ["Batsman data","bowlers data"])

if datasets == "Batsman data":
    st.subheader("Batsman data")
    st.dataframe(data)

if datasets == "bowlers data":
    st.subheader("Bowlers data")
    st.dataframe(bowl)

