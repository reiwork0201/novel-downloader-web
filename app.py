from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask Web App is running on PythonAnywhere!"

@app.route("/fetch", methods=["POST"])
def fetch_novel():
    data = request.json
    url = data.get("url")
    start_chapter = int(data.get("start_chapter", 1))

    if not url:
        return jsonify({"error": "URL is required"}), 400

    return jsonify({"message": f"Downloading novel from {url} starting at chapter {start_chapter}."})

# PythonAnywhereでは app.run() を使わない！
if __name__ == "__main__":
    # ローカル開発時のみ起動
    app.run(debug=True, port=5050)
