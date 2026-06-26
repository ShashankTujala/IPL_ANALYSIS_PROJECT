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
from src.analysis import metriccorr
from src.analysis import playercompare
from src.report import generate_report

data = batsman_data()
bowl = bowler_data() 
pdf_file = generate_report(data, bowl)
with open(pdf_file, "rb") as pdf:
    st.download_button(label="📄 Download IPL Report",data=pdf,file_name="IPL_Analysis_Report.pdf",mime="application/pdf")
st.title("IPL ANALYSIS DASHBOARD")

tab1, tab2, batterstab, bowlerstab, corrmaps= st.tabs(['Batting Analysis','Bowling Analysis','Batsman Individual Stats','Bowlers Individual Stats', 'Corelation Analysis'])
with tab1:
    st.plotly_chart(Top_Scorers(data), key = 'c1')
    st.plotly_chart(Most_4s(data), key = 'c2')
with tab2:
    st.plotly_chart(Most_wkts(bowl), key = 'c3')
    st.plotly_chart(Best_Econ(bowl), key = 'c4')
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

    st.subheader('Head To Head Comparsion')

    col1, col2 = st.columns(2) 
    pname = data['Player'].unique()
    p1 = col1.selectbox('Choose Player 1', data['Player'].unique(), key = 's5')
    remain_names = [col for col in pname if col != p1]
    p2 = col2.selectbox('Choose Player 2', remain_names, key = 's6')

    st.subheader("Select Metrics")
    cb1, cb2, cb3 = st.columns(3)
    stats = []
    with cb1:
        if st.checkbox("Runs", value=True):
            stats.append("Runs")
        if st.checkbox("Average"):
            stats.append("Avg")
        if st.checkbox("Strike Rate", value=True):
            stats.append("SR")
        if st.checkbox("Highest Score"):
            stats.append("HS")
    with cb2:
        if st.checkbox("Matches"):
            stats.append("Mat")
        if st.checkbox("Innings"):
            stats.append("Inns")
        if st.checkbox("Not Outs"):
            stats.append("NO")
        if st.checkbox("Balls Faced"):
            stats.append("BF")
    with cb3:
        if st.checkbox("100s"):
            stats.append("100")
        if st.checkbox("50s"):
            stats.append("50")
        if st.checkbox("Fours", value=True):
            stats.append("4s")
        if st.checkbox("Sixes", value=True):
            stats.append("6s")

    st.plotly_chart(playercompare(data,p1,p2,stats))

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
    
    st.subheader('Head To Head Comparsion')

    col1, col2 = st.columns(2) 
    pname = bowl['Player'].unique()
    p1 = col1.selectbox('Choose Player 1', bowl['Player'].unique(), key = 's7')
    remain_names = [col for col in pname if col != p1]
    p2 = col2.selectbox('Choose Player 2', remain_names, key = 's8')

    st.subheader("Select Metrics")
    cb11, cb22, cb33 = st.columns(3)
    stats = []
    with cb11:
        if st.checkbox("Runs", value=True, key = 'bcb1'):
            stats.append("Runs")
        if st.checkbox("Average", key = 'bcb2'):
            stats.append("Avg")
        if st.checkbox("Bowling Strike Rate", value=True, key = 'bcb3'):
            stats.append("SR")
        if st.checkbox("Wickets Scored", value=True, key = 'bcb4'):
            stats.append("Wkts")
    with cb22:
        if st.checkbox("Matches", key = 'bcb5'):
            stats.append("Mat")
        if st.checkbox("Innings", key = 'bcb6'):
            stats.append("Inns")
        if st.checkbox("Overs Delivered", key = 'bcb7'):
            stats.append("Ov")
        if st.checkbox("Economy", value=True, key = 'bcb8'):
            stats.append("Econ")
    with cb33:
        if st.checkbox("4 Wicket Hauls", key = 'bcb9'):
            stats.append("4w")
        if st.checkbox("5 Wicket Hauls", key = 'bcb10'):
            stats.append("5w")
    st.plotly_chart(playercompare(bowl,p1,p2,stats))

    st.subheader('BBI Comparision')
    col1, col2 = st.columns(2)
    
    bpnames = bowl['Player'].unique()
    bp1 = col1.selectbox('Choose Player 1', bowl['Player'].unique(), key = 's9')
    remain_names = [col for col in bpnames if col != bp1]
    bp2 = col2.selectbox('Choose Player 2', remain_names, key = 's10')

    player1_data = bowl[bowl["Player"] == bp1].iloc[0]
    player2_data = bowl[bowl["Player"] == bp2].iloc[0]

    with col1:
        st.metric("BBI", player1_data["BBI"])

    with col2:
        st.metric("BBI", player2_data["BBI"])
    

with corrmaps:
    st.subheader('Batting Metrics')
    corr = data.corr(numeric_only=True)
    mapcol1 , mapcol2 = st.columns(2)
    mapcol1dis = mapcol1.selectbox("metric 1", corr.columns, key = 's1')
    remaining_metrics = [col for col in corr.columns if col != mapcol1dis]
    mapcol2dis = mapcol2.selectbox("metric 2", remaining_metrics, key = 's2')
    
    corr_value = corr.loc[mapcol1dis,mapcol2dis]

    st.metric("Correlation", f"{corr_value:.2f}")
    if corr_value >= 0.7:
        st.success("Strong Positive Correlation")
    elif corr_value >= 0.4:
        st.info("Moderate Positive Correlation")
    elif corr_value >= 0:
        st.warning("Weak Positive Correlation")
    elif corr_value <= -0.7:
        st.success("Strong Negative Correlation")
    elif corr_value <= -0.4:
        st.info("Moderate Negative Correlation")
    else:
        st.warning("Weak Negative Correlation")
    if mapcol1dis == mapcol2dis:
        st.info("Please select two different metrics to view the scatter plot.")
    else:
        st.plotly_chart(metriccorr(data, mapcol1dis, mapcol2dis),use_container_width=True)
    
    
    st.subheader('Bowling Metrics')
    corr = bowl.corr(numeric_only=True)
    mapcol1 , mapcol2 = st.columns(2)
    mapcol1dis = mapcol1.selectbox("metric 1", corr.columns, key = 's3')
    remaining_metrics = [col for col in corr.columns if col != mapcol1dis]
    mapcol2dis = mapcol2.selectbox("metric 2", remaining_metrics, key = 's4')
    
    corr_value = corr.loc[mapcol1dis,mapcol2dis]

    st.metric("Correlation", f"{corr_value:.2f}")
    if corr_value >= 0.7:
        st.success("Strong Positive Correlation")
    elif corr_value >= 0.4:
        st.info("Moderate Positive Correlation")
    elif corr_value >= 0:
        st.warning("Weak Positive Correlation")
    elif corr_value <= -0.7:
        st.success("Strong Negative Correlation")
    elif corr_value <= -0.4:
        st.info("Moderate Negative Correlation")
    else:
        st.warning("Weak Negative Correlation")
    if mapcol1dis == mapcol2dis:
        st.info("Please select two different metrics to view the scatter plot.")
    else:
        st.plotly_chart(metriccorr(bowl, mapcol1dis, mapcol2dis),use_container_width=True)
    
    
    st.subheader('Heatmaps')
    mapchoose = st.radio('Choose Heatmaps',['Bowling Heatmap','Batting Heatmap'], key = 'ch1')
    if mapchoose == 'Bowling Heatmap':
        st.plotly_chart(corrheatmap(bowl))
    if mapchoose == 'Batting Heatmap':
        st.plotly_chart(corrheatmap(data))

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
    st.plotly_chart(Top_Scorers(data),key = 'c5')

if options == "Most Fours":
    st.plotly_chart(Most_4s(data), key = 'c6')

if options == "Most Sixes":
    st.plotly_chart(Most_6s(data), key = 'c7')    

if options == "Strike Rate":
    st.plotly_chart(Most_sr(data), key = 'c8')

if options == "Batting Average":
    st.plotly_chart(Best_avg(data), key = 'c9')

if options == "Most Wickets":
    st.plotly_chart(Most_wkts(bowl), key = 'c10')

if options == "Bowling Average":
    st.plotly_chart(Best_bowl_avg(bowl), key = 'c11')

if options == "Economy Rate":
    st.plotly_chart(Best_Econ(bowl), key = 'c12')

if options == "Bowling Strike Rate":
    st.plotly_chart(Best_bowl_sr(bowl), key = 'c13')

if options == "Correlation Heatmap":
    st.plotly_chart(corrheatmap(bowl), key = 'c14')

if options == "Strike Rate VS Average":
    st.plotly_chart(sr_vs_avg(bowl), key = 'c15')

if options == "Most 4 wicket Haul":
    st.plotly_chart(Most_4wkts(bowl), key = 'c16')

if options == "Most 5 wicket Haul":
    st.plotly_chart(Most_5wkts(bowl), key = 'c17')
 
st.subheader("Datasets")
datasets = st.sidebar.selectbox("Datasets", ["Batsman data","bowlers data"])

if datasets == "Batsman data":
    st.subheader("Batsman data")
    st.dataframe(data)

if datasets == "bowlers data":
    st.subheader("Bowlers data")
    st.dataframe(bowl)

