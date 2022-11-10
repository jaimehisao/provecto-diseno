import React from "react";
import "./App.css";
import image from "./assets/logo.png";
import { Link } from "react-router-dom";

function Navbar() {
  return (
    <div className="app__headerWrapper">
    
    <Link to="/">
        <img src={image}
        alt="Exchange-o-gram Logo"
        />
    
    </Link>
    <div className="app__headerButtons">
    <button className="primary__button">Log in</button>
    <button className="text__button">Sign up</button>
    </div>
    </div>
    
  );
}

export default Navbar;
