import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.header("Dashboard Bike Sharing")

st.subheader("""
    Ini adalah Dashboard untuk melihat:
            1. Korelasi antara cuaca dengan banyaknya user bike sharing
        2. Trend Penyewaan Sepeda setiap harinya
    """)

# Load dataset
day_df = pd.read_csv('day.csv')

# Function to map weather
def map_weather(x):
    if x == 1:
        return "1"
    elif x == 2:
        return "2"
    elif x == 3:
        return "3"
    elif x == 4:
        return "4"

# Processing data for weather correlation
rent_weather_cor_df = pd.DataFrame(day_df[['weathersit', 'cnt']])
rent_weather_cor_df['weather'] = rent_weather_cor_df['weathersit'].apply(map_weather)
result_weather = rent_weather_cor_df.groupby(by="weather")['cnt'].nunique().sort_values(ascending=False)

# Plotting with Streamlit
st.subheader('Weather Correlation with Rental Count')

# Display result
st.write("Unique rental counts by weather:")
st.write(result_weather)

# Plotting the bar chart
st.bar_chart(result_weather)
with st.expander("See explanation"):
    st.write(
        """
        - 1: Clear, Few clouds, Partly cloudy, Partly cloudy\n
- 2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist\n
- 3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds\n
- 4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog
        """
    )

##########################################################

# Function to map weekday to day names
def map_weather(x):
    days = {0: 'Sunday', 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday'}
    return days.get(x, 'Unknown')

# Apply the mapping function
day_df['day'] = day_df['weekday'].apply(map_weather)

# Group by day and calculate the sum of casual, registered, and total count
grouped_df = day_df.groupby('day').agg({'casual': 'sum', 'registered': 'sum', 'cnt': 'sum'}).reset_index()

# Create a Streamlit title
st.subheader('Bicycle rental trends every day')

# Display data table
st.write(grouped_df)

# Plotting with Streamlit
fig, ax = plt.subplots(1, 3, figsize=(20, 8))

# Plot Casual by Day
ax[0].bar(grouped_df['day'], grouped_df['casual'])
ax[0].set_title('Casual by Day')
ax[0].tick_params(axis='x', rotation=45)

# Plot Registered by Day
ax[1].bar(grouped_df['day'], grouped_df['registered'])
ax[1].set_title('Registered by Day')
ax[1].tick_params(axis='x', rotation=45)

# Plot Total Count by Day
ax[2].bar(grouped_df['day'], grouped_df['cnt'])
ax[2].set_title('All by Day')
ax[2].tick_params(axis='x', rotation=45)

# Show the plot in the Streamlit app
st.pyplot(fig)