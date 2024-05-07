import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load the data
data = pd.read_csv("dataset/tips.csv")
st.write("Data Visualization using tips.csv Dataset")
st.write("By Fariz - 21082010156")

# Scatter Plot with Matplotlib
st.write("Scatter Plot")
fig, ax = plt.subplots()
scatter_plot = ax.scatter(data['day'], data['tip'], c=data['size'], s=data['total_bill'])
plt.xlabel('Day')
plt.ylabel('Tip')
plt.colorbar(scatter_plot, label='Size')
st.pyplot(fig)

# Bar Chart with Matplotlib
st.write("Bar Chart")
fig, ax = plt.subplots()
bar_chart = ax.bar(data['day'], data['tip'])
st.pyplot(fig)

# Histogram with Matplotlib
st.write("Histogram")
fig, ax = plt.subplots()
histogram = ax.hist(data['total_bill'])
st.pyplot(fig)

# Line Plot with Seaborn
st.write("Line Plot")
fig, ax = plt.subplots(figsize=(10, 6))
line_plot = sns.lineplot(data=data.drop(['total_bill'], axis=1), ax=ax)
st.pyplot(fig)

# Bar Plot with Seaborn
st.write("Bar Plot")
fig, ax = plt.subplots(figsize=(10, 6))
bar_plot = sns.barplot(x='day', y='tip', data=data, hue='sex', ax=ax)
st.pyplot(fig)

# Visualization with Interaction with Plotly
st.write("Line Chart with Interaction")
fig = px.line(data, y='tip')
st.plotly_chart(fig)