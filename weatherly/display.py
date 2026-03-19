from .models import WeatherData


def display_weather(data: WeatherData) -> None:
    """Display weather data in the terminal with emoji labels."""
    time_emoji = "☀️" if data.is_day else "🌙"
    print(f"\n{time_emoji}  Weather for {data.location}")
    print("─" * 40)
    print(f"🌡️  Temperature: {data.temperature_c}°C ({data.temperature_f}°F)")
    print(f"🤔  Feels like:  {data.feels_like_c}°C")
    print(f"💧  Humidity:    {data.humidity}%")
    print(f"📝  Conditions:  {data.description}")
    print(f"💨  Wind:        {data.wind_speed_kph} kph {data.wind_direction}")
