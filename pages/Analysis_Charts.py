import streamlit as st
import plotly.express as px 
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

st.cache_resource.clear()
st.markdown(
    """
    <style>
    .stTabs [role="tablist"] {
        border-bottom: 2px solid #e0e0e0;
        padding-bottom: 8px;
    }

    </style>
    """,unsafe_allow_html=True)





df = pd.read_csv('data/Life Expectancy CleanedUpdated.csv')
df.drop("Unnamed: 0", axis=1, inplace=True)


tab1,tab2,tab3,tab4,tab5,tab6=st.tabs(['Status Analysis','Top and Bottom Countries',' Relationships1','Population vs life expectancy','Alcohol vs Life expectancy','Scatterplots'])
# select which feature to compare
with tab1:
    comp = st.sidebar.selectbox("Select Feature to Compare", ['Life expectancy', 'Adult Mortality',
       'infant deaths', 'Alcohol', 'Hepatitis B',
       'Measles', 'BMI', 'Polio', 'Total expenditure',
       'Diphtheria', 'HIV/AIDS', 'thinness  1-19 years','Schooling'])
    with st.container():
        if comp== 'Life expectancy':
            grouped_status =df.groupby(["Status"])["Life expectancy"].mean().sort_values(ascending=True).reset_index()
            fig = px.bar(grouped_status, x='Status', y='Life expectancy', color_discrete_sequence=px.colors.qualitative.D3, title= 'Life Expectancy According to Country Status')
            st.plotly_chart(fig,use_container_width=True)
        elif comp== 'Adult Mortality':
            mort =df.groupby(["Status"])["Adult Mortality"].mean().sort_values(ascending=True).reset_index()
            fig = px.bar(mort, x='Status', y='Adult Mortality', color= 'Status', color_continuous_scale=px.colors.sequential.GnBu, title= 'Average Adult Mortality in pure litres According to Country Status')
            st.plotly_chart(fig,use_container_width=True)
        elif comp== 'infant deaths':
            infant =df.groupby(['Status'])["infant deaths"].mean().sort_values(ascending=False).reset_index()
            fig = px.bar(infant, x='Status', y='infant deaths', color='Status', color_continuous_scale=px.colors.sequential.GnBu, title= 'Average Infant Deaths according to status')
            st.plotly_chart(fig,use_container_width=True)
        elif comp== 'Alcohol':
            alc =df.groupby(["Status"])["Alcohol"].mean().sort_values(ascending=True).reset_index()
            fig = px.bar(alc, x='Status', y='Alcohol', color= 'Status', color_continuous_scale=px.colors.sequential.GnBu, title= 'Average Alcohol consumption in pure litres According to Country Status')
            st.plotly_chart(fig,use_container_width=True)
        elif comp== 'Hepatitis B':
            alc =df.groupby(["Status"])["Hepatitis B"].mean().sort_values(ascending=True).reset_index()
            fig = px.bar(alc, x='Status', y='Hepatitis B', color= 'Status', color_continuous_scale=px.colors.sequential.GnBu, title= 'Hepatitis B Immunization of infants according to status')
            st.plotly_chart(fig,use_container_width=True)
        elif comp== 'Measles':
            alc =df.groupby(["Status"])["Measles"].mean().sort_values(ascending=True).reset_index()
            fig = px.bar(alc, x='Status', y='Measles', color= 'Status', color_continuous_scale=px.colors.sequential.GnBu, title= 'Average Measles cases according to status')
            st.plotly_chart(fig,use_container_width=True)
        elif comp== 'BMI':
            grouped_measles =df.groupby(["Status"])["BMI"].mean().sort_values(ascending=True).reset_index()
            fig = px.bar(grouped_measles, x='Status', y='BMI', title= 'Average BMI According to Country Status')
            st.plotly_chart(fig,use_container_width=True)
        elif comp== 'Polio':
            polio= df.groupby(['Status'])["Polio"].mean().sort_values(ascending=False).reset_index()
            fig = px.bar(polio, x='Status', y='Polio', color='Status', color_continuous_scale=px.colors.sequential.GnBu, title= 'Polio Immunization of infants according to status')
            st.plotly_chart(fig,use_container_width=True)
        elif comp== 'Total expenditure':
            tot= df.groupby(['Status'])["Total expenditure"].mean().sort_values(ascending=False).reset_index()
            fig = px.bar(tot, x='Status', y='Total expenditure', color='Status', color_continuous_scale=px.colors.sequential.GnBu, title= 'Total government expenditure on health according to status')
            st.plotly_chart(fig,use_container_width=True)
        elif comp== 'Diphtheria':
            di= df.groupby(['Status'])["Diphtheria"].mean().sort_values(ascending=False).reset_index()
            fig = px.bar(di, x='Status', y='Diphtheria', color='Status', color_continuous_scale=px.colors.sequential.GnBu, title= 'Diphtheria Immunization of infants according to status')
            st.plotly_chart(fig,use_container_width=True)
        elif comp== 'thinness  1-19 years':
            fig = plt.figure(figsize=(16,11))
            sns.barplot(df, x='Status', y='thinness  1-19 years', hue='Status', width=8)
            plt.title('Thinness in children and adolescents according to Status')
            st.pyplot(fig)
        elif comp== 'Schooling':
            grouped_schooling =df.groupby(["Status"])["Schooling"].mean().sort_values(ascending=True).reset_index()
            fig = px.bar(grouped_schooling, x='Status', y='Schooling', color_discrete_sequence=px.colors.qualitative.G10, title= 'Average schooling years According to Country Status')
            st.plotly_chart(fig,use_container_width=True)
        elif comp== 'HIV/AIDS':
            HIV =df.groupby(['Status'])["HIV/AIDS", 'Life expectancy'].mean().sort_values(ascending=False, by= "HIV/AIDS").reset_index()
            fig = px.bar(HIV, x='HIV/AIDS', y='Life expectancy', color='Status', color_continuous_scale=px.colors.sequential.GnBu, title= 'HIV/AIDS and average life expectancy according to status')
            st.plotly_chart(fig,use_container_width=True)

with tab2:
    col1,col2,col3=st.columns([14,1,14])
    
    with col1:
        # Show highest 15 countries in life expectancy
        top15 =df.groupby(["Country"])["Life expectancy"].mean().sort_values(ascending=False).head(15).reset_index()
        fig = px.bar(top15, x='Country', y='Life expectancy', color='Life expectancy', color_continuous_scale=px.colors.sequential.GnBu, title= 'Top fifteen countries in life expectancy')
        st.plotly_chart(fig,use_container_width=True)
        #top ten countries in expenditure
        topexp= df.groupby(["Country","Status"])["Total expenditure"].mean().sort_values(ascending=False).head(10).reset_index()
        fig21 = px.bar(topexp , x='Country', y='Total expenditure', color= "Status", color_continuous_scale=px.colors.sequential.GnBu, title= 'Top Ten Countries in Total Expenditure and their Statuses')
        fig21.update_layout(xaxis_categoryorder = 'total descending')
        st.plotly_chart(fig21,use_container_width=True)
       
        
    with col3:
        # bottom 15 countries in life expectancy
        last15 =df.groupby(["Country"])["Life expectancy"].mean().sort_values(ascending=True).head(15).reset_index()
        fig = px.bar(last15 , x='Country', y='Life expectancy', color='Life expectancy', color_continuous_scale=px.colors.sequential.GnBu, title= 'Bottom fifteen countries in life expectancy')
        st.plotly_chart(fig,use_container_width=True)
        
        # see countries with most infant deaths
        least20=df.groupby(["Country",'Status'])["infant deaths"].mean().sort_values(ascending=False).head(20).reset_index()
        fig = px.pie(least20, values='infant deaths', names='Country', color='Status', color_discrete_sequence=px.colors.qualitative.D3, title='Top ten countries in infant deaths and their statuses')
        st.plotly_chart(fig,use_container_width=True)

with tab3:
    
    col1,col2,col3=st.columns([1,9,1])
    
    with col2:
        # see the immunization average and life expectancy of each of the top 5 countries
        top5 =df.groupby(["Country"]).mean().sort_values(ascending=False, by='Life expectancy').head(5).reset_index()["Life expectancy", 'Hepatitis B']
        fig = px.pie(top5, values='Hepatitis B', names='Country', color='Life expectancy', color_discrete_sequence=px.colors.qualitative.D3, title= 'Hepatitis B immunization and Life expectancy in the top 5 longest living countries')
        st.plotly_chart(fig,use_container_width=True)
        
        # relationship between HepB immunization and life expectancy
        hep=df.groupby(['Status','Hepatitis B'])["Life expectancy"].mean().sort_values(ascending=True).reset_index()
        fig=px.bar(hep, x='Hepatitis B', y='Life expectancy', color='Status', title='Hepatitis B immunization and life expectancy in developed anddeveloping countries')
        st.plotly_chart(fig,use_container_width=True)
        
        # schooling vs expectancy in developing and developed countries
        st.write("Schooling vs average life expectacy in developed and developing countries")
        fig = plt.figure(figsize=(50,50))
        sns.lineplot(data=df, x= "Schooling", y= "Life expectancy", hue= "Status", markers= True)
        plt.title("Schooling vs average life expectacy in developed and developing countries")
        st.pyplot(fig)        
       
        
with tab4:
    col1,col2,col3=st.columns([1,11,1])
    with col2:
        # relationship between population and life expectancy over the years
        st.write('Population vs life expectancy over the years')
        pop=df.groupby(["Year"])["Life expectancy", "Population"].mean().sort_values(ascending=True, by= "Life expectancy").reset_index()
        fig = make_subplots(specs=[[{"secondary_y": True}]])
        fig.add_trace(go.Scatter(x= pop["Year"], y= pop["Population"], name="Average Population"),secondary_y=False)

        fig.add_trace(go.Scatter( x=pop["Year"], y=pop["Life expectancy"], name="Average Life expectancy"),secondary_y=True,)
        fig.update_xaxes(title_text="Year")
        fig.update_yaxes(title_text="Population", secondary_y=False)
        fig.update_yaxes(title_text="Life Expectancy", secondary_y=True)
        st.plotly_chart(fig,use_container_width=True)
        
        # see the average expectancy and its relation to population
        fig= px.scatter(df, x='Population', y="Life expectancy",trendline="ols", title='Population vs Life expectancy')
        st.plotly_chart(fig,use_container_width=True)

with tab5:
    col1,col2,col3=st.columns([1,11,1])
    with col2:
        # seeing average life expectancy and alcohol consumption through the years
        st.write('Alcohol Consumption vs life expectancy over the years')
        alc=df.groupby(["Year"])["Life expectancy", "Alcohol"].mean().sort_values(ascending=True, by= "Life expectancy").reset_index()
        fig = make_subplots(specs=[[{"secondary_y": True}]])
        fig.add_trace(go.Scatter(x= alc["Year"], y= alc["Alcohol"], name="Average Alcohol consumption"),secondary_y=False)

        fig.add_trace(go.Scatter( x=alc["Year"], y=alc["Life expectancy"], name="Average Life expectancy"),secondary_y=True,)

        fig.update_xaxes(title_text="Year")
        fig.update_yaxes(title_text="Alcohol in pure litres ", secondary_y=False)
        fig.update_yaxes(title_text="Average Life Expectancy", secondary_y=True)
        st.plotly_chart(fig,use_container_width=True)
        
with tab6:
    col1,col2,col3=st.columns([1,13,1])
    
    with col2:
        fig25= px.scatter(df, x='Income composition of resources', y="Life expectancy",trendline="lowess", title='Income Utilization vs Life expectancy')
        st.plotly_chart(fig25,use_container_width=True)
        
        fig26= px.scatter(df, x='BMI', y="Life expectancy", trendline="ols", title='BMI vs Life Expectancy')
        st.plotly_chart(fig26,use_container_width=True)
      
        fig22= px.scatter(df, x='GDP', y="Life expectancy",trendline="ols", title='GDP vs Life expectancy')
        st.plotly_chart(fig22,use_container_width=True)



        
    
