import "../styles/about.css";

function About() {
  return (
    <div className="about">
      <h1>ℹ️ About This Project</h1>
      <p>
        This project uses <b>DistilBERT</b>, a lightweight Transformer model,
        fine-tuned for fake news classification. It analyzes news articles and
        predicts whether they are <b>FAKE</b> or <b>REAL</b>.
      </p>

      <h2>🛠 Tech Stack</h2>
      <div className="tech-stack">
        <a href="https://react.dev/" target="_blank" rel="noopener noreferrer">React</a>
        <a href="https://www.typescriptlang.org/" target="_blank" rel="noopener noreferrer">TypeScript</a>
        <a href="https://fastapi.tiangolo.com/" target="_blank" rel="noopener noreferrer">FastAPI</a>
        <a href="https://www.python.org/" target="_blank" rel="noopener noreferrer">Python</a>
        <a href="https://huggingface.co/transformers/" target="_blank" rel="noopener noreferrer">Transformers</a>
        <a href="https://pytorch.org/" target="_blank" rel="noopener noreferrer">PyTorch</a>
        <a href="https://huggingface.co/distilbert-base-uncased" target="_blank" rel="noopener noreferrer">DistilBERT</a>
      </div>

      <div className="author">
        <p>👨‍💻 Developed by <b>Nilesh Pulate 🚀</b></p>
      </div>
    </div>
  );
}

export default About;
