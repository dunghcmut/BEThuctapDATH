from flask import Blueprint, jsonify, request

from app.models.ai_model import AIModel


predict_bp = Blueprint("predict", __name__)


@predict_bp.post("/predict")
def predict():
    payload = request.get_json(silent=True) or {}
    raw_value = payload.get("x")

    if raw_value is None:
        return jsonify({"error": "x is required"}), 400

    try:
        value = float(raw_value)
    except (TypeError, ValueError):
        return jsonify({"error": "x must be a number"}), 400

    return jsonify(AIModel.predict(value)), 200
