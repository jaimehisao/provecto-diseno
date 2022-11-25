from pymongo import MongoClient

from dto.post import Post
from dto.comment import Comment

import logging

client = MongoClient('mongo', 27017)

post_db = client['posts']
user_db = client['users']


def get_user(user_id: str):
    logging.info("Getting user with id: " + user_id)
    return user_db.users.find_one({"user_id": user_id})


def get_user_posts(user_id: str):
    logging.info("Getting posts from user with id: " + user_id)
    return post_db.find_all({"user_id": user_id})


def get_post_by_id(post_id: str):
    logging.info("Getting post with id: " + post_id)
    post = post_db.find_one({"id": post_id})
    post = Post(post_id=post['id'],
                body=post['body'],
                image_path=post['image'],
                user_id=post['user_id'],
                created_at=post['created_at'])
    return post


def create_new_comment_in_post(post: Post, comment: Comment):
    logging.info("Creating new comment in post with id: " + str(post.id))
    post.comments.append(comment)
    return post_db.update_one({"id": post.id}, post)


def like_post(post_id):
    logging.info("Liking post with id: " + post_id)
    post = post_db.find_one({"id": post_id})
    # case where post not found
    post['likes'] = post['likes']+1
    post_db.update_one({"id": post.id}, post)


def unlike_post(post_id):
    logging.info("Unliking post with id: " + post_id)
    post = post_db.find_one({"id": post_id})
    if post['likes'] > 0:
        post['likes'] = post['likes'] - 1
        post_db.update_one({"id": post.id}, post)
        return
    logging.info("Post has no likes")


def create_new_comment(post_id, comment: Comment):
    logging.info("Creating new comment in post with id: " + post_id)
    post = post_db.find_one({"id": post_id})
    # case where post not found
    post['comment'].append(comment)


"""
def create_new_post(post: Post):
    logging.info("Creating new post")
    return post_db.insert_one(post)


def delete_post(post_id: str):
    logging.info("Deleting post with id: " + post_id)
    # TODO validate post ownership
    post_db.delete_one({"id": post_id})
"""
