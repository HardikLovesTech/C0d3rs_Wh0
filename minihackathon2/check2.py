import os
import hashlib
import requests
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

# Ensure uploads folder exists
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Your VirusTotal API Key (Replace with actual key)
VIRUSTOTAL_API_KEY = "31fc95c0d8cf560b727b73eb6f02f80a911a911ec7507da2696947699e98f758"

# Function to get SHA-256 hash of a file
def get_file_hash(file_path):
    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
    except FileNotFoundError:
        return None  # Return None if file doesn't exist
    return sha256_hash.hexdigest()

# Function to check file safety using VirusTotal
def check_virus_total(file_hash):
    if not file_hash:
        return {"status": "Error", "message": "⚠️ File not found!"}

    url = f"https://www.virustotal.com/api/v3/files/{file_hash}"
    headers = {"x-apikey": VIRUSTOTAL_API_KEY}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if data["data"]["attributes"]["last_analysis_stats"]["malicious"] > 0:
            return {"status": "Unsafe", "message": "⚠️ The file is flagged as unsafe!"}
        else:
            return {"status": "Safe", "message": "✅ The file appears safe."}
    return {"status": "Error", "message": "⚠️ Could not check the file on VirusTotal."}

# Homepage Route
@app.route("/")
def index():
    return render_template("ind2.html")

# File Upload Route
@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(file_path)  # Save file in uploads folder

    file_hash = get_file_hash(file_path)
    result = check_virus_total(file_hash)

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
