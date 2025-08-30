# 📰 Fake News Detector

An **AI-powered Fake News Detection App** that analyzes news articles and predicts whether they are **FAKE** or **REAL** using **DistilBERT**, a state-of-the-art NLP model from Hugging Face.

---

## 🚀 Features

- 🔎 **AI-Powered Detection** → Uses DistilBERT for text classification  
- ⚡ **Fast & Lightweight** → Optimized inference with FastAPI backend  
- 🎨 **Modern UI** → React + TypeScript frontend with clean dark theme  
- 📊 **Confidence Score** → Shows probability with FAKE/REAL labels  
- 🌍 **Deployed Live** → Access from any browser, no setup required  

---

## 🛠 Tech Stack

**Frontend**
- React (Vite + TypeScript)
- React Router
- Vanilla CSS (Black/White theme)

**Backend**
- FastAPI (Python)
- Uvicorn (ASGI server)
- Pydantic for validation

**AI / ML**
- Hugging Face Transformers
- DistilBERT (distilbert-base-uncased)
- PyTorch

**Deployment**
- Render (Backend API & Frontend Static Site)

---

## 📸 Screenshots

### 🔹 Home Page
Modern landing page with AI-powered tagline and CTA.

### 🔹 Predict Page
Paste any news article → AI classifies FAKE / REAL with confidence score.

### 🔹 About Page
Info about project, tech stack (clickable badges → official docs), and author.

---

## ▶️ Run Locally

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/fake-news-app.git
cd fake-news-app
````

### 2️⃣ Backend (FastAPI)

```bash
cd backend
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate  # Mac/Linux

pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

API will run at → `http://localhost:8000`

---

### 3️⃣ Frontend (React + Vite)

```bash
cd frontend
npm install
npm run dev
```

Frontend will run at → `http://localhost:5173`

---

## 🌍 Deployment

### Backend

* Hosted on **Render** as a Python Web Service
* Start Command:

  ```bash
  uvicorn app.main:app --host 0.0.0.0 --port 8000
  ```

### Frontend

* Hosted on **Render (Static Site)**
* Build Command:

  ```bash
  npm install && npm run build
  ```
* Publish Directory: `dist`
* Environment Variable:

  ```bash
  VITE_API_URL=https://<your-backend-url>/api/v1
  ```

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!
Feel free to open a Pull Request.

---

## 👨‍💻 Author

**Developed by [Nilesh Pulate 🚀](https://github.com/<your-username>)**
Passionate about **AI, Full Stack Development, and Cybersecurity**.

---

## ⭐ Support

If you like this project, don’t forget to **star ⭐ the repo**.

```

---

# 🔹 Why this is the “best”
- ✅ Explains **what the project is**  
- ✅ Lists **features & tech stack**  
- ✅ Shows **setup instructions** step-by-step  
- ✅ Has **deployment guide**  
- ✅ Credits **you (Nilesh Pulate 🚀)**  

