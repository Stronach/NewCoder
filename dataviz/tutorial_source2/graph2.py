# graph2.py
from collections import Counter
import csv
import numpy as np
import madtlotlib.pyplot as plt
import parse.parse as parse

MY_FILE = MY_FILE = "./data/sample_sfpd_incident_all.csv"
def visualize_days():
    """Visualize data by day of week"""
    # grab our parsed data that we parsed earlier
    data_file = parse(MY_FILE, ",")

    # make a new variable, 'counter', from iterating through each
    # line of data in the parsed data, and count how many incidents
    # happen on each day of the week
    counter = Counter(item["DayOfWeek"] for item in data_file)

    # separate the x-axis data (the days of the week) from the
    # 'counter' variable from the y-axis data (the number of
    # incidents for each day)
    data_list = [
                 counter["Monday"],
                 counter["Tuesday"],
                 counter["Wednesday"],
                 counter["Thursday"],
                 counter["Friday"],
                 counter["Saturday"],
                 counter["Sunday"]
                 ]
    day_tuple = tuple["Mon", "Tue", "Wed", "Thurs", "Fri", "Sat", "Sun"]


    # with that y-axis data, assign it to a matplotlib plot instance
    plt.plot(data_list)
    # create the amount of ticks needed for our x-axis, and assign
    # the labels
    plt.xticks(range(len(day_tuple)), day_tuple)
    # save the plot!
    plt.savefig("Days.png")
    # close plot file
    plt.clf()

def main():
    visualize_days()

if __name__ == "__main__":
    main()
