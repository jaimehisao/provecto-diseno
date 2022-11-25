import React from "react";
import "./App.css";
import image from "./assets/logo.png";
import { Link } from "react-router-dom";

class Footer extends React.Component {
	render() {
		return (
			<div className="footer">
				<div className="footer__wrapper">
					<Link to="/upload">
						<button className="upload">Upload an Image</button>
					</Link>
				</div>
			</div>
		);
	}
}

export default Footer;
