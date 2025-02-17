# C0d3rs_Wh0
# *Authenica - Secure URL Shortener & Link Safety Checker*  

🔗 *Authenica* is a security-focused URL shortener that ensures user safety by checking links and uploaded files for potential threats. It integrates *Google Safe Browsing* to verify URLs and *VirusTotal API* to scan uploaded files, making it an all-in-one security solution for users.  

---

## *🚀 Features*
✔️ *URL Shortening* – Convert long URLs into short, easy-to-share links  
✔️ *Link Safety Verification* – Check if a link is flagged as malicious or unsafe  
✔️ *File Upload Safety Check* – Scan uploaded files for malware using VirusTotal API  
✔️ *User-Friendly Interface* – Clean and responsive UI for smooth navigation  
✔️ *Fast & Lightweight* – Powered by Python Flask for quick responses  

---

## *🛠 Tech Stack*  
| Component  | Technology Used  |
|------------|----------------|
| **Frontend**  | HTML, CSS, JavaScript  |
| **Backend**  | Python (Flask)  |
| **APIs Used**  | Google Safe Browsing, VirusTotal API  |
| **Database**  | Dictionary-based storage for shortened links  |
| **Hosting**  | Localhost / Flask development server  |

---

## *📂 Project Structure*  

```
/authenica
│── /templates
│   ├── linkverify.html     # Frontend UI for link verification
│── /static
│   ├── styles.css          # Styles for UI
│── /uploads                # Folder to store uploaded files temporarily
│── linkshortener.py        # URL shortener logic
│── check.py                # URL safety checker using Google Safe Browsing API
│── verify.py               # API endpoint for checking URL safety
│── check2.py               # File upload and VirusTotal scanning logic
│── README.md               # Project documentation
│── requirements.txt        # Dependencies
│── app.py                  # Main Flask app (if combined)
```

---

## *⚙️ Installation & Setup*  

### *1️⃣ Clone the Repository*  
```bash
git clone https://github.com/your-username/authenica.git
cd authenica
```

### *2️⃣ Install Dependencies*  
```bash
pip install flask requests
```

### *3️⃣ Configure API Keys*  
- Get a **Google Safe Browsing API key** [here](https://developers.google.com/safe-browsing/)  
- Get a **VirusTotal API key** [here](https://developers.virustotal.com/)  


### *4️⃣ * 
#### *Option 1: Run URL Shortener*
```bash
python linkshortener.py
```
#### *Option 2: Run URL Checker*
```bash
python check.py
```
#### **Option 3: Run File Safety Scanner**
```bash
python check2.py
```
---

## *📌 API Endpoints*

| Endpoint  | Method | Description  |
|------------|--------|--------------|
| `/check-url` | POST  | Checks if a given URL is safe or malicious |
| `/upload` | POST  | Uploads and scans a file for malware |
| `/shorten` | GET/POST  | Generates a short link for a given URL |
| `/redirect/<short_code>` | GET  | Redirects to the original URL |

---

## *🖥️ Usage Guide*

### **🔗 URL Shortener**
1. Enter the long URL in the input field 
2. Click **"Shorten"** to generate a short link 
3. Copy the generated short link and share it 

### *🔍 URL Safety Checker*
1. Paste a URL into the input field
2. Click **"Check URL"** 
3. If the URL is **unsafe**, it will show a red warning
### *🛡️ File Safety Scanner*
1. Select a file to upload 
2. Click **"Upload & Scan"** 
3. If the file contains malware, it will display a warning 

---

## *🚧 Known Issues & Future Improvements*
- **🔹 URL Expiry:** Add expiration time for shortened links 
- **🔹 Database Integration:** Store URLs persistently using SQLite or MongoDB 
- **🔹 Enhanced UI:** Improve styling and mobile responsiveness 

---

## *👥 Contributors*
- **Hardik Runwal** 
- **Mohammad Arsh**
- **Jujhar Singh**
- **Kedas Siri Sahiti**
- **Giridhar Sreekumar**
---
