import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'D:\WORK\Learning\csv\weather_data\sitka_weather_2021_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
   

    # Чтение максимальных температура 
    highs = []
    dates = []
    lows = []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        dates.append(current_date)
        high = int(row[4])
        low = int(row[5])
        highs.append(high)
        lows.append(low)

    print(highs)

# нанесение данных на гистограмму
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')
ax.plot(dates, lows, c='blue')
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Форматирование диаграммы
plt.title("Daily high and low temperatures - 2021", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both',which='major', labelsize=16)

plt.show()