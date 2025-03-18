from flask import Flask, request, jsonify
import os
from clear import fetch_novel_info, download_novel  # clear.py の関数を利用

app = Flask(__name__)

@app.route("/fetch", methods=["POST"])
def fetch_novel():
    data = request.json
    url = data.get("url")
    start_chapter = int(data.get("start_chapter", 1))

    if not url:
        return jsonify({"error": "URL is required"}), 400

    title, sublist = fetch_novel_info(url)
    download_novel(start_chapter, sublist, title)
    
    return jsonify({"message": "Download started", "title": title})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
