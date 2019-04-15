import pandas as pd
import matplotlib.pyplot as plt

# Import both data tables into python using pandas. Set the index column to "MESS_DATUM" and parse the column values as dates. [1P]
garmisch  = 
zugspitze = 

# Clip the tables to the year 2018: [1P]
garmisch  = 
zugspitze = 

# Resample the temperature data to monthly averages (" TMK") and store them in simple lists: [1P]
garmisch_temp  = list(...)
zugspitze_temp = list(...)

# Resample the precipitation data to monthly sums (" RSK") and store them in simple lists: [1P]
garmisch_prec  =  list(...)
zugspitze_prec =  list(...)

# Define a plotting function that draws a simple climate diagram
# Add the arguments as mentioned in the docstring below [1P]
# Set the default temperature range from -15°C to 20°C and the precipitation range from 0mm to 370mm [1P]
def create_climate_diagram(...):
    """
    Draw a climate diagram.
    
    Parameters
    ----------
    temp : A list with 12 numbers, one for each month
        The temperature values
    prec : A list with 12 numbers, one for each month
        The precipitation values
    title: String
        The title for the figure
    filename: String
        The name of the output figure
    temp_min: Number
        The minimum temperature value to display
    temp_max: Number
        The maximum temperature value to display
    prec_min: Number
        The minimum precipitation value to display
    prec_max: Number
        The maximum precipitation value to display

    Returns
    -------
    The figure
    
    """

    fig = plt.figure(figsize=(10,8))
    plt.rcParams['font.size'] = 16

    ax2 = fig.add_subplot(111)
    ax1 = ax2.twinx()

    # Draw temperature values as a red line and precipitation values as blue bars: [1P]
    ax2.bar(...)
    ax1.plot(...)

    # Put meaningful labels on each Y-axis and give your diagram the title from the passed arguments: [1P]
    ax2.
    ax1.
    plt.title(...)

    ax1.set_ylim((temp_min,temp_max))
    ax2.set_ylim((prec_min,prec_max))

    ax2.set_xticks(range(12))
    ax2.set_xticklabels(("Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"))
    
    # Save the figure as png image in the "output" folder with the given filename. [1P]
    plt.
    
    return fig

# Use this function to draw a climate diagram for 2018 for both stations and save the result: [1P]
create_climate_diagram(...)
create_climate_diagram(...)
