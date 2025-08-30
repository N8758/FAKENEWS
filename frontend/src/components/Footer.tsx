import "../styles/footer.css";

function Footer() {
  return (
    <footer>
      <div className="container">
        <p>
          © {new Date().getFullYear()} Fake News Detector. Built with ❤️ using
          React + FastAPI + DistilBERT.
        </p>
      </div>
    </footer>
  );
}

export default Footer;
