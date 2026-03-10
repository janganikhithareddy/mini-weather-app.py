import requests
from colorama import Fore, init
from datetime import datetime

# initialize colorama
init(autoreset=True)

# API key
api_key = "147ee5d6d7b12b24910a05a192745d41"

# search history
search_history = []

def get_weather(city):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            city_name = data["name"]
            temperature_c = data["main"]["temp"]
            temperature_f = (temperature_c * 9/5) + 32
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]
            condition = data["weather"][0]["description"]

            # time
            now = datetime.now()
            time = now.strftime("%Y-%m-%d %H:%M:%S")

            search_history.append(city_name)

            print(Fore.GREEN + "\n===== Weather Information =====")
            print(Fore.WHITE + f"City: {city_name}")
            print(Fore.WHITE + f"Temperature: {temperature_c}°C / {temperature_f:.2f}°F")
            print(Fore.WHITE + f"Weather Condition: {condition}")
            print(Fore.WHITE + f"Humidity: {humidity}%")
            print(Fore.WHITE + f"Wind Speed: {wind_speed} m/s")
            print(Fore.WHITE + f"Checked at: {time}")

        else:
            print(Fore.RED + "City not found. Please try again.")

    except:
        print(Fore.RED + "Network error. Check your internet connection.")

while True:
    print(Fore.CYAN + "\n===== Weather App Menu =====")
    print("1. Search Weather")
    print("2. View Search History")
    print("3. Exit")

    choice = input(Fore.YELLOW + "Enter your choice: ")

    if choice == "1":
        city = input("Enter city name: ")
        get_weather(city)

    elif choice == "2":
        print(Fore.MAGENTA + "\nSearch History:")
        if len(search_history) == 0:
            print("No searches yet.")
        else:
            for c in search_history:
                print(c)

    elif choice == "3":
        print(Fore.CYAN + "Thank you for using Weather App!")
        break

    else:
        print(Fore.RED + "Invalid choice. Please select 1, 2, or 3.")
