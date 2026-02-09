# api/app.py
from flask import Flask
from routes.diagnose import diagnose_bp

app = Flask(__name__)
app.register_blueprint(diagnose_bp, url_prefix="/api")

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
