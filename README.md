
# 🛡️ Phishing Website Detection - Flask App

This is a Flask-based web app that detects whether a given URL is a phishing website or not.

---

## 🚀 Getting Started (Local Deployment)

### 1. Clone the Project

First, clone the project to your local machine:

```bash
git clone <(https://github.com/Sanikaware/Phishing-Website.git)>
cd backend
```

### 2. Create Virtual Environment (Windows)

Create and activate a virtual environment to manage dependencies:

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

Once the virtual environment is activated, install all the required libraries:

```bash
pip install -r requirements.txt
```

If you don't have `requirements.txt` yet, let me know and I'll help generate it based on the libraries you use.

### 4. Run the App

To start the Flask app, simply run:

```bash
python app.py
```

By default, the app will run at:  
**http://127.0.0.1:5000**

Now, the Flask web server should be up and running locally.

---

## 📡 API Endpoints

### `/predict` - POST  
**Description:** Accepts a URL and returns a prediction (whether the URL is phishing or legitimate).

**Input Example (JSON):**
```json
{
  "url": "http://example.com/login"
}
```

**Response Example:**
```json
{
  "prediction": "phishing"
}
```

---

## 🧠 Explanation (Optional)

If **LIME** is implemented, you could add an `/explain` endpoint that provides an explanation of why the model made its prediction.

---

## 🧰 Tools Used

- **Python**: Programming language
- **Flask**: Web framework for building the app
- **Scikit-learn**: Machine learning library for the model
- **LIME** (optional): For model explainability (can be added later)

---

## 📄 Future Enhancements (Optional)

- Cloud Deployment (Render, AWS, etc.)
- Docker container for easy deployment
- Interactive web UI for better user experience
