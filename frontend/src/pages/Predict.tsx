import { useState } from "react";
import { usePredict } from "../hooks/usePredict";
import Loader from "../components/Loader";
import "../styles/predict.css";

function Predict() {
  const [text, setText] = useState("");
  const { predict, result, loading, error } = usePredict();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (text.trim().length > 0) {
      await predict(text);
    }
  };

  return (
    <div className="predict">
      <h1>🔎 Check News Authenticity</h1>
      <form onSubmit={handleSubmit}>
        <textarea
          placeholder="Paste news article text here..."
          value={text}
          onChange={(e) => setText(e.target.value)}
          rows={6}
        />
        <button type="submit" disabled={loading || !text.trim()}>
          {loading ? "Analyzing..." : "Check News"}
        </button>
      </form>

      {loading && <Loader />}
      {error && <p className="error">{error}</p>}

      {result && (
        <div className="result-card">
          <h2>Result</h2>
          <p>
            This news is:{" "}
            <span className={`label ${result.label.toLowerCase()}`}>
              {result.label}
            </span>
          </p>
          <p>Confidence: {(result.confidence * 100).toFixed(2)}%</p>
        </div>
      )}
    </div>
  );
}

export default Predict;
