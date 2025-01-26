
import streamlit as st
import plotly.express as px 
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

st.set_page_config(
    layout="wide",
    page_title = 'Life Expectancy Analysis',
    page_icon= '📊'
)

st.markdown("""
    <style>
        body {
            background-color: #f6f6f6 !important;
        }
        .stApp {
            background-color: #f6f6f6 !important; 
        }

        .title {
            background-color: #ffffff; 
            color: #616f89;             
            padding: 20px;
            text-align: center;
            font-size: 46px;
            font-weight: bold;
            border: 4px solid #000083; 
            border-radius: 10px;       
            box-shadow: 0px 10px 20px rgba(0, 0, 0, 0.2); 
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);  
        
        }

        .metric {
            background-color: white;
            border: 2px solid #000083;  
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0px 10px 15px rgba(0, 0, 0, 0.1);
            text-align: center;
        }

        .metric p {
            color: #000083;
            font-size: 28px;
            font-style: italic;
            text-shadow: 1px 1px 2px #000083;
           
        }

        .metric h3 {
            margin-bottom: 10px;
            font-size: 20px;
            font-weight: bold;
            color: #999999;
        
        }
    </style>
""", unsafe_allow_html=True)



df = pd.read_csv('data\Life Expectancy CleanedUpdated.csv')
# Use the new data after cleaning and preprocessing, we wrote it to a.csv file in our analysis notebook
df_developed= df[df['Status']=='Developed'].groupby(['Status']).mean()   # get the statistics for each status to display on dashboard
df_developing= df[df['Status']=='Developing'].groupby(['Status']).mean()

## side bar 
x = st.sidebar.checkbox('Show Data', False, key=1)
status = st.sidebar.selectbox("Select Status", np.append(df['Status'].unique(),'All'))

# show data if button is chosen                              
if x:
                                     
    st.header('DataSet Sample')
    st.dataframe(df.sample(100))

# Create columns for layout
col1, col2, col3 = st.columns([2,2,8])
# depending on choice
if status=='Developed':
    
    with col1:
        st.markdown(f'''
            <div class="metric">
                <h3>Average Life Expectancy</h3>
                <p>{df_developed['Life expectancy'][0]}</p>
            </div>
        ''', unsafe_allow_html=True)
        st.write(" ")
        st.markdown(f'''
            <div class="metric">
                <h3>Average Adult Mortality</h3>
                <p>{df_developed['Adult Mortality'][0]}</p>
            </div>
        ''', unsafe_allow_html=True)
        st.write(" ")
        st.markdown(f'''
        <div class="metric">
            <h3>Average Schooling Years</h3>
            <p>{df_developed['Schooling'][0]}</p>
        </div>
    ''', unsafe_allow_html=True)


    with col2:
        st.markdown(f'''
            <div class="metric">
                <h3>Average Population</h3>
                <p>{df_developed['Population'][0]}</p>
            </div>
        ''', unsafe_allow_html=True)

        st.write(" ")

        st.markdown(f'''
            <div class="metric">
                <h3>Avg BMI</h3>
                <p>{df_developed['BMI'][0]}</p>
            </div>
        ''', unsafe_allow_html=True)
        
        st.write(" ")
        
        st.markdown(f''' 
            <div class="metric">
                <h3>Average GDP</h3>
                <p>{df_developed['GDP'][0]}</p>
            </div>
        ''', unsafe_allow_html=True)


     

    with col3:
    
        developed_df= df[df['Status']=='Developed']
        developed_years= developed_df.groupby(['Year'])['Life expectancy'].mean().sort_values(ascending=True).reset_index()
        fig = px.line(developed_years, x="Year", y="Life expectancy", title='Life expectancy in Developed countries over the years', markers=True)
        st.plotly_chart(fig,use_container_width=True)
   
           

    
elif status== 'Developing':
        
    with col1:
        st.markdown(f'''
            <div class="metric">
                <h3>Average Life Expectancy</h3>
                <p>{df_developing['Life expectancy'][0]}</p>
            </div>
        ''', unsafe_allow_html=True)
        st.write(" ")
        st.markdown(f'''
            <div class="metric">
                <h3>Average Adult Mortality</h3>
                <p>{df_developing['Adult Mortality'][0]}</p>
            </div>
        ''', unsafe_allow_html=True)
        st.write(" ")
        
        st.markdown(f'''
            <div class="metric">
                <h3>Average GDP</h3>
                <p>{df_developing['GDP'][0]}</p>
            </div>
        ''', unsafe_allow_html=True)



    with col2:
        st.markdown(f'''
            <div class="metric">
                <h3>Average Population</h3>
                <p>{df_developing['Population'][0]}</p>
            </div>
        ''', unsafe_allow_html=True)

        st.write(" ")

        st.markdown(f'''
            <div class="metric">
                <h3>Avg BMI</h3>
                <p>{df_developing['BMI'][0]}</p>
            </div>
        ''', unsafe_allow_html=True)
        
        st.write(" ")

        st.markdown(f'''
            <div class="metric">
                <h3>Average Schooling Years</h3>
                <p>{df_developing['Schooling'][0]}</p>
            </div>
        ''', unsafe_allow_html=True)


    with col3:
        developing_df= df[df['Status']=='Developing']
        developing_years= developing_df.groupby(['Year'])['Life expectancy'].mean().sort_values(ascending=True).reset_index()
        fig = px.line(developing_years, x="Year", y="Life expectancy", title='Life expectancy in Developing countries over the years', markers=True)
        st.plotly_chart(fig,use_container_width=True)
   




else:
    
    with col1:
        
        st.markdown(f'''
            <div class="metric">
                <h3>Average Life Expectancy</h3>
                <p>{df['Life expectancy'].mean()}</p>
            </div>
        ''', unsafe_allow_html=True)
        st.write(" ")
        st.markdown(f'''
            <div class="metric">
                <h3>Average Adult Mortality</h3>
                <p>{df['Adult Mortality'].mean()}</p>
            </div>
        ''', unsafe_allow_html=True)
        st.write(" ")
        
        st.markdown(f'''
            <div class="metric">
                <h3>Average GDP</h3>
                <p>{df['GDP'].mean()}</p>
            </div>
        ''', unsafe_allow_html=True)



    with col2:
        st.markdown(f'''
            <div class="metric">
                <h3>Average Population</h3>
                <p>{df['Population'].mean()}</p>
            </div>
        ''', unsafe_allow_html=True)

        st.write(" ")

        st.markdown(f'''
            <div class="metric">
                <h3>Avg BMI</h3>
                <p>{df['BMI'].mean()}</p>
            </div>
        ''', unsafe_allow_html=True)
        
        st.write(" ")

        st.markdown(f'''
            <div class="metric">
                <h3>Average Schooling Years</h3>
                <p>{df['Schooling'].mean()}</p>
            </div>
        ''', unsafe_allow_html=True)



    with col3:
        fig = plt.figure(figsize=(16,11))
        sns.lineplot(df, x='Year', y= 'Life expectancy', markers=True)
        plt.title('Average Life expectancy throughout the years')
        st.pyplot(fig)

       
     
