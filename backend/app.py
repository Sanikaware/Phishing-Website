from flask import Flask, request, jsonify
import pickle
from utils import extract_features_no_http
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend to access backend

# Load model
with open("ml_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    url = data.get("url", "")

    # Whitelist of known safe domains
    whitelist = ["google.com", "facebook.com", "twitter.com", "github.com", "linkedin.com"]

    from urllib.parse import urlparse
    domain = urlparse(url).netloc.lower()
    # Remove port if present
    domain = domain.split(':')[0]

    # Check whitelist - only exact matches, no subdomains
    if domain in whitelist:
        print(f"URL '{url}' is in whitelist. Marking as Safe.")
        return jsonify({"prediction": "Safe"})

    features = extract_features_no_http(url)
    print(f"URL: {url}")
    print(f"Extracted features: {features}")
    prediction = model.predict([features])[0]
    print(f"Model prediction: {prediction}")

    result = "Phishing" if prediction == 1 else "Safe"
    return jsonify({"prediction": result})

if __name__ == "__main__":
    app.run(debug=True)
