from pathlib import Path
import csv
from datetime import datetime
from copy import deepcopy

import matplotlib.pyplot as plt


def load_death_valley_weather():
    path = Path('weather_data/death_valley_2021_simple.csv')
    lines = path.read_text().splitlines()
    reader = csv.reader(lines)
    header_row = next(reader)

    # print(header_row)

    # for index, column_header in enumerate(header_row):
    #    print(index, column_header)

    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        try:
            high = int(row[3])
            low = int(row[4])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    # Plot the high temperatures.
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, highs, color='red', alpha=0.5)
    ax.plot(dates, lows, color='blue', alpha=0.5)
    ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

    # Format plot.
    ax.set_title("Daily high temperatures, July 2021", fontsize=24)
    ax.set_xlabel('', fontsize=16)
    fig.autofmt_xdate()
    ax.set_ylabel('Temperature (F)', fontsize=16)
    ax.tick_params(labelsize=16)

    plt.show()


def load_sitka_weather():
    path = Path('weather_data/sitka_weather_2021_simple.csv')
    lines = path.read_text().splitlines()
    reader = csv.reader(lines)
    header_row = next(reader)

    # print(header_row)

    #for index, column_header in enumerate(header_row):
    #    print(index, column_header)

    # Extract dates and high temperatures.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        high = int(row[4])
        dates.append(current_date)
        highs.append(high)
        lows.append(int(row[5]))


    # Plot the high temperatures.
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, highs, color='red', alpha=0.5)
    ax.plot(dates, lows, color='blue', alpha=0.5)
    ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

    # Format plot.
    ax.set_title("Daily high temperatures, July 2021", fontsize=24)
    ax.set_xlabel('', fontsize=16)
    fig.autofmt_xdate()
    ax.set_ylabel('Temperature (F)', fontsize=16)
    ax.tick_params(labelsize=16)

    plt.show()


def open_file():
    path = Path('weather_data/etmgeg_260.txt')
    lines = path.read_text().splitlines()
    return csv.reader(lines)


def read_txt_file():
    reader = open_file()

    header_found = False
    counter = 0
    while not header_found and counter < 100:
        current_row = next(reader)
        # print(current_row)
        if not current_row:
            header_found = True
        counter += 1

    header_row = next(reader)

    columns = {}

    for index, column_header in enumerate(header_row):
        columns[column_header.strip()] = index

    print(columns)

    next(reader)

    return columns, reader


def load_period_data(start, end, field_to_ld):
    columns, data = read_txt_file()

    loaded_data = []
    dates = []
    previous_value = None
    total = 0
    for row in data:
        date = datetime.strptime(row[columns['YYYYMMDD']], '%Y%m%d')

        if start <= date <= end:
            value = float(row[columns[field_to_ld]])/10
            total += value
            # if previous_value is not None:
            #     ma = previous_value * 0.8 + value * 0.2
            # else:
            #     ma = value
            previous_value = value
            loaded_data.append(total)
            dates.append(datetime.strptime(row[columns['YYYYMMDD']], '%Y%m%d'))

    return dates, loaded_data


# Plot the high temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
# ax.plot(dates, highs, color='red', alpha=0.5)
# ax.plot(dates, lows, color='blue', alpha=0.5)
# ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# field_to_load = "TX"
field_to_load = "SQ"
# field_to_load = "RH"

dates, highs22 = load_period_data(datetime(2022, 3, 1), datetime(2022, 4, 30), field_to_load)
ax.plot(highs22, color='blue', alpha=0.5, label="2022")

dates, highs23 = load_period_data(datetime(2023, 3, 1), datetime(2023, 4, 30), field_to_load)
ax.plot(highs23, color='red', alpha=0.5, label="2023")

# print(highs23)

# Format plot.
# ax.set_title("Daily high temperatures, July 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.legend(loc="upper left")
ax.set_ylabel('Temperature (C)', fontsize=16)
ax.tick_params(labelsize=16)

plt.show()

