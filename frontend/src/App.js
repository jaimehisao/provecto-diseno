import React from "react";
import "./App.css";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Navbar from "./Navbar";
import Home from "./Home";
import User from "./User";
import Post from "./Post";
import Login from "./Login";
import Footer from "./Footer";
import Upload from "./Upload";

import UserProfile from "./UserProfile";

class App extends React.Component {
	render() {
		if (sessionStorage.getItem("logged") === "true") {
			this.footer = <Footer />;
		} else {
			this.footer = null;
		}

		return (
			<Router>
				<div className="app">
					<div className="app__header">
						<Navbar />
					</div>
					<div className="app__body">
						<Routes>
							<Route path="/" element={<Home />} />
							{/* <Route path="/user" element={<User />} /> */}
							<Route path="/post" element={<Post />} />
							<Route path="/login" element={<Login />} />
							<Route path="/upload" element={<Upload />} />
						</Routes>
					</div>

					{this.footer}
				</div>
			</Router>
		);
	}
}

export default App;
