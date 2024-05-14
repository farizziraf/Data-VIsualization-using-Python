import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import plotly.express as px
import streamlit as st
import translators as ts
import pyttsx3
import time
import os

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

#Connect to kubela.id server
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.bar_chart(chart_data)

conn = st.connection("mydb", type="sql", autocommit=True)

df = conn.query('SELECT EnglishPromotionName, StartDate, EndDate, MaxQty from dimpromotion limit 10;', ttl=600)

st.table(df)

# Initialize the pyttsx3 engine
engine = pyttsx3.init()

# Function to perform text-to-speech and translation
def perform_tts_and_translation(text, target_language):
    # Text-to-speech
    engine.say(text)
    engine.runAndWait()
    time.sleep(2)
    
    # Translation
    st.write("Terjemahan dalam bahasa target:")
    hasil = ts.translate(text, to_language=target_language, translator='google')
    st.write(hasil)
    
    # Text-to-speech for translated text
    engine.say(hasil)
    engine.runAndWait()

# Main Streamlit app
def main():
    st.title("Text-to-Speech and Translation App")
    
    # Input text
    text = st.text_area("Masukkan teks yang ingin diucapkan dan diterjemahkan", 
                        "This company was founded in 2010 by the infamous movie star, Graeme Alexander. Currently, the company worths USD 1 billion according to Forbes report in 2023. What an achievement in just 13 years.")
    
    # Target language selection
    target_language = st.selectbox("Pilih bahasa target untuk menerjemahkan", 
                                   ["id", "fr", "es", "zh-CN"])
    
    # Button to perform TTS and translation
    if st.button("Proses"):
        perform_tts_and_translation(text, target_language)

# Run the app
if __name__ == "__main__":
    main()