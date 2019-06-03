import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
#%%
# Import both data tables into python using pandas. Set the index column to "MESS_DATUM" and parse the column values as dates. [1P]
garmisch  = pd.read_csv("./data/produkt_klima_tag_20171010_20190412_01550.txt", sep = ";", index_col="MESS_DATUM", parse_dates=["MESS_DATUM"], na_values=-999.0)
zugspitze = pd.read_csv("./data/produkt_klima_tag_20171010_20190412_05792.txt",sep = ";", index_col="MESS_DATUM", parse_dates=["MESS_DATUM"], na_values=-999.0)

#%%
# Clip the tables to the year 2018: [1P]
garmisch  = garmisch["2018"]
zugspitze = zugspitze["2018"]

#%%
# Resample the temperature data to monthly averages (" TMK") and store them in simple lists: [1P]
garmisch_agg  = list(garmisch.resample("1M").mean()[" TMK"])
zugspitze_agg = list(zugspitze.resample("1M").mean()[" TMK"])
 
#%%
# Define a plotting function that draws a simple climate diagram
# Add the arguments as mentioned in the docstring below [1P]
# Set the default temperature range from -15°C to 20°C and the precipitation range from 0mm to 370mm [1P]
def create_climate_diagram(df,
                           temp_col,
                           prec_col,
                           title,
                           output_filename,
                           temp_range=(-15,20),
                           prec_range=(0,370)):
    """
    Draw a climate diagram.
    
    Parameters
    ----------
    df : pd.DataFrame
        Dataframe with values to plot from
    temp_col : str
        Name of temperature column
    prec_col : str
        Name of precipitation column
    title : String
        The title for the figure
    filename : String
        The name of the output figure
    temp_range : Tuple of 2 Numbers
        The minimum and maximun temperature values to display
    prec_range : Tuple of 2 Numbers
        The minimum and maximun precipitation values to display


    Returns
    -------
    The figure
    
    """

    fig = plt.figure(figsize=(10,8))
    plt.rcParams['font.size'] = 16

    ax2 = fig.add_subplot(111)
    ax1 = ax2.twinx()
    
    
    df_agg = df.resample(rule = "1MS", ).agg({temp_col:"mean", prec_col:"sum"})
    print(df_agg.index)

    # Draw temperature values as a red line and precipitation values as blue bars: [1P]
    # Hint: Check out the matplotlib documentation how to plot barcharts. Try to directly set the correct
    #       x-axis labels (month shortnames).
    ax2.bar(df_agg.index, df_agg[prec_col], color = "blue", width = 20, align = 'center')
    ax1.plot(df_agg[temp_col], color= "red")
    # Set appropiate limits to each y-axis using the function arguments: [1P]
    ax2.set_ylim(prec_range)
    ax1.set_ylim(temp_range)
    #monate auf der xachse
    ax1.xaxis.set_major_locator(mdates.MonthLocator())
    ax1.xaxis.set_major_formatter(mdates.DateFormatter("%b/%y"))
    
    
    #plt.xticks(rotation=45)
    fig.autofmt_xdate()
    #ax1.set_xlim(df_agg.index[0],df_agg.index[-1] )
    
    # Set appropiate labels to each y-axis: [1P]
    ax2.set_ylabel("Precipitation [mm]")
    ax1.set_ylabel("Temperature [°C]")

    # Give your diagram the title from the passed arguments: [1P]
    plt.title(title)
    

    # Save the figure as png image in the "output" folder with the given filename. [1P]
    plt.savefig(output_filename + ".png")
    return fig
#%%
# Use this function to draw a climate diagram for 2018 for both stations and save the result: [1P]
create_climate_diagram(garmisch, " TMK", " RSK", "klimadiagram", "garmisch"  )
create_climate_diagram(zugspitze, " TMK", " RSK", "klimadiagram", "zugspitze")
