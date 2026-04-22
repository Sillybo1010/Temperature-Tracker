"""
may_2025_temps.py
Author: ITP 150 Student Subaita Sajjad
Date Created: April 13th 2026
This script reads a csv file containing temperatures recorded at the Dulles
Sterling area by the National Weather Service for May 2025. We print the data
and calculate the average temperature for each day. We determine the lowest
temperature and the date it occurred on. We determine the highest temperature
and the date it occurred on. We calculate the average of the average
temperatures. The descriptive statistics are stored in a Python dictionary
and saved to a file in the json format that keeps the structure of the
dictionary.

"""
import csv
import json


def input_menu_choice(menu_string, valid_choices):
    while True:
        try:
            print('-'*68)
            print(menu_string)
            print('-'*68)
            # Get the user's choice
            choice = int(input())
            # Validate the choice
            if choice in valid_choices:
                return choice
            else:
                raise ValueError
        except ValueError:
            print('Invalid. Please enter 1, 2, 3, 4, 5, or 99 as an integer.')


def read_the_file():
    try:
        filename = 'may2025temps.txt'
        temps_list = []
        with open(filename, newline='') as temps_file:
            temps_reader = csv.reader(temps_file, delimiter='\t')
            temps_list = [row for row in temps_reader]
        print(temps_list)
        return temps_list
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return []
    except PermissionError:
        print(f"Error: You do not have permission to read '{filename}'.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []


def data_conversions(temps_list):
    """convert all numerical data to integers or floats and calc avg. temp"""
    try:
        for row in range(0, len(temps_list)):
            temps_list[row][1] = int(temps_list[row][1])
            temps_list[row][2] = int(temps_list[row][2])
            temps_list[row].append((temps_list[row][1]+temps_list[row][2])/2)
        print("There are ", len(temps_list), "rows within the temps list.")
        print(temps_list)
        return temps_list
    except IndexError:
        print('An Index Error occurred.')
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []


def display_list(temps_list):
    try:
        print(f'{"Dates":10s}{"Low Temp":>10s}{"High Temp":>10s}\
        {"Average Temp":>15s}')
        for row in range(len(temps_list)):
            print(f'{temps_list[row][0]:10s}{temps_list[row][1]:>10d}\
            {temps_list[row][2]:>10d}{temps_list[row][3]:15.1f}')
    except IndexError:
        print('An Index Error occurred.')
    except ValueError:
        print('A Value Error occurred.')
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def calc_lowest(temps_list, temps_stats):
    try:
        if temps_list:
            lowest_low = temps_list[0][1]
            lowest_date = temps_list[0][0]
            # search through the remaining rows
            for row in range(1, len(temps_list)):
                if temps_list[row][1] < lowest_low:
                    lowest_low = temps_list[row][1]
                    lowest_date = temps_list[row][0]
            print(f'\n{"Lowest Low":40s}{"Date":>20s}')
            print(f'{lowest_low:<40d}{lowest_date:>20s}')
            temps_stats["Lowest Low"] = lowest_low
            temps_stats["Lowest Low Date"] = lowest_date
        else:
            print('The temps list is empty. Read the list first.')
        return temps_stats
    except IndexError:
        print('An Index Error occurred.')
        return {}
    except ValueError:
        print('A Value Error occurred.')
        return {}
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return {}


def calc_highest(temps_list, temps_stats):
    try:
        if temps_list:
            highest_high = temps_list[0][2]
            highest_date = temps_list[0][0]
            # search through the remaining rows
            for row in range(1, len(temps_list)):
                if temps_list[row][2] > highest_high:
                    highest_high = temps_list[row][2]
                    highest_date = temps_list[row][0]
            print(f'\n{"Highest High":40s}{"Date":>20s}')
            print(f'{highest_high:<40d}{highest_date:>20s}')
            temps_stats["Highest High"] = highest_high
            temps_stats["Highest High Date"] = highest_date
        else:
            print('The temperatures list is empty. Read the list first.')
        return temps_stats
    except IndexError:
        print('An Index Error occurred.')
        return {}
    except ValueError:
        print('A Value Error occurred.')
        return {}
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return {}


def calc_average(temps_list, temps_stats):
    try:
        if temps_list:
            sum_avg_temps = 0
            for row in range(len(temps_list)):
                sum_avg_temps = sum_avg_temps + temps_list[row][3]
            average_average_temps = sum_avg_temps / len(temps_list)
            print(f'\n{"Average of Average Temps":40s}')
            print(f'{average_average_temps:<40.1f}')
            temps_stats["Average of Average Temps"] = average_average_temps
        return temps_stats
    except IndexError:
        print('An Index Error occurred.')
        return {}
    except ZeroDivisionError:
        print('A Zero Division error occurred.')
        return {}
    except ValueError:
        print('A Value Error occurred.')
        return {}
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return {}


def save_stats(temps_stats):
    try:
        if temps_stats:
            filename = 'temps_stats.json'
            print(temps_stats)
            with open(filename, 'w', newline='') as temps_stats_file:
                json.dump(temps_stats, temps_stats_file, indent=4)
            print("The temps_stats.json file has been updated.")
    except PermissionError:
        print(f"Error: You do not have permission to write to '{filename}'.")
    except OSError as e:
        print(f"An unexpected operating system error occurred for '{filename}': {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def main():
    DISPLAY_LIST = 1
    LOWEST = 2
    HIGHEST = 3
    AVERAGE = 4
    SAVE_STATS = 5
    QUIT = 99

    temperatures = []
    temperatures_stats = {}
    choice = 0
    temperatures = read_the_file()
    temperatures = data_conversions(temperatures)
    if temperatures:
        print('May 2025 Temperature Tracker')
        while choice != QUIT:
            menu_string = 'Please choose from the following menu: \
            \nEnter 1 to print the May 2025 temps_list list.\
            \nEnter 2 to find lowest temperature and its date.\
            \nEnter 3 to find highest temperature and its date.\
            \nEnter 4 to display average of average daily temperature.\
            \nEnter 5 to save the statistics.\
            \nEnter 99 to Quit.'
            valid_choices = [1, 2, 3, 4, 5, 99]
            choice = input_menu_choice(menu_string, valid_choices)
            if choice == DISPLAY_LIST:
                display_list(temperatures)
            elif choice == LOWEST:
                temperatures_stats = calc_lowest(temperatures,
                                                 temperatures_stats)
            elif choice == HIGHEST:
                temperatures_stats = calc_highest(temperatures,
                                                  temperatures_stats)
            elif choice == AVERAGE:
                temperatures_stats = calc_average(temperatures,
                                                  temperatures_stats)
            elif choice == SAVE_STATS:
                save_stats(temperatures_stats)
            else:
                print('Enjoy the weather.')
    else:
        print('A problem occurred while reading the file or converting values.')


if __name__ == '__main__':
    main()