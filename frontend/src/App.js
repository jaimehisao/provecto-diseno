import React from "react";
import "./App.css";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Navbar from "./Navbar";
import Home from "./Home";
import User from "./User";
import Post from "./Post";

function App() {
  return (
    <Router>
      <div className="app">
        <div className="app__header">
          <Navbar />
        </div>
        
        <div className="app__body">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/user" element={<User />} />
            <Route path="/post" element={<Post />} />
          </Routes>
        </div>
      </div>
    </Router>
    
  );
}

export default App;
