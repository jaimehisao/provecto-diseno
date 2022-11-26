import React from "react";
import "./App.css";
import image from "./assets/logo.png";
import { Link, useNavigate } from "react-router-dom";

import Axios from "axios";

function Upload() {
	const nav = useNavigate();
	const [body, setBody] = React.useState("");

	const handleBodyChange = (e) => {
		setBody(e.target.value);
	};

	const [image, setImage] = React.useState("");

	const handleImageChange = (e) => {
		setImage(e.target.value);
	};

	const handleSubmit = (e) => {
		e.preventDefault();
		uploadPost(sessionStorage.getItem("username"), body);
		postImage();
		nav("/");
	};

	const uploadPost = (user, body) => {
		var imgFile = document.getElementById("file").files[0];
		var filename = imgFile.name;

		Axios({
			method: "post",
			url: "http://localhost:4000/post/new",
			data: {
				user_id: user,
				body: body,
				image_name: filename,
			},
		});
	};

	const postImage = () => {
		var img = new FormData();
		var imgFile = document.getElementById("file").files[0];
		img.append("file", imgFile);
		// Axios({
		// 	method: "post",
		// 	url: "http://localhost:4000/post/new/image",
		// 	body: {
		// 		image: img,
		// 	},
		// });
		var xhr = new XMLHttpRequest();
		xhr.open("POST", "http://localhost:4000/post/new/image");
		xhr.setRequestHeader("Access-Control-Allow-Origin", "*");
		xhr.send(img);
	};

	return (
		<div className="upload__page">
			<div className="upload__wrapper">
				<form className="upload__form">
					<h1>Upload an image</h1>
					<label for="file" className="file__input">
						Click to choose an image...
					</label>
					<input
						type="file"
						name="file"
						id="file"
						className="inputfile"
						onChange={handleImageChange}
					/>
					<textarea
						name="description"
						id="description"
						cols="30"
						rows="10"
						placeholder="Enter a description..."
						onChange={handleBodyChange}
					></textarea>
					{/* <input
						type="textarea"
						name="description"
						id="description"
						placeholder="Description"
					/> */}
					<Link to="/">
						<button className="cancel__button">Cancel</button>
					</Link>
					<input
						type="submit"
						value="Upload"
						className="primary__button"
						onClick={handleSubmit}
					/>
				</form>
			</div>
		</div>
	);
}

export default Upload;
