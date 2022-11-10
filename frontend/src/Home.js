import React from "react";
import "./App.css";
import heart from "./assets/heart.svg";
import heart_filled from "./assets/heart_filled.svg";
import { Link } from "react-router-dom";

function Home() {
  return (
    
    <div className="post">
      <div className="post__header">
        <Link to="/user">
          <img src={require("./assets/test.jpg")} className="post__avatar" alt="avatar" />
          <p className="post__user">username01</p>
        </Link>
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
            <Link to="/user">
              <div className="commenter">
                user02
              </div>
            </Link>
            <p>
              this is a comment 1
            </p>
          </div>

          <Link to="/post#comments">
            <div className="more_comments">
              <p>View all comments</p>
            </div>
          </Link>

          <div className="comment__form">
            <form>
              <input type="text" placeholder="Add a comment..." />
              <input type="submit" value="Post" />
            </form>
          </div>
        
        </div>
      </div>
    </div>

  );
}

export default Home;
