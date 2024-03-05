import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

#import dataset
day_df = pd.read_csv('day.csv')

st.write(
    """
    # Dashboard Bike Rent
    """
)

# Load dataset
day_df = pd.read_csv('day.csv')

# Function to map weekday to day names
def map_weather(x):
    days = {0: 'Sunday', 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday'}
    return days.get(x, 'Unknown')

# Apply the mapping function
day_df['day'] = day_df['weekday'].apply(map_weather)

# Group by day and calculate the sum of casual, registered, and total count
grouped_df = day_df.groupby('day').agg({'casual': 'sum', 'registered': 'sum', 'cnt': 'sum'}).reset_index()

# Create a Streamlit title
st.title('Dashboard Bike Rent')

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