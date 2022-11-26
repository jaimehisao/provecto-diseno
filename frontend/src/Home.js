import React from "react";
import "./App.css";
import heart from "./assets/heart.svg";
import heart_filled from "./assets/heart_filled.svg";
import { useNavigate } from "react-router-dom";

import Axios from "axios";

const client = Axios.create({
	baseURL: "http://localhost:4000",
});

function Home() {
	const nav = useNavigate();
	const [posts, setPosts] = React.useState([]);
	// const [comments, setComments] = React.useState([]);
	const [postid, setPostid] = React.useState(0);

	React.useEffect(() => {
		client.get("/posts").then((res) => {
			setPosts(res.data);
		});
	}, []);

	// const get_image = (image) => {
	// 	Axios.get("http://localhost:4000/post/image/" + image, {
	// 		responseType: "arraybuffer",
	// 	}).then((res) => {
	// 		const base64 = btoa(new Uint8Array(res.data).reduce(""));
	// 		// return setImage(base64);
	// 	});
	// };

	const [comment, setComment] = React.useState("");

	const handleCommentChange = (e) => {
		setComment(e.target.value);
		setPostid(e.target.id);
	};

	const handleSubmit = (e) => {
		e.preventDefault();
		addComment(sessionStorage.getItem("username"), comment, postid);
		nav("/");
	};

	const addComment = (user, body, postId) => {
		Axios({
			method: "post",
			url: "http://localhost:4000/post/comments/add",
			data: {
				comment_body: body,
				user_id: user,
				post_id: postId,
			},
		});
	};

	const handleLike = (e, postid) => {
		e.preventDefault();
		likePost(postid);
		// console.log(e.target.id);
		nav("/");
	};

	const likePost = (post_id) => {
		Axios({
			method: "post",
			url: "http://localhost:4000/post/like/" + post_id,
		});
	};

	return (
		<div className="home">
			{posts.map((post) => {
				return (
					<div className="post" key={post.id}>
						<div className="post__header">
							<img
								src={require("./assets/avatar.png")}
								className="post__avatar"
								alt="avatar"
							/>
							<p className="post__user">{post.user_id}</p>
						</div>

						<img
							src={
								"http://localhost:4000/post/image/" +
								post.image_path
							}
							className="post__image"
							alt="post"
						/>
						<div className="post__footer">
							<div className="likes">
								<button
									className="likes__icon"
									onClick={(e) => {
										handleLike(e, post.id);
									}}
									id={post.id}
									key={post.id}
								>
									<img
										src={heart}
										className="likes__icon"
										alt="likes"
									/>
								</button>
								<p className="likes__count">
									{post.likes} Likes
								</p>
							</div>
							<p className="post__description">{post.body}</p>

							<div className="post__comments">
								{/* <p className="comments__count">5 Comments</p> */}
								{post.comments.map((comment) => {
									return (
										<div
											className="comment"
											key={comment.id}
										>
											<div className="commenter">
												{comment.user_id}
											</div>
											<p>{comment.body}</p>
										</div>
									);
								})}
								<div className="comment__form">
									<form>
										<input
											type="text"
											placeholder="Add a comment..."
											name={"body_" + post.id}
											onChange={handleCommentChange}
											id={post.id}
										/>
										<input
											type="submit"
											value="Post"
											onClick={handleSubmit}
										/>
									</form>
								</div>
							</div>
						</div>
					</div>
				);
			})}

			{/* <div className="post">
				<div className="post__header">
					<img
						src={require("./assets/test.jpg")}
						className="post__avatar"
						alt="avatar"
					/>
					<p className="post__user">username01</p>
				</div>

				<img
					src={require("./assets/test.jpg")}
					className="post__image"
					alt="post"
				/>
				<div className="post__footer">
					<div className="likes">
						<img src={heart} className="likes__icon" alt="likes" />
						<p className="likes__count">100 Likes</p>
					</div>
					<p className="post__description">
						This is the post description! Lorem ipsum dolor sit
						amet, consectetur adipiscing elit, sed do eiusmod tempor
						incididunt ut labore et dolore magna aliqua. Amet purus
						gravida quis blandit turpis cursus in. Nibh cras
						pulvinar mattis nunc sed blandit libero volutpat. Urna
						nec tincidunt praesent semper. Non tellus orci ac auctor
						augue mauris augue neque gravida. Sodales ut eu sem
						integer vitae justo eget magna. Elit at imperdiet dui
						accumsan sit amet nulla. Sapien pellentesque habitant
						morbi tristique. In nulla posuere sollicitudin aliquam
						ultrices sagittis. Ultrices gravida dictum fusce ut
						placerat orci nulla. Dis parturient montes nascetur
						ridiculus mus mauris vitae. Nisl vel pretium lectus
						quam. Accumsan sit amet nulla facilisi. Feugiat
						scelerisque varius morbi enim nunc faucibus a.
						Suspendisse potenti nullam ac tortor vitae purus. Libero
						volutpat sed cras ornare arcu dui vivamus arcu. Quam
						adipiscing vitae proin sagittis nisl rhoncus. Nisl nisi
						scelerisque eu ultrices. Amet commodo nulla facilisi
						nullam vehicula ipsum a arcu. Magna fringilla urna
						porttitor rhoncus dolor purus non enim.
					</p>

					<div className="post__comments">
						<p className="comments__count">5 Comments</p>

						<div className="comment">
							<Link to="/user">
								<div className="commenter">user02</div>
							</Link>
							<p>this is a comment 1</p>
						</div>

						<Link to="/post#comments">
							<div className="more_comments">
								<p>View all comments</p>
							</div>
						</Link>

						<div className="comment__form">
							<form>
								<input
									type="text"
									placeholder="Add a comment..."
								/>
								<input type="submit" value="Post" />
							</form>
						</div>
					</div>
				</div>
			</div> */}
		</div>
	);
}

export default Home;
