from flask import Flask, jsonify
from services.db import patients_col
from routes.diagnose import diagnose_bp
from services.patients import add_patient


app = Flask(__name__)
app.register_blueprint(diagnose_bp, url_prefix="/api")

@app.route("/health")
def health():
    count = patients_col.count_documents({})
    return jsonify({"status": "ok", "patients_count": count})
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
from services.patients import add_patient

@app.route("/add_patient/<patient_id>/<consent>")
def add_patient_route(patient_id, consent):
    add_patient(patient_id, consent == "true")
    return {"status": "ok"}
