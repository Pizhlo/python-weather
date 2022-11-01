from coordinates import get_location
from weather_api_service import get_weather
from weather_formatter import format_weather


def main():
    coords = get_location()
    weather = get_weather(coords)
    print(format_weather(weather))


if __name__ == "__main__":
    main()
