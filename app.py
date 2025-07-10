from flask import Flask, render_template, request
from weather import get_weather

app = Flask(__name__)
API_KEY = "a6ebae32122f93f882bb555f2341a6fa"  # <-- Thay bằng API key của bạn

@app.route("/", methods=["GET", "POST"])
def home():
    weather = None
    error = None

    if request.method == "POST":
        city = request.form["city"]
        if not city:
            error = "Vui lòng nhập tên thành phố."
        else:
            data = get_weather(API_KEY, city)
            if "error" in data:
                error = data["error"]
            elif data.get("cod") == "404":
                error = f"Không tìm thấy thành phố '{city}'."
            else:
                weather = {
                    "city": data["name"],
                    "description": data["weather"][0]["description"].capitalize(),
                    "temperature": data["main"]["temp"],
                    "humidity": data["main"]["humidity"]
                }

    return render_template("index.html", weather=weather, error=error)

if __name__ == "__main__":
    app.run(debug=True)
