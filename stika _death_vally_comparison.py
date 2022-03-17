import csv
from datetime import datetime
from matplotlib import dates



#Sitka

#Import data
sitka = open("sitka_weather_2018_simple.csv", "r")
s_csv_file = csv.reader(sitka, delimiter = ',')
s_header_row = next(s_csv_file)



sitka_name = s_header_row.index("NAME")
sitka_date = s_header_row.index("DATE")
sitka_min = s_header_row.index("TMIN")
sitka_max = s_header_row.index("TMAX")

sitka_highs = []
sitka_lows = []
sitka_dates = []

for i in s_csv_file:

    try:
        s_name = i[sitka_name]
        current_date = datetime.strptime(i[sitka_date], "%Y-%m-%d")
        high = int(i[sitka_max])
        low= int(i[sitka_min])

    except ValueError:
        print(f"Missing Data for {current_date}")

    else:
        sitka_highs.append(high)
        sitka_dates.append(current_date)
        sitka_lows.append(low)

#Death Valley

#import data
death_valley = open("death_valley_2018_simple.csv", "r")
d_csv_file = csv.reader(death_valley, delimiter = ',')
d_header_row = next(d_csv_file)

#for index, column_header in enumerate(d_header_row):  #allows you to see the index for each value
    #print(index, column_header)
    
dv_name = d_header_row.index("NAME")
dv_date = d_header_row.index("DATE")
dv_min = d_header_row.index("TMIN")
dv_max = d_header_row.index("TMAX")

dv_highs = []
dv_lows = []
dv_dates = []

for i in d_csv_file:
    try:
        d_name = i[dv_name]
        current_date = datetime.strptime(i[dv_date], "%Y-%m-%d")
        high = int(i[dv_max])
        low= int(i[dv_min])

    except ValueError:
        print(f"Missing Data for {current_date}")

    else:
        dv_highs.append(high)
        dv_dates.append(current_date)
        dv_lows.append(low)

#Create graphs

import matplotlib.pyplot as plt #giving it an alias, plt is usually the alias for pyplot

fig = plt.figure()

plt.suptitle(f"Temperature comparison between {s_name}  and {d_name} ", fontsize=16)
#Sitka Plot

plt.subplot(2,1,1)
plt.title(s_name)
plt.plot(sitka_dates, sitka_highs, c='red')
plt.plot(sitka_dates, sitka_lows, c='blue')
plt.fill_between(sitka_dates, sitka_highs, sitka_lows, facecolor = 'blue', alpha=0.1)

#Death Vally Plot
plt.subplot(2,1,2)
plt.title(d_name)
plt.plot(dv_dates, dv_highs, c='red')
plt.plot(dv_dates, dv_lows, c='blue')
plt.fill_between(dv_dates, dv_highs, dv_lows, facecolor = 'blue', alpha=0.1)


fig.autofmt_xdate()

plt.show()

