# Social-Media-User-Performance-and-Dashboards

# Overview
In this project, I analyzed the Social Media User Performance dataset, extracted key insights, and created different types of charts. In the last business, Gorth created an interactive dashboard.

# Objectives
Identify which platform is being used the most? Define how much Average time is spent on each platform? Platform Popularity. Finding Insight for business help. Dataset Sources and Structure source of the dataset The dataset has been taken from Kaggle Data Link : https://www.kaggle.com/datasets/umeradnaan/daily-social-media-active-users
Dataset File Type: CSV Structure of the dataset The dataset has 10,000 rows and 7 columns.

# Columns Information :
Platform: The social media platform (e.g., Facebook, Instagram, TikTok) Owner: The company or entity that owns the platform (e.g., Meta, Google, ByteDance) Primary Usage: Describes the platform’s main functionality (e.g., social networking, video sharing) Country: The user’s location, simulated from a global range Daily Time Spent (min): The amount of time (in minutes) the user spends daily on the platform Verified Account: Indicates whether the user has a verified account Date Joined: The simulated date the user joined the platform
Data Cleaning
It is very important for data analysis that the data set is clean, one of the steps to clean the data set is to clean the data. For example, removing missing values ​​or filling the data set, removing duplicate values, removing or identifying outliers. If the data set is not clean, then many problems will be faced in the analysis or building machine learning models. Therefore, cleaning the data set is one of the most important steps in data analysis or creating dashboards or building machine learning models. Missing Values Handling After checking for missing values ​​in the dataset, there are no missing values ​​in the dataset.

# Data Preprocessing
Data preprocessing is a crucial step in any data analysis project, as it prepares raw data for accurate and reliable analysis. Outlier Remove: The Dataset doesn't have any outliers
Change datatype: "Data Joined" columns datatype is object, convert this datatype to pandas datetime

# Analysis & Visualization

1. Which platform is being used the most? (Analysis)  

    Which platform is being used the most? - showing by pie chart (Visualization) 

    Observation of this analysis: Reddit Platform used most , used number = 764



2. How much Average time is spent on each platform (Analysis)  

    How much Average time is spent on each platform? - showing by linechart (Visualization) 

    Observation of this analysis: Most Average spent Platform is Facebook : 157.95




3. Which platform is more popular in which country? (Analysis)  

     Which platform is more popular in which country? - showing by choropleth chart (Visualization) 

     Observation of this analysis: WeChat Platform used most Afghanistan country , Daily Time Spent (min) : 1207.94




4. Number and percentage of verified accounts (Analysis)  

    Number and percentage of verified accounts? -showing by donut chart (Visualization) 




5. In which year/month were the most accounts opened? (Analysis)  

    In which year/month were the most accounts opened?-showing by linchart (Visualization) 

   Observation of this analysis: Oct 2024 were the most accounts opened : 105 Account




6. If there are multiple owners, who uses the platform the most? (Analysis)  

    If there are multiple owners, who uses the platform the most?- showing by barchart (Visualization) 

Observation of this analysis: Meta Owner Platform usage tha most - daliy time spent : 400000+




7. Whether any platform is doing particularly well/worse by country. (Analysis)  

   Whether any platform is doing particularly well/worse by country. - showing by boxplot (Visualization) 

Observation of this analysis: Youtube Platform , Country Panama , Daily Time Spent (min) - 299.31 , Youtube platform is doing well






8. How does time spent change as the account ages? (Analysis)  

   How does time spent change as the account ages?-showing by tabel (Visualization) 
# Social Media User Performance Dashboards
Developed an interactive dashboard using Python (Streamlit, Pandas, Plotly). The Dashboard provides actionable insight and shows businesses' performance in different types of visualizations. You can see your business growth by filtering.

# Key Features:
Filter KPI's Time Series Analysis Insight Visulaization
🛠 Tools & Technologies
Python — Data Processing & Analysis
Streamlit — Interactive dashboard
Pandas — Data Handling
Plotly , Scaborn, Matplotlib — Data Visualization
CSV — Export & Download Feature

Check my portfolio - https://meharinhasnapuspo.me
