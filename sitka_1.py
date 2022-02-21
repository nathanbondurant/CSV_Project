import csv
from email import header
infile = open("sitka_weather_07-2018_simple.csv", "r")
csv_file = csv.reader(infile, delimiter = ',')

header_row = next(csv_file)

#print(type(header_row))

for index, column_header in enumerate(header_row):  #allows you to see the index for each value
    print(index, column_header)

highs = []
for i in csv_file:
    highs.append(int(i[5]))
print(highs)

import matplotlib.pyplot as plt #giving it an alias, plt is usually the alias for pyplot

plt.plot(highs, c='red')

plt.title("Daily high temperatures, July 2018", fontsize = 16)
plt.xlabel("")
plt.ylabel("Temperatures (F)", fontsize = 16)
plt.tick_params(axis = 'both', which='major', labelsize=16)

plt.show()