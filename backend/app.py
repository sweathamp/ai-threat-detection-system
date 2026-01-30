from flask import Flask, request, jsonify
import pickle

from features import extract_features
from utils import get_risk_level, get_impact, get_recommended_actions

app = Flask(__name__)

# Load trained model
with open("../models/url_risk_model.pkl", "rb") as f:
    model = pickle.load(f)


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "AI Cyber Threat Intelligence API is running"
    })


@app.route("/analyze-url", methods=["POST"])
def analyze_url():
    data = request.get_json()

    if not data or "url" not in data:
        return jsonify({"error": "URL is required"}), 400

    url = data["url"]

    # Feature extraction
    features = extract_features(url)

    # Prediction
    probability = model.predict_proba([features])[0][1]

    # Risk interpretation
    risk_level, risk_score = get_risk_level(probability)
    impact = get_impact(risk_level)
    actions = get_recommended_actions(risk_level)

    return jsonify({
        "url": url,
        "risk_level": risk_level,
        "risk_score": f"{risk_score}%",
        "if_you_continue": impact,
        "recommended_action": actions
    })


if __name__ == "__main__":
    app.run(debug=True)
