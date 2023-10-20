import csv
from matplotlib import pyplot as plt

filename = 'D:\WORK\Learning\csv\weather_data\sitka_weather_07-2021_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
   

    # Чтение максимальных температура 
    highs = []
    for row in reader:
        high = int(row[5])
        highs.append(high)

    print(highs)

# нанесение данных на гистограмму
fig, ax = plt.subplots()
ax.plot(highs, c='red')

# Форматирование диаграммы
plt.title("Daily hight temperatures, 07/2021", fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both',which='major', labelsize=16)

plt.show()