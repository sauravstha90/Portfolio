# DSC 510
# Week 12
# This program connects with a webservice in order to pull weather data.
# Author
# 03/05/2021

# Importing requests module to send HTTP requests and receive Response Object
# Importing json module to convert json string from Response Object into python dictionary.
import requests
import json


# Made http request using get method from requests library using url and parameters with city name as query and api key.
def city_choice(city_param):

    response = None
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    app_id = "e6d50fdcac9b2157817252047c61978c"
    try:
        response = requests.get(base_url, params={"q": city_param, "units": "imperial", "appid": app_id})
    except ConnectionError:
        print("Connection Error. Please try again.")
    data = json.loads(response.text)
    return data


def zip_choice(zip_param):

    response = None
    endpoint = "http://api.openweathermap.org/data/2.5/weather"
    app_id = "e6d50fdcac9b2157817252047c61978c"
    try:
        response = requests.get(endpoint, params={"zip": zip_param, "appid": app_id})
    except ConnectionError:
        print("Connection Unsuccessful.Please try again.")
    data = json.loads(response.text)
    return data


def city_unit(city_param, city_temp):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    app_id = "e6d50fdcac9b2157817252047c61978c"
    try:
        if city_temp == 'f':
            response = requests.get(base_url, params={"q": city_param, "units": "imperial", "appid": app_id})
            data = json.loads(response.text)
            print_temp(data)
        elif city_temp == 'c':
            response = requests.get(base_url, params={"q": city_param, "units": "metric", "appid": app_id})
            data = json.loads(response.text)
            print_temp(data)
        elif city_temp == 'k':
            response = requests.get(base_url, params={"q": city_param, "appid": app_id})
            data = json.loads(response.text)
            print_temp(data)
        else:
            print("Invalid input. Please try again.")
    except ConnectionError:
        print("Unable to process your request. Please try again.")


def zip_unit(zip_param, unit2):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    app_id = "e6d50fdcac9b2157817252047c61978c"
    try:
        if unit2 == 'f':
            response = requests.get(base_url, params={"q": zip_param, "units": "imperial", "appid": app_id})
            data = json.loads(response.text)
            print_temp(data)
        elif unit2 == 'c':
            response = requests.get(base_url, params={"q": zip_param, "units": "metric", "appid": app_id})
            data = json.loads(response.text)
            print_temp(data)
        elif unit2 == 'k':
            response = requests.get(base_url, params={"q": zip_param, "appid": app_id})
            data = json.loads(response.text)
            print_temp(data)
        else:
            print("Invalid input. Please try again.")
    except ConnectionError:
        print("Unable to process your request. Please try again.")


def print_temp(temp):

    print('Current Weather Conditions For {}.'.format(temp['name']))
    print('Current Temp: {:.2f} degrees'.format(temp['main']['temp']))
    print('High Temp: {:.2f} degrees'.format(temp['main']['temp_max']))
    print('Low Temp: {:.2f} degrees'.format(temp['main']['temp_min']))
    print('Pressure: {:.2f} hPa'.format(temp['main']['pressure']))
    print('Humidity: {}%'.format(temp['main']['humidity']))
    print('Weather Condition: {}'.format((temp['weather'][0]['description']).title()))
    print("Longitude: {}".format(temp['coord']['lon']))
    print("Latitude: {}".format(temp['coord']['lat']))


def search_city():
    while True:
        city_name = input("Please enter the name of the city:")
        city_response = city_choice(city_name)
        if city_response['cod'] != 200:
            print("{} is not a valid zip code. Please try again".format(city_name))
            continue
        else:
            print("\nConnection Successful.")
            print("How would you like to view the temperature?")
            while True:
                city_temp = input("Please enter 'f' for Fahrenheit, 'c' for Celsius, 'k' for Kelvin:").lower()
                if city_temp == 'f' or city_temp == 'c' or city_temp == 'k':
                    city_unit(city_name, city_temp)
                    user_wish()
                else:
                    print("Unable to accept {}. Please try again".format(city_temp))
                    continue


# Asks user for zip code and temperature metrics to provide details on the weather zip code.
def search_zip():
    while True:
        zip_code = input("Please enter the zip code:")
        zip_response = zip_choice(zip_code)
        if zip_response['cod'] != 200:
            print("{} is not a valid zip code. Please try again.".format(zip_code))
            continue
        else:
            print("\nConnection Successful.")
            print("How would you like to view the temperature in?")
            while True:
                zip_temp = input("Please enter 'f' for Fahrenheit, 'c' for Celsius, 'k' for Kelvin:").lower()
                if zip_temp == 'f' or zip_temp == 'c' or zip_temp == 'k':
                    zip_unit(zip_code, zip_temp)
                    user_wish()
                else:
                    print("Unable to accept {}. Please try again".format(zip_temp))
                    continue


# Loop to ask if they want to perform additional weather search or quit.
def user_wish():
    while True:
        char = input("Would you like to continue the weather search? (y/n):").lower()
        if char == 'y':
            main()
        elif char == 'n':
            print("You have exited the program. See you soon!")
            quit()
        else:
            print('Sorry, we only have two options available. Please Press y to continue the weather search or n to exit.')
            continue


# main function to start the program via use of above functions to provides user with readable weather information.
def main():
    print("Welcome to search engine for weather.\n")
    while True:
        user = input("Would you like to lookup weather data by US City or zip code? Enter 1 for US City 2 for zip:").lower()
        if user == '1':
            search_city()
        elif user == '2':
            search_zip()
        elif user == 'q':
            print("You have chosen to exit the program. See you again!")
            break
        else:
            print("\nSorry, {} isn't acceptable. Please enter a valid input.".format(user))
            continue
       

if __name__ == "__main__":
    main()

# Change#:1
# Change(s) Made:1) Changed from nested while loop to functions to loop incorrect user input for all questions asked.
# 2) Changed city_response['cod'] != '200' to city_response['cod'] != 200. Figured the value was an integer instead of
# string of integer
# Date of Change: 03/04/2021
# Author:
# Change Approved by:
# Date Moved to Production: 03/06/2021
