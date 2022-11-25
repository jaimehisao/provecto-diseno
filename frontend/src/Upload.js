import React from "react";
import "./App.css";
import image from "./assets/logo.png";
import { Link } from "react-router-dom";

class Upload extends React.Component {
	render() {
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
						/>
						<textarea
							name="description"
							id="description"
							cols="30"
							rows="10"
							placeholder="Enter a description..."
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
						/>
					</form>
				</div>
			</div>
		);
	}
}

export default Upload;
