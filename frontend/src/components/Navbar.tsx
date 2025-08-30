import { Link } from "react-router-dom";
import "../styles/navbar.css";

function Navbar() {
  return (
    <nav>
      <div className="container">
        {/* Logo / App Name */}
        <Link to="/" className="logo">
          📰 Fake News Detector
        </Link>

        {/* Navigation Links */}
        <div className="links">
          <Link to="/">Home</Link>
          <Link to="/predict">Predict</Link>
          <Link to="/about">About</Link>
        </div>
      </div>
    </nav>
  );
}

export default Navbar;
