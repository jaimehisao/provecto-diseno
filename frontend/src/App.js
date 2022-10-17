import React from "react";
import "./App.css";
import image from "./assets/logo.png";

function App() {
  return (
    <div className="app">
    <div className="app__header">
    <div className="app__headerWrapper">
    <img src={image}
    alt="Exchange-o-gram Logo"
    />
    <div className="app__headerButtons">
    <button className="primary__button">Log in</button>
    <button className="text__button">Sign up</button>
    </div>
    </div>
    </div>
    </div>
  );
}

export default App;
