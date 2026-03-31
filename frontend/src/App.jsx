import React, { useState } from 'react'
import axios from 'axios'
import { AlertTriangle, CheckCircle2, Search, Info } from 'lucide-react'

function App() {
  const [text, setText] = useState('')
  const [loading, setLoading] = useState(false)
  const [result, setResult] = useState(null)
  const [error, setError] = useState(null)

  const handlePredict = async () => {
    if (!text.trim()) return
    
    setLoading(true)
    setError(null)
    setResult(null)
    
    try {
      // Assuming backend is running on localhost:8000
      const response = await axios.post('http://localhost:8000/predict', { text })
      setResult(response.data)
    } catch (err) {
      console.error(err)
      setError("Failed to connect to the analysis server. Please ensure the backend is running.")
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="container">
      <header>
        <h1>Veritas AI</h1>
        <p className="subtitle">Advanced Fake News Detection System</p>
      </header>

      <main>
        <div className="input-group">
          <label htmlFor="news-input">Enter news article or headline</label>
          <textarea
            id="news-input"
            placeholder="Paste the news content here for instant analysis..."
            value={text}
            onChange={(e) => setText(e.target.value)}
          />
        </div>

        <button 
          onClick={handlePredict} 
          disabled={loading || !text.trim()}
        >
          {loading ? "Analyzing..." : "Analyze Authenticity"}
        </button>

        {loading && (
          <div className="loader">
            <div className="spinner"></div>
          </div>
        )}

        {error && (
          <div className="result-card" style={{ background: 'rgba(239, 68, 68, 0.1)', color: '#ef4444', border: '1px solid rgba(239, 68, 68, 0.2)' }}>
            <p>{error}</p>
          </div>
        )}

        {result && (
          <div className={`result-card ${result.is_fake ? 'fake' : 'real'}`}>
            <div className="prediction-badge">
              {result.is_fake ? (
                <span style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                  <AlertTriangle size={18} /> Likely Deceptive
                </span>
              ) : (
                <span style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                  <CheckCircle2 size={18} /> Likely Reliable
                </span>
              )}
            </div>
            
            <p className="confidence-label">Confidence Score</p>
            <h2 className="confidence-value">{result.confidence}</h2>
            
            <p style={{ marginTop: '1.5rem', opacity: 0.8, fontSize: '0.9rem' }}>
              {result.is_fake 
                ? "This content contains linguistic patterns frequently associated with misinformation or fabricated news."
                : "This content aligns with patterns typically found in factual, verified news reports."}
            </p>
          </div>
        )}
      </main>

      <footer style={{ marginTop: '4rem', padding: '2rem', borderTop: '1px solid rgba(255, 255, 255, 0.05)' }}>
        <p style={{ color: '#64748b', fontSize: '0.8rem' }}>
          Powered by Scikit-Learn and Natural Language Processing.
          <br />
          Always cross-verify important information with multiple trusted sources.
        </p>
      </footer>
    </div>
  )
}

export default App
