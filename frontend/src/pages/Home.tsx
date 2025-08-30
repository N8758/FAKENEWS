import { Link } from "react-router-dom";
import "../styles/home.css";

function Home() {
  return (
    <div className="home">
      {/* Hero Section */}
      <h1>
        <span className="icon">📰</span> Fake News Detector
      </h1>
      <p className="tagline">
        Detect misinformation with the power of <b>AI</b>.  
        Paste any news article and find out instantly if it’s <b>FAKE</b> or <b>REAL</b>.
      </p>
      <Link to="/predict" className="btn">
        🚀 Try It Now
      </Link>

      {/* About Section */}
      <div className="about-tool">
        <h2>Why use Fake News Detector?</h2>
        <p>
          In today’s digital age, misinformation spreads faster than ever.  
          Our tool leverages <b>DistilBERT</b>, an advanced AI model,  
          to help you quickly check the credibility of any news content.  
        </p>
      </div>

      {/* Features Section */}
      <div className="features">
        <div className="feature-card">
          <h3>⚡ Fast</h3>
          <p>Get instant predictions in seconds with optimized AI models.</p>
        </div>
        <div className="feature-card">
          <h3>🤖 AI-Powered</h3>
          <p>Built using <b>Transformers</b> & <b>PyTorch</b> for state-of-the-art NLP.</p>
        </div>
        <div className="feature-card">
          <h3>🎯 Accurate</h3>
          <p>Fine-tuned on fake/real news datasets for reliable results.</p>
        </div>
      </div>
    </div>
  );
}

export default Home;
