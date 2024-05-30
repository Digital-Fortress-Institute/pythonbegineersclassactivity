import tkinter as tk
from tkinter import messagebox
import requests
from configparser import ConfigParser

# Load the API key from the configuration file
config_file = "C:/Users/SMITH/Desktop/api/config.ini"
config = ConfigParser()
config.read(config_file)

try:
    api_key = config['api_keys']['api_key']
except KeyError as e:
    messagebox.showerror("Error", f"API key not found: {e}")
    api_key = None

# Function to get weather
def get_weather(lat, lon):
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather = {
            'city': data.get('name', 'Unknown location'),
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed']
        }
        return weather
    else:
        return None

# Function to display weather
def display_weather():
    lat = lat_entry.get()
    lon = lon_entry.get()
    if lat and lon:
        try:
            lat = float(lat)
            lon = float(lon)
            weather = get_weather(lat, lon)
            if weather:
                result = (f"City: {weather['city']}\n"
                          f"Temperature: {weather['temperature']}°C\n"
                          f"Description: {weather['description']}\n"
                          f"Humidity: {weather['humidity']}%\n"
                          f"Wind Speed: {weather['wind_speed']} m/s")
                weather_result.config(text=result)
            else:
                messagebox.showerror("Error", "Location not found or unable to fetch weather!")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid latitude and longitude values.")
    else:
        messagebox.showwarning("Input Error", "Please enter both latitude and longitude.")

# Create the main window
app = tk.Tk()
app.title("Weather App")
app.geometry("300x300")

# Add widgets
lat_label = tk.Label(app, text="Enter Latitude:")
lat_label.pack(pady=5)
lat_entry = tk.Entry(app)
lat_entry.pack(pady=5)

lon_label = tk.Label(app, text="Enter Longitude:")
lon_label.pack(pady=5)
lon_entry = tk.Entry(app)
lon_entry.pack(pady=5)

get_weather_button = tk.Button(app, text="Get Weather", command=display_weather)
get_weather_button.pack(pady=10)

weather_result = tk.Label(app, text="", justify="left")
weather_result.pack(pady=20)

# Run the main loop
app.mainloop()
