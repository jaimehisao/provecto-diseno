import React from "react";
import UserProfile from "./UserProfile";
import "./App.css";
import { Link } from "react-router-dom";
import { useEffect, useState } from "react";

const Login = () => {
	const [username, setUsername] = React.useState("");

	const win = window.sessionStorage;

	function handleSubmit() {
		sessionStorage.setItem("username", username);
		sessionStorage.setItem("logged", true);
		window.location.href = "/";
	}

	useEffect(() => {
		if (win.getItem("username")) {
			setUsername(win.getItem("username"));
		}
	}, []);

	useEffect(() => {
		win.setItem("username", username);
	}, [username]);

	return (
		<div className="login__container">
			<h1>Log in</h1>
			<form>
				<p className="input__label">
					<label htmlFor="username">Enter your username:</label>
				</p>
				<input
					type="text"
					placeholder="username"
					className="username__input"
					value={username}
					onChange={(e) => setUsername(e.target.value)}
				/>
				<Link to="/">
					<button
						type="submit"
						className="login__button"
						onClick={handleSubmit}
					>
						Log in
					</button>
				</Link>
			</form>
		</div>
	);
};

export default Login;
