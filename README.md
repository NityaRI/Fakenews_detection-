# Veritas AI: Fake News Detection Prototype

Veritas AI is a sophisticated, full-stack web application designed to demonstrate the power of Machine Learning in identifying potential misinformation in news articles. This project serves as a **functional prototype** and educational tool for Natural Language Processing (NLP) based classification.

---

## 🎯 Project Vision
In an era of information overload, Veritas AI aims to provide a first line of defense against misinformation. By analyzing linguistic patterns and word frequencies, the application offers an immediate probability score to help users gauge the reliability of their news source.

---

## 🏗️ Architecture Overview
The project follows a decoupled, three-tier architecture:
1. **Frontend (React + Vite)**: A responsive, high-performance user interface focused on UX/UI best practices.
2. **Backend (FastAPI)**: A lightweight but powerful Python-based API designed for low-latency inference.
3. **ML Engine (Scikit-Learn)**: A robust pipeline leveraging TF-IDF (Term Frequency-Inverse Document Frequency) and Logistic Regression.

---

## 🛠️ Technology Stack
### Frontend
- **Framework**: [React](https://reactjs.org/) (built with Vite for speed)
- **Styling**: Vanilla CSS3 using **Glassmorphism** and **Dynamic CSS Gradients**
- **Icons**: [Lucide-React](https://lucide.dev/)
- **Communication**: [Axios](https://axios-http.com/)

### Backend & ML
- **API Framework**: [FastAPI](https://fastapi.tiangolo.com/)
- **Server**: Uvicorn
- **Development**: Python 3.10+
- **Machine Learning**: Scikit-Learn, Pandas, Numpy

---

## 🧠 The NLP Pipeline
Veritas AI uses a standard but effective classification workflow:
1. **Vectorization (TF-IDF)**: Converts raw text into numerical values, weighing words by their importance and frequency across the dataset.
2. **Inference (Logistic Regression)**: A mathematical model that calculates the probability of an article being "Real" vs "Fake" based on those word weights.
3. **Calibration**: For this prototype, the confidence scores are tuned for demonstration purposes.

---

## 📊 Prototype Dataset
The model is currently trained on a curated synthetic dataset of 60 examples.

### Real News Examples (Training Set)
*Focuses on factual, formal reporting on politics, science, and economy.*
-   "The Federal Reserve chair announced a slight increase in interest rates..."
-   "NASA successfully landed its Falcon 9 rocket on a drone ship..."
-   "Economic analysts suggest that the tech sector will lead the market recovery..."

### Fake News Examples (Training Set)
*Focuses on sensationalist, conspiratorial, and "clickbait" style language.*
-   "Secret government files reveal that the moon landing was filmed in a basement."
-   "Drinking lemon juice every morning will grant you the ability to speak to dolphins."
-   "The government is secretly replacing all birds with high-tech drones."

*(Refer to `backend/train_model.py` for the complete list of 60 items.)*

---

## 🚀 Getting Started

### Prerequisites
- Node.js (v18+)
- Python (3.10+)

### Setup Instructions
1. Navigate to the project root:
   ```powershell
   cd FakeNewsDetectionApp
   ```
2. Run the automated startup script:
   ```powershell
   ./start.ps1
   ```

### Training Your Own Data
To upgrade this from a prototype to a real-world tool:
1. Replace the dataset in `backend/train_model.py` with 10,000+ real samples from sources like Kaggle.
2. Re-train:
   ```powershell
   cd backend
   python train_model.py
   ```

---

## 🔮 Roadmap & Future Scope
- [ ] **Live URL Scraping**: Analyze news directly from a link using BeautifulSoup or Playwright.
- [ ] **Transformer Models**: Upgrade to BERT or GPT-based embeddings for deeper contextual understanding.
- [ ] **Deep Learning**: Implementation of LSTM/RNN for sequential text analysis.
- [ ] **Multi-language Support**: Expanding verification to diverse languages.

---

## ⚖️ License
This project is for educational and prototype purposes only.
