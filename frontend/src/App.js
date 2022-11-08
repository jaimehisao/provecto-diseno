import React from "react";
import "./App.css";
import image from "./assets/logo.png";
import heart from "./assets/heart.svg";
import heart_filled from "./assets/heart_filled.svg";
import { Link, Route, Routes } from "react-router-dom";

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

    <div className="app__body">

    <div className="post">
    <div className="post__header">
    <img src={require("./assets/test.jpg")} className="post__avatar" alt="avatar" />
    <p className="post__user">username01</p>
    </div>

    <img src={require("./assets/test.jpg")} className="post__image" alt="post" />
    <div className="post__footer">
    <div className="likes">
    <img src={heart} className="likes__icon" alt="likes" />
    <p className="likes__count">100 Likes</p>
    </div>
    <p className="post__description">This is the post description! Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Amet purus gravida quis blandit turpis cursus in. Nibh cras pulvinar mattis nunc sed blandit libero volutpat. Urna nec tincidunt praesent semper. Non tellus orci ac auctor augue mauris augue neque gravida. Sodales ut eu sem integer vitae justo eget magna. Elit at imperdiet dui accumsan sit amet nulla. Sapien pellentesque habitant morbi tristique. In nulla posuere sollicitudin aliquam ultrices sagittis. Ultrices gravida dictum fusce ut placerat orci nulla. Dis parturient montes nascetur ridiculus mus mauris vitae. Nisl vel pretium lectus quam. Accumsan sit amet nulla facilisi. Feugiat scelerisque varius morbi enim nunc faucibus a. Suspendisse potenti nullam ac tortor vitae purus. Libero volutpat sed cras ornare arcu dui vivamus arcu. Quam adipiscing vitae proin sagittis nisl rhoncus. Nisl nisi scelerisque eu ultrices. Amet commodo nulla facilisi nullam vehicula ipsum a arcu. Magna fringilla urna porttitor rhoncus dolor purus non enim.</p>
    
    <div className="post__comments">
    <p className="comments__count">5 Comments</p>

    <div className="comment">
    <div className="commenter">
    user02
    </div>
    <p>
    this is a comment 1 incididunt ut labore et dolore magna aliqua. Amet purus gravida quis blandit turpis cursus in. Nibh cras pulvinar mattis nunc sed blandit libero volutpat. Urna nec tincidunt praesent semper. Non tellus orci ac auctor augue mauris augue neque gravida. Sodales ut eu sem integer vitae justo
    </p>
    </div>
    
    <div className="comment">
    <div className="commenter">
    user02
    </div>
    <p>
    this is a comment 1
    </p>
    </div>
    
    <div className="comment">
    <div className="commenter">
    user02
    </div>
    <p>
    this is a comment 1
    </p>
    </div>

    <div className="more_comments">
    <p>View all comments</p>
    </div>

    <div className="comment__form">
    <form>
    <input type="text" placeholder="Add a comment..." />
    <input type="submit" value="Post" />
    </form>
    </div>
    
    </div>
    </div>
    </div>

    <div className="post">
    <div className="post__header">
    <img src={require("./assets/test.jpg")} className="post__avatar" alt="avatar" />
    <p className="post__user">username01</p>
    </div>

    <img src={require("./assets/test.jpg")} className="post__image" alt="post" />
    <div className="post__footer">
    <div className="likes">
    <img src={heart_filled} className="likes__icon" alt="likes" />
    <p className="likes__count">100 Likes</p>
    </div>
    <p className="post__description">This is the post description! Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Amet purus gravida quis blandit turpis cursus in. Nibh cras pulvinar mattis nunc sed blandit libero volutpat. Urna nec tincidunt praesent semper. Non tellus orci ac auctor augue mauris augue neque gravida. Sodales ut eu sem integer vitae justo eget magna. Elit at imperdiet dui accumsan sit amet nulla. Sapien pellentesque habitant morbi tristique. In nulla posuere sollicitudin aliquam ultrices sagittis. Ultrices gravida dictum fusce ut placerat orci nulla. Dis parturient montes nascetur ridiculus mus mauris vitae. Nisl vel pretium lectus quam. Accumsan sit amet nulla facilisi. Feugiat scelerisque varius morbi enim nunc faucibus a. Suspendisse potenti nullam ac tortor vitae purus. Libero volutpat sed cras ornare arcu dui vivamus arcu. Quam adipiscing vitae proin sagittis nisl rhoncus. Nisl nisi scelerisque eu ultrices. Amet commodo nulla facilisi nullam vehicula ipsum a arcu. Magna fringilla urna porttitor rhoncus dolor purus non enim.</p>
    
    <div className="post__comments">
    <p className="comments__count">5 Comments</p>

    <div className="comment">
    <div className="commenter">
    user02
    </div>
    <p>
    this is a comment 1 incididunt ut labore et dolore magna aliqua. Amet purus gravida quis blandit turpis cursus in. Nibh cras pulvinar mattis nunc sed blandit libero volutpat. Urna nec tincidunt praesent semper. Non tellus orci ac auctor augue mauris augue neque gravida. Sodales ut eu sem integer vitae justo
    </p>
    </div>
    
    <div className="comment">
    <div className="commenter">
    user02
    </div>
    <p>
    this is a comment 1
    </p>
    </div>
    
    <div className="comment">
    <div className="commenter">
    user02
    </div>
    <p>
    this is a comment 1
    </p>
    </div>

    <div className="more_comments">
    <p>View all comments</p>
    </div>

    <div className="comment__form">
    <form>
    <input type="text" placeholder="Add a comment..." />
    <input type="submit" value="Post" />
    </form>
    </div>
    
    </div>
    </div>
    </div>

    </div>




    </div>
    
  );
}

export default App;
