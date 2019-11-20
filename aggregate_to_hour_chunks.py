"""
This aggregates the Volume data into 1-hour bins.
"""
import pandas as pd
from tqdm import tqdm

def sum_over_hours(df):
    volumes = []
    durations = []

    hour = []
    year  = []
    month = []
    day = []
    Event = []
    House = []

    # starting value
    vol = df['Volume'][0]
    dur = df['Duration'][0]

    for i in tqdm(range(len(df)-1)):
        sameday =  df['year'][i+1]==df['year'][i] and df['month'][i+1]==df['month'][i] and df['day'][i+1]==df['day'][i]
        if sameday:
            samehour = df['hour'][i+1] == df['hour'][i]
            samehouse = df['House'][i+1] == df['House'][i]
            same_event = df['Event'][i+1] == df['Event'][i]
           
            if samehour and samehouse and same_event:
                vol = vol + df['Volume'][i+1]
                dur = dur + df['Duration'][i+1]
            else:
                volumes.append(vol)
                durations.append(dur)

                hour.append(df['hour'][i])
                year.append(df['year'][i])
                month.append(df['month'][i])
                day.append(df['day'][i])
                #new
                Event.append(df['Event'][i])
                House.append(df['House'][i])

            
                vol = df['Volume'][i+1] #reset this AFTER appending vol.
                dur = df['Duration'][i+1]

    d = {'year': year, 'month':month, 'day':day, 'hour':hour, 'Event':Event, 'House':House, 'Volume': volumes, 'Duration': durations}
    newdf = pd.DataFrame(data=d)
    newdf.to_csv('REU2016_volume_and_duration_by_hour2.csv')
    return newdf
