import requests

def get_weather(api_key, city):
    """Lấy dữ liệu thời tiết từ OpenWeatherMap API."""
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric', # Lấy nhiệt độ theo độ C
        'lang': 'vi'       # Lấy mô tả bằng tiếng Việt
    }

    try:
        response = requests.get(base_url, params=params)
        return response.json() # Trả về dữ liệu dạng JSON
    except requests.exceptions.RequestException:
        return {"cod": "error", "message": "Lỗi kết nối mạng."}