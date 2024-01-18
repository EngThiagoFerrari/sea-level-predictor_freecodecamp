import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(20, 8), layout='constrained')
    ax.scatter(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])
    
    # Create first line of best fit
    lin_reg0 = linregress(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])
    slope0 = lin_reg0[0]
    y_int0 = lin_reg0[1]
    x_0 = df['Year'][0]
    x_1 = 2051
    years = np.arange(x_0, x_1)
    pred_lev = np.array([x*slope0 + y_int0 for x in years])
    ax.plot(years, pred_lev, color='orange')
    
    # Create second line of best fit
    df1 = pd.DataFrame(df.loc[df['Year']>=2000])
    df1.reset_index(inplace=True)

    lin_reg1 = linregress(x=df1['Year'], y=df1['CSIRO Adjusted Sea Level'])
    slope1 = lin_reg1[0]
    y_int1 = lin_reg1[1]

    x_0 = df1['Year'][0]
    x_1 = 2051
    years = np.arange(x_0, x_1)
    pred_lev = np.array([x*slope1 + y_int1 for x in years])
    ax.plot(years, pred_lev, color='red')
  
    # Add labels and title
    ax.set_title('Rise in Sea Level')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()