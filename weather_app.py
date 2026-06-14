import requests

def get_weather():
    city = input("Enter city name: ").strip()

    if not city:
        print("Error: Please enter a city name")
        return

    # REPLACE THIS WITH YOUR NEW KEY FROM STEP 1
    api_key = "4242d450bd3cc5b33cc32e5a347945c6"

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url, timeout=10)
        data = response.json()

        if response.status_code == 200:
            print(f"\nWeather in {data['name']}:")
            print(f"Temperature: {data['main']['temp']}°C")
            print(f"Humidity: {data['main']['humidity']}%")
            print(f"Condition: {data['weather'][0]['description'].title()}")
            print(f"Wind Speed: {data['wind']['speed']} m/s")
        elif response.status_code == 401:
            print("Error: Invalid API key. Did you wait 10 mins after creating it?")
        else:
            print(f"Error: {data.get('message', 'City not found')}")

    except requests.exceptions.RequestException:
        print("Error: Check your internet connection")

if __name__ == "__main__":
    get_weather()