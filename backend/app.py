from flask import Flask, request, jsonify
from flask_cors import CORS
from zify_logic import zify_word

app = Flask(__name__)
CORS(app)  # Enable CORS

@app.route('/')
def home():
    """Health check or welcome route."""
    return jsonify({"message": "Welcome to the Z-ify API!"})

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

if __name__ == '__main__':
    app.run(debug=True)