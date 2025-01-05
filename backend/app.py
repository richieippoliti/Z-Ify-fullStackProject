from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from zify_logic import zify_word
import os

app = Flask(__name__)
CORS(app)  # Enable CORS

@app.route('/zify', methods=['POST'])
def zify():
    """Endpoint to Z-ify a word."""
    if not request.is_json:
        return jsonify({"error": "Invalid or missing JSON"}), 400

    data = request.json  # Get JSON input
    word = data.get("word", "")  # Extract 'word' field from JSON

    if not word:
        return jsonify({"error": "No word provided"}), 400

    zified_word = zify_word(word)  # Apply the Z-ify logic
    return jsonify({"original_word": word, "zified_word": zified_word})

frontend_folder = os.path.join(os.getcwd(), "..", "frontend", "dist")

@app.route("/", defaults={"filename": "index.html"})
@app.route("/<path:filename>")
def serve_frontend(filename):
    """Serve the React frontend."""
    if filename == "index.html" or not filename:
        return send_from_directory(frontend_folder, "index.html")
    file_path = os.path.join(frontend_folder, filename)
    if os.path.exists(file_path):
        return send_from_directory(frontend_folder, filename)
    return send_from_directory(frontend_folder, "index.html")


if __name__ == '__main__':
    app.run(debug=True)