from pymongo import MongoClient

from dto.post import Post
from dto.comment import Comment

client = MongoClient('mongo', 27017)

post_db = client['posts']
user_db = client['users']


def get_user(user_id: str):
    return user_db.users.find_one({"user_id": user_id})


def get_user_posts(user_id: str):
    return post_db.find_all({"user_id": user_id})


def get_post_by_id(post_id: str):
    return post_db.find_one({"id": post_id})


def create_new_post(post: Post):
    return post_db.insert_one(post)


def create_new_comment_in_post(post: Post, comment: Comment):
    post.comments.append(comment)
    return post_db.update_one({"id": post.id}, post)


def like_post(post_id):
    post = post_db.find_one({"id": post_id})
    # case where post not found
    post['likes'] = post['likes']+1
    post['liked_by'].append("NONE")  # TODO append user id of person that like the post
    post_db.update_one({"id": post.id}, post)


def unlike_post(post_id):
    post = post_db.find_one({"id": post_id})
    # TODO pop user from list
    post['likes'] = post['likes'] + 1
    post_db.update_one({"id": post.id}, post)


def create_new_comment(post_id, comment: Comment):
    post = post_db.find_one({"id": post_id})
    # case where post not found
    post['comment'].append(comment)
