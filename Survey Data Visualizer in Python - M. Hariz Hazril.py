# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 10:42:28 2024

@author: hariz
"""

import pandas as pd
import matplotlib.pyplot as plt

def parse_survey_data(file_path):
    # Read the CSV file
    df = pd.read_csv(file_path)
    
    # Print the first few rows of the dataframe
    print("Survey Data:")
    print(df.head())
    
    return df

def plot_pie_chart(data, column_name):
    # Count the frequency of each response
    response_counts = data[column_name].value_counts()
    
    # Plot pie chart
    plt.figure(figsize=(8, 8))
    plt.pie(response_counts, labels=response_counts.index, autopct='%1.1f%%', startangle=140)
    plt.title(f'Responses for {column_name}')
    plt.show()

def main():
    file_path = 'C:/Users/hariz/Downloads/2024 Class Survey.csv'  # Path to your CSV file
    survey_data = parse_survey_data(file_path)
    
    # Loop through each column to create a pie chart
    for column in survey_data.columns:
        plot_pie_chart(survey_data, column)

if __name__ == "__main__":
    main()
