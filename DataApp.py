import pandas as pd
import numpy as np
import matplotlib.pyplot
import streamlit as st
import plotly.express as px
import seaborn as sns

st.title("My First Data Dashboarding App in Streamlit GapMinder Dataset 2007")
data = px.data.gapminder()
data.head()
st.dataframe(data.head())
# scatter map in plotly
option = st.sidebar.selectbox("Select a Continent", data["continent"].unique())
st.write("You've selected", option)

#Sunburst based on selections in the Select Box

if option == "Asia":
    fig3= px.scatter(data.query("year==2007" and "continent=='Asia'"), x="gdpPercap", y="lifeExp",
                     color="continent", size="pop", size_max=60,
                     log_x=True,hover_name="country", title="Scatter Plot")
    fig1 = px.sunburst(data.query("continent=='Asia'"), path=["continent", "country"],
                      color="lifeExp", values="pop", hover_name="country",
                      hover_data=["continent", "lifeExp", "pop"]
                      )
    fig2 = px.treemap(data.query("continent=='Asia'"), path=[px.Constant("World"), "continent", "country"],
                     values="pop", color="pop",
                     hover_name="country", hover_data=["pop"])
    st.plotly_chart(fig3)
    st.plotly_chart(fig1)
    st.plotly_chart(fig2)
elif option=="Africa":
    fig3 = px.scatter(data.query("year==2007" and "continent=='Africa'"), x="gdpPercap", y="lifeExp",
                      color="continent", size="pop", size_max=60,
                      log_x=True,hover_name="country", title="Scatter Plot")
    fig = px.sunburst(data.query("continent=='Africa'"), path=["continent", "country"],
                      color="lifeExp", values="pop", hover_name="country",
                      hover_data=["continent", "lifeExp", "pop"]
                      )
    fig2 = px.treemap(data.query("continent=='Africa'"), path=[px.Constant("World"), "continent", "country"],
                      values="gdpPercap", color="pop",
                      hover_name="country", hover_data=["gdpPercap", "pop"])
    st.plotly_chart(fig3)
    st.plotly_chart(fig)
    st.plotly_chart(fig2)
elif option=="Oceania":
    fig3 = px.scatter(data.query("year==2007" and "continent=='Oceania'"), x="gdpPercap", y="lifeExp",
                      color="continent", size="pop", size_max=60,
                      log_x=True,hover_name="country", title="Scatter Plot")
    fig = px.sunburst(data.query("continent=='Oceania'"), path=["continent", "country"],
                      color="lifeExp", values="pop", hover_name="country",
                      hover_data=["continent", "lifeExp", "pop"]

                      )
    fig2 = px.treemap(data.query("continent=='Oceania'"), path=[px.Constant("World"), "continent", "country"],
                      values="gdpPercap", color="pop",
                      hover_name="country", hover_data=["gdpPercap", "pop"])
    st.plotly_chart(fig3)
    st.plotly_chart(fig)
    st.plotly_chart(fig2)
elif option=="Europe":
    fig3 = px.scatter(data.query("year==2007" and "continent=='Europe'"), x="gdpPercap", y="lifeExp",
                      color="country", size="pop", size_max=100,
                       log_x=True,hover_name="country", title="Scatter Plot")
    fig = px.sunburst(data.query("continent=='Europe'"), path=["continent", "country"],
                      color="lifeExp", values="pop", hover_name="country",
                      hover_data=["continent", "lifeExp", "pop"]
                      )
    fig2 = px.treemap(data.query("continent=='Europe'"), path=[px.Constant("World"), "continent", "country"],
                      values="gdpPercap", color="pop",
                      hover_name="country", hover_data=["gdpPercap", "pop"])
    st.plotly_chart(fig3)
    st.plotly_chart(fig)
    st.plotly_chart(fig2)
elif option=="Americas":
    fig3 = px.scatter(data.query("year==2007" and "continent=='Americas'"), x="gdpPercap", y="lifeExp",
                      color="country", size="pop", size_max=100,
                       log_x=True, hover_name="country",title="Scatter Plot")
    fig = px.sunburst(data.query("continent=='Americas'"), path=["continent", "country"],
                      color="lifeExp", values="pop", hover_name="country",
                      hover_data=["continent", "lifeExp", "pop"]
                      )
    fig2 = px.treemap(data.query("continent=='Americas'"), path=[px.Constant("World"), "continent", "country"],
                      values="gdpPercap", color="pop",
                      hover_name="country", hover_data=["gdpPercap", "pop"])
    st.plotly_chart(fig3)
    st.plotly_chart(fig)
    st.plotly_chart(fig2)
else:
    st.write("Select a Continent")
