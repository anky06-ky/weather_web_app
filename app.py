import os
from dotenv import load_dotenv
from flask import Flask, render_template, request
from weather import get_weather # Import hàm từ file weather.py

load_dotenv() # Tải các biến từ file .env
# Khởi tạo ứng dụng Flask
app = Flask(__name__)

# Lấy API key từ biến môi trường để bảo mật

# Dịch vụ triển khai (Render) sẽ cung cấp giá trị cho biến này
API_KEY = os.environ.get("OPENWEATHER_API_KEY")

@app.route("/", methods=["GET", "POST"])
def home():
    weather_data = None
    error_message = None

    # Nếu người dùng gửi yêu cầu bằng cách nhấn nút "Tra cứu" (phương thức POST)
    if request.method == "POST":
        city = request.form["city"]
        if not city:
            error_message = "Vui lòng nhập tên thành phố."
        else:
            # Gọi hàm get_weather để lấy dữ liệu
            data = get_weather(API_KEY, city)
            
            # Xử lý kết quả trả về
            if data and data.get("cod") == 200:
                weather_data = {
                    "city": data["name"],
                    "description": data["weather"][0]["description"].capitalize(),
                    "temperature": round(data["main"]["temp"]), # Làm tròn nhiệt độ
                    "humidity": data["main"]["humidity"],
                    "main_status": data["weather"][0]["main"], # Ví dụ: "Clouds", "Rain", "Clear"
                    "icon": data["weather"][0]["icon"],
                    "feels_like": round(data["main"]["feels_like"]), # Nhiệt độ cảm nhận
                    "wind_speed": data["wind"]["speed"]  
                }
            else:
                # Nếu có lỗi (không tìm thấy, key sai,...)
                error_message = data.get("message", "Không thể lấy dữ liệu.")

    # Trả về file HTML và truyền dữ liệu (thời tiết hoặc lỗi) sang
    return render_template("index.html", weather=weather_data, error=error_message)

# Chạy ứng dụng khi file này được thực thi trực tiếp
if __name__ == "__main__":
    app.run(debug=True)