from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

# Replace with your Google Safe Browsing API Key
API_KEY = "AIzaSyCvS2PzTBT48qt7v-g76FbS8KU3wWhYGCw"
API_URL = f"https://safebrowsing.googleapis.com/v4/threatMatches:find?key={API_KEY}"

def check_url_safety(url):
    payload = {
        "client": {"clientId": "yourapp", "clientVersion": "1.0"},
        "threatInfo": {
            "threatTypes": ["MALWARE", "SOCIAL_ENGINEERING", "UNWANTED_SOFTWARE"],
            "platformTypes": ["ANY_PLATFORM"],
            "threatEntryTypes": ["URL"],
            "threatEntries": [{"url": url}]
        }
    }
    response = requests.post(API_URL, json=payload)
    result = response.json()

    if "matches" in result:
        return {"status": "Unsafe", "message": "This URL is flagged as unsafe!"}
    return {"status": "Safe", "message": "This URL is safe."}


@app.route('/')
def hello_world():
    return render_template("linkverify.html")

@app.route('/check-url', methods=['POST'])
def check_url():
    data = request.json
    url = data.get("url")

    if not url:
        return jsonify({"error": "No URL provided"}), 400

    result = check_url_safety(url)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
