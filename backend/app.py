from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "status": "Backend running",
        "message": "AI Threat Detection System API"
    })

if __name__ == "__main__":
    app.run(debug=True)
