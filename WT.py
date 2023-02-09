import streamlit as st
import pandas as pd
from plotly import graph_objs as go
  
st.title("well test derivatives Dashboard")
st.markdown("The dashboard will help a researcher to get to know \
more about the derivatives and it's interpretation")
st.sidebar.title("Select Visual Curves")

st.sidebar.markdown("Select the Curves/Plots accordingly:")
  
data = pd.read_csv(r"derivative.csv",sep=';')
  
chart_visual = st.sidebar.selectbox('Select Charts/Plot type', 
                                    ('Line Chart', 'Bubble Chart'))
  
st.sidebar.checkbox("Show derivatives", True, key = 1)
selected_status = st.sidebar.selectbox('Select type',
                                       options = ['drawdown finite action', 
                                                  'drawdon semi_log', 'changing wellbore storage', 'closed rectangular drainage'
                                                  'hydraulic fracturing'])
  
fig = go.Figure()
  
if chart_visual == 'Line Chart':
    if selected_status == 'drawdown finite action':
        fig.add_trace(go.Scatter(x = data.t1,y= data.tdP1,
                                 mode = 'lines',
                                 name = 'drawdown finite action'))
    if selected_status == 'drawdon semi_log':
        fig.add_trace(go.Scatter(x = data.t2, y = data.dP2,
                                 mode = 'lines', name = 'drawdon semi_log'))
    if selected_status == 'changing wellbore storage':
        fig.add_trace(go.Scatter(x = data.t3, y= data.tdP3,
                                 mode = 'lines',
                                 name = 'changing wellbore storage'))
    if selected_status == 'closed rectangular drainage': 
        fig.add_trace(go.Scatter(x=data.t4, y=data.tdP4,
                                 mode='lines',
                                 name="closed rectangular drainage"))
    if selected_status == 'hydraulic fracturing': 
        fig.add_trace(go.Scatter(x=data.t5, y=data.tdP5,
                                 mode='lines',
                                 name="hydraulic fracturing"))
  
elif chart_visual == 'Bubble Chart':
    if selected_status == 'drawdown finite action':
        fig.add_trace(go.Scatter(x = data.t1, y = data.tdP1,
                                 mode='markers',
                                 marker_size=[40, 60, 80, 60, 40, 50],
                                 name='drawdown finite action'))
          
    if selected_status == 'drawdon semi_log':
        fig.add_trace(go.Scatter(x = data.t2, y = data.dP2,
                                 mode='markers', 
                                 marker_size=[40, 60, 80, 60, 40, 50],
                                 name='drawdon semi_log'))
   
   
          
    if selected_status == 'changing wellbore storage':
        fig.add_trace(go.Scatter(x = data.t3, y= data.tdP3,
                                 mode='markers', 
                                 marker_size=[40, 60, 80, 60, 40, 50],
                                 name = 'changing wellbore storage'))
    if selected_status == 'closed rectangular drainage':
        fig.add_trace(go.Scatter(x=data.t4, y=data.tdP4,
                                 mode='markers',
                                 marker_size=[40, 60, 80, 60, 40, 50], 
                                 name="closed rectangular drainage"))
    if selected_status == 'hydraulic fracturing':

        
        fig.add_trace(go.Scatter(x=data.t5,y=data.tdP5,
                                 mode='markers', 
                                 marker_size=[40, 60, 80, 60, 40, 50],
                                 name='hydraulic fracturing'))


st.plotly_chart(fig, use_container_width=True)
