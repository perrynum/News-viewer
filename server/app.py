import os
from flask import Flask, jsonify, request, send_from_directory
from dotenv import load_dotenv
from news_api import get_top_headlines, search_everything, NewsAPIError

load_dotenv()

app = Flask(__name__, static_folder="../web", static_url_path="")

@app.route("/")
def root():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/api/top-headlines", methods=["GET"])
def api_top_headlines():
    country = request.args.get("country", "us")
    page_size = int(request.args.get("pageSize", 20))
    try:
        data = get_top_headlines(country=country, page_size=page_size)
        return jsonify(data)
    except NewsAPIError as e:
        return jsonify({"status": "error", "message": str(e)}), 502

@app.route("/api/search", methods=["GET"])
def api_search():
    q = request.args.get("q", "").strip()
    if not q:
        return jsonify({"status": "error", "message": "Missing query parameter 'q'"}), 400
    page_size = int(request.args.get("pageSize", 20))
    sort_by = request.args.get("sortBy", "publishedAt")
    language = request.args.get("language", "en")
    try:
        data = search_everything(q=q, page_size=page_size, sort_by=sort_by, language=language)
        return jsonify(data)
    except NewsAPIError as e:
        return jsonify({"status": "error", "message": str(e)}), 502

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
