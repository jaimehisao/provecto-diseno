from pymongo import MongoClient

from dto.post import Post
from dto.comment import Comment

import logging

client = MongoClient("localhost", 27017)
# client = MongoClient('mongo', 27017)
# database
database = client["exchangeagram"]
post_db = database["posts"]
user_db = database["users"]


def convert_post_to_dict(post: Post):
    new_comments = []
    for comment in post.comments:
        new_comments.append(comment.dict())
    post.comments = new_comments
    dict_post = dict(post)
    return dict_post


def get_post_by_id_db(post_id: str):
    logging.info("Getting post with id from DB: " + post_id)
    post = post_db.find_one({"_id": post_id})
    return Post.parse_obj(post)


def update_post(post: Post):
    logging.info("Updating post with id: " + post.id)
    post = convert_post_to_dict(post)
    post_db.update_one({"_id": post["id"]}, post)


def post_upsert(post: Post):
    logging.info("Upserting post with id: " + post.id)
    post = convert_post_to_dict(post)
    dict_post = convert_post_to_dict(post)
    post_db.replace_one({"_id": dict_post["id"]}, dict_post, upsert=True)
