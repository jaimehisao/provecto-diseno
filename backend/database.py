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
    if type(post) is not dict:
        new_comments = []
        for comment in post.comments:
            new_comments.append(dict(comment))
        post.comments = new_comments
        dict_post = dict(post)
        return dict_post
    return post


def get_post_by_id_db(post_id: str):
    logging.info("Getting post with id from DB: " + post_id)
    post = post_db.find_one({"_id": post_id})
    return Post.parse_obj(post)


def update_post(post: Post):
    post = convert_post_to_dict(post)
    logging.info("Updating post with id: " + post["id"])
    post_db.replace_one({"_id": post["id"]}, post)


def post_upsert(post: Post):
    logging.info("Upserting post with id: " + post.id)
    post = convert_post_to_dict(post)
    post_db.replace_one({"_id": post["id"]}, post, upsert=True)
