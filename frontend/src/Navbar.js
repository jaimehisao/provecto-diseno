import React from "react";
import "./App.css";
import image from "./assets/logo.png";
import { Link } from "react-router-dom";

class Navbar extends React.Component {
	// getLogged = () => {
	// 	return this.state.logged;
	// };

	handleLogout = () => {
		sessionStorage.setItem("logged", false);
		sessionStorage.setItem("username", "");
		window.location.href = "/";
	};

	render() {
		if (sessionStorage.getItem("username") !== "") {
			return (
				<div className="app__headerWrapper">
					<Link to="/">
						<img src={image} alt="Exchange-o-gram Logo" />
					</Link>

					<div className="app__headerButtons">
						<p className="username__header">
							{sessionStorage.getItem("username")}
						</p>
						<button
							className="primary__button"
							onClick={this.handleLogout}
						>
							Log Out
						</button>
					</div>
				</div>
			);
		} else {
			return (
				<div className="app__headerWrapper">
					<Link to="/">
						<img src={image} alt="Exchange-o-gram Logo" />
					</Link>

					<div className="app__headerButtons">
						<Link to="/login">
							<button className="primary__button">Log in</button>
						</Link>
					</div>
				</div>
			);
		}
	}
}

export default Navbar;
