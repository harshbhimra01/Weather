import tkinter as tk
from tkinter import messagebox
import requests


def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200:
        weather = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'pressure': data['main']['pressure'],
            'wind_speed': data['wind']['speed']
        }
        return weather
    else:
        return None


def show_weather():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name")
        return

    api_key = '3b556fc323b34e2be3980c193dfd20ad'  # Replace with your actual API key
    weather = get_weather(city, api_key)

    if weather:
        result_var.set(
            f"City: {weather['city']}\n"
            f"Temperature: {weather['temperature']}°C\n"
            f"Weather: {weather['description']}\n"
            f"Humidity: {weather['humidity']}%\n"
            f"Pressure: {weather['pressure']} hPa\n"
            f"Wind Speed: {weather['wind_speed']} m/s"
        )
    else:
        messagebox.showerror("Error", "City not found or API request failed")


# Create the main window
root = tk.Tk()
root.title("Weather App")

# Create and place the widgets
tk.Label(root, text="Enter city name:").pack(pady=5)

city_entry = tk.Entry(root)
city_entry.pack(pady=5)

tk.Button(root, text="Get Weather", command=show_weather).pack(pady=5)

result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var, justify="left")
result_label.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
