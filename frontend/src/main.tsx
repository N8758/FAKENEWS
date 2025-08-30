import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";

// React 18 entry point
ReactDOM.createRoot(document.getElementById("root") as HTMLElement).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
