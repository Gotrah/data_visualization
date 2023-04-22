from pathlib import Path
import csv
from datetime import datetime
from copy import deepcopy
from enum import Enum

import matplotlib.pyplot as plt


class DataType(Enum):
    AVERAGE = 1
    CUMULATIVE = 2
    MOVING_AVERAGE = 3


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
        if not current_row:
            header_found = True
        counter += 1

    header_row = next(reader)

    columns = {}

    for index, column_header in enumerate(header_row):
        columns[column_header.strip()] = index

    next(reader)

    return columns, reader


def load_period_data(start, end, data_config):
    columns, data = read_txt_file()

    loaded_data = []
    dates = []
    data_value = None
    total = 0
    count = 0
    for row in data:
        date = datetime.strptime(row[columns['YYYYMMDD']], '%Y%m%d')

        if start <= date <= end:
            value = float(row[columns[data_config["field"]]])/10
            total += value
            count += 1
            if data_config["data_type"] == DataType.CUMULATIVE:
                data_value = total
            elif data_config["data_type"] == DataType.AVERAGE:
                data_value = total / count
            loaded_data.append(data_value)
            dates.append(datetime.strptime(row[columns['YYYYMMDD']], '%Y%m%d'))

    return dates, loaded_data


def create_graph(data_config):
    fig, ax = plt.subplots()
    dates, data22 = load_period_data(datetime(2022, 3, 1), datetime(2022, 4, 30), data_config)
    ax.plot(data22, color='blue', alpha=0.5, label="2022")

    dates, data23 = load_period_data(datetime(2023, 3, 1), datetime(2023, 4, 30), data_config)
    ax.plot(data23, color='red', alpha=0.5, label="2023")

    ax.set_xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.legend(loc="upper left")
    ax.set_ylabel(data_config["y_label"], fontsize=16)
    ax.tick_params(labelsize=16)


# Plot the statistics.
plt.style.use('seaborn')
create_graph({"field": "SQ", "data_type": DataType.CUMULATIVE, "y_label": "Total sun hours"})
create_graph({"field": "TX", "data_type": DataType.AVERAGE, "y_label": "Average Temperature (C)"})
create_graph({"field": "RH", "data_type": DataType.CUMULATIVE, "y_label": "Total rainfall (mm)"})


plt.show()

