# import libery
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import warnings
warnings.filterwarnings('ignore')

# set the page confiygure , page title , page icon , layout
st.set_page_config(page_title="Social Media Performance" , page_icon='🌐',layout='wide')


# uplode data
df = pd.read_csv ('preprocessing_data.csv', parse_dates=['Date Joined'])


# set  title
st.title("💬 Social Media Performance")
st.markdown("<style>div.block-container{padding-top:3rem;}</style>" , unsafe_allow_html=True)

# getting min max Date Joined
col1 , col2 = st.columns((2))
df['Date Joined'] = pd.to_datetime(df['Date Joined'])
start_date = pd.to_datetime(df['Date Joined'].min())
end_date = pd.to_datetime(df['Date Joined'].max())
with col1 : 
    date1 = st.date_input("Start Date", start_date, min_value=start_date, max_value=end_date)
with col2 :
    date2 = st.date_input("End Date", end_date, min_value=start_date, max_value=end_date)
date1 = pd.to_datetime(date1)
date2 = pd.to_datetime(date2)
df = df[(df["Date Joined"] >= date1) & (df['Date Joined'] <= date2)].copy()

# KPI Card
c1 , c2, c3,c4 = st.columns((4))
total_users = len(df)
with c1:
    st.metric("Total Users", total_users)


verified_count = df[df["Verified Account"] == "Yes"].shape[0]
with c2:
    st.metric("Verified Users", verified_count)

avg_time = df["Daily Time Spent (min)"].mean()
with c3:
    st.metric("Average Daily Time Spent (min)", f"{avg_time:.2f}")
with c4:
    most_popular = df["Platform"].value_counts().idxmax()
    user_count = df["Platform"].value_counts().max()
    st.metric("Most Popular Platform", f"{most_popular} ({user_count})")



# Donut Chart
color = {
    "Yes" : "#EA738D",
    "No"  : " #F7C5CC"
}
country_verified = df.groupby(["Country", "Verified Account"]).size().reset_index(name="Count")
fig = px.bar(
    country_verified,
    x="Country",
    y="Count",
    color="Verified Account",
    barmode="stack",  color_discrete_map=color)
fig.update_layout(xaxis=dict(title=dict(text="Country", font=dict(color="black")),tickfont=dict(color="black")  ),
        yaxis=dict(title=dict(text="Number of Users", font=dict(color="black")),  tickfont=dict(color="black")),width=1000,height=600)
st.markdown(
    "<h4 style='text-align: center; color: black;'>Verified vs Unverified Users by Country</h4>",
    unsafe_allow_html=True)
# Show in Streamlit
st.plotly_chart(fig, use_container_width=True)


col1 , col2 , col3 = st.columns((3))
social_media_colors = {
    "Reddit": "#FFB6C1",
    "Instagram": "#C48F98",
    "WeChat": "#FF69B4",
    "Threads": "#EE6DB2",
    "TikTok": "#DB7093",
    "LinkedIn": "#D358A6",
    "YouTube": "#DA70D6",
    "Facebook": "#D8BFD8",
    "X (formerly Twitter)": "#EC8FEC",
    "Pinterest": "#EE82EE",
    "Snapchat": "#FFF0F5",
    "Telegram": "#FFE4E1",
    "Quora": "#DDA0DD",
    "WhatsApp": "#F0A7CB"
}

with col1:
    df['YearMonth'] = df['Date Joined'].dt.to_period('M').astype(str)   
    growth = df.groupby(['YearMonth', 'Platform']).size().reset_index(name='New Users')
    total_growth = growth.groupby('Platform')['New Users'].sum().reset_index()
    fig = px.pie(
        total_growth,
        values='New Users',
        names='Platform',
        title="Platform-wise User Growth Distribution",color="Platform",
        hole=0.5,color_discrete_map=social_media_colors )
    fig.update_layout(
        legend=dict(title=dict(font=dict(color="black")), font=dict(color="black")),
        title=dict(font=dict(color="black")),
        width=800,
        height=500)
    st.plotly_chart(fig)

with col2:
    platform_count = df["Platform"].value_counts().reset_index()
    platform_count.columns = ["Platform", "User Count"]
    fig1 = px.bar(
    platform_count,
    x="Platform",
    y="User Count",
    text="User Count",
    title="Platform-wise User Count",
    color="Platform",color_discrete_map=social_media_colors)
    fig1.update_layout(xaxis=dict(title=dict(font=dict(color="black")),tickfont=dict(color="black")  ),
        yaxis=dict(title=dict(font=dict(color="black")),  tickfont=dict(color="black")),legend=dict(title=dict(font=dict(color="black")), font=dict(color="black")),
        title=dict(font=dict(color="black")),width=1000,height=500)
    fig1.update_traces( textfont=dict(color="black"))

with col2:
    platform_count = df["Platform"].value_counts().reset_index()
    platform_count.columns = ["Platform", "User Count"]
    fig1 = px.bar(
    platform_count,
        x="Platform",
        y="User Count",
        text="User Count",
        title="Platform-wise User Count",
        color="Platform",color_discrete_map=social_media_colors)
    fig1.update_layout(xaxis=dict(title=dict(font=dict(color="black")),tickfont=dict(color="black")  ),
            yaxis=dict(title=dict(font=dict(color="black")),  tickfont=dict(color="black")),legend=dict(title=dict(font=dict(color="black")), font=dict(color="black")),
            title=dict(font=dict(color="black")),width=1000,height=550)
    fig1.update_traces(textposition="outside", textfont=dict(color="black"))
    st.plotly_chart(fig1, use_container_width=True)


with col3:
    fig = px.histogram(
    df,
    x="Daily Time Spent (min)",
    nbins=20,          
    title="Distribution of Daily Time Spent",
    labels={"Daily Time Spent (min)": "Daily Time (minutes)"}, 
    color_discrete_sequence=["skyblue"])
    fig.update_layout(
    xaxis_title="Daily Time Spent (minutes)",
    yaxis_title="Number of Users",
    template="plotly_white")
    fig.update_layout(xaxis=dict(title=dict(font=dict(color="black")),tickfont=dict(color="black")  ),
        yaxis=dict(title=dict(font=dict(color="black")),  tickfont=dict(color="black")),legend=dict(title=dict(font=dict(color="black")), font=dict(color="black")),
        title=dict(font=dict(color="black")),width=1000,height=500)
    st.plotly_chart(fig, use_container_width=True)


platform_country = df.groupby(['Country', 'Platform']).size().reset_index(name='UserCount')
top_platform_country = platform_country.loc[platform_country.groupby('Country')['UserCount'].idxmax()]
fig = px.choropleth(
    top_platform_country,
    locations='Country',
    locationmode='country names',  
    color='Platform',               
    hover_name='Country',
    hover_data=['Platform', 'UserCount'],
    title='Most Popular Platform by Country')
fig.update_layout(xaxis=dict(title=dict(font=dict(color="black")),tickfont=dict(color="black")  ),
        yaxis=dict(title=dict(font=dict(color="black")),  tickfont=dict(color="black")),legend=dict(title=dict(font=dict(color="black")), font=dict(color="black")),
        title=dict(font=dict(color="black")),width=1000,height=500)

st.plotly_chart(fig)

# Convert to datetime
df["Date Joined"] = pd.to_datetime(df["Date Joined"], errors="coerce")
# Create Year-Month
df["YearMonth"] = df["Date Joined"].dt.to_period("M")

col1 ,  col2 = st.columns((2))
with col1:
    # Group by YearMonth
    monthly_growth = df.groupby("YearMonth").size().reset_index(name="New Users")
    # Convert YearMonth to string for plotting
    monthly_growth["YearMonth"] = monthly_growth["YearMonth"].astype(str)
    # Create line chart
    fig_month = px.line(monthly_growth, 
                        x="YearMonth", 
                        y="New Users")
    fig_month.update_traces(line=dict(color="#9b45eb"))
    st.markdown("""<h4 style='text-align: center;'>Monthly New Users Trend</h4>""",
    unsafe_allow_html=True)
    fig_month.update_layout(
        xaxis=dict(title=dict(font=dict(color="black")), tickfont=dict(color="black")),
        yaxis=dict(title=dict(font=dict(color="black")), tickfont=dict(color="black")),
        legend=dict(title=dict(font=dict(color="black")), font=dict(color="black")),
        title=dict(font=dict(color="black")),
        width=1000,
        height=500
    )

    st.plotly_chart(fig_month, use_container_width=True)

with col2:
    # Count platforms by owner
    owner_counts = df.groupby("Owner")["Platform"].count().reset_index()
    owner_counts = owner_counts.rename(columns={"Platform": "Total Platforms"})
    # Bar Chart
    fig = px.bar(
        owner_counts,
        x="Owner",
        y="Total Platforms",
        color="Owner",
        title="Number of Platforms by Owner",
        text="Total Platforms"
    )
    fig.update_layout(
        xaxis=dict(title=dict(font=dict(color="black")), tickfont=dict(color="black")),
        yaxis=dict(title=dict(font=dict(color="black")), tickfont=dict(color="black")),
        legend=dict(title=dict(font=dict(color="black")), font=dict(color="black")),
        title=dict(font=dict(color="black")),
        width=1000,
        height=500
    )
    st.subheader("Number of Platforms by Owner")
    st.plotly_chart(fig, use_container_width=True)
