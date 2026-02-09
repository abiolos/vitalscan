# api/routes/diagnose.py
from flask import Blueprint, request, jsonify

diagnose_bp = Blueprint("diagnose", __name__)

@diagnose_bp.route("/diagnose", methods=["POST"])
def diagnose():
    file = request.files.get("image")
    if not file:
        return jsonify({"error": "No image"}), 400

    return jsonify({
        "diabetes_risk": 0.23,
        "anemia_risk": 0.12,
        "nutrition_deficiency_risk": 0.44,
        "disclaimer": "Pré-diagnostic éducatif uniquement."
    })
