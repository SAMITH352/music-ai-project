from flask import Flask, jsonify, send_file
from flask_cors import CORS
import generate_music

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "🎵 Music AI Backend Running"

@app.route("/generate", methods=["GET"])
def generate():
    try:
        midi_file = generate_music.generate_music()
        return send_file(midi_file, as_attachment=True)
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
