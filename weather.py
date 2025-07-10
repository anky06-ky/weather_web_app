import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric',
        'lang': 'vi'
    }

    try:
        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Không thể lấy dữ liệu. Mã lỗi: {response.status_code}"}
    except requests.exceptions.RequestException as e:
        return {"error": f"Lỗi kết nối: {e}"}
