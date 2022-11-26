from pymongo import MongoClient

from dto.post import Post
from dto.comment import Comment

from database import get_post_by_id_db, convert_post_to_dict, update_post, post_upsert, get_all_posts_db

import logging


def get_all_posts():
    logging.info("Getting all posts")
    posts = get_all_posts_db()
    return posts


def get_post_by_id(post_id: str) -> Post or None:
    """
    Gets a post by its ID.
    :param post_id: The ID of the post to be retrieved.
    :return: The Post object with the given ID.
    """
    logging.info("Getting post with id: " + post_id)
    post = get_post_by_id_db(post_id)
    if post is None:
        return None
    return post


def create_new_comment_in_post(post_id: str, comment: Comment):
    """
    Creates a new comment in a post
    :param post_id: The ID of the post where the comment will be added.
    :param comment: Comment that will be added to the post.
    :return: Returns the status of the operation, none if negative.
    """
    post = get_post_by_id_db(post_id)
    if post is None:
        return False
    post = convert_post_to_dict(post)
    logging.info("Creating new comment in post with id: " + str(post["id"]))
    post["comments"].append(dict(comment))
    update_post(post)
    return True


def like_post(post_id: str):
    logging.info("Liking post with id: " + post_id)
    post = get_post_by_id_db(post_id)
    if post is None:
        return False   # In case of an unnsucesful operation
    post = convert_post_to_dict(post)
    post["likes"] = post["likes"] + 1
    print(post)
    update_post(post)
    return True  # If operation is successful


def unlike_post(post_id: str):
    logging.info("Unliking post with id: " + post_id)
    post = get_post_by_id_db(post_id)
    if post is None:
        return False   # In case of an unnsucesful operation
    post = convert_post_to_dict(post)
    if post["likes"] > 0:
        post["likes"] = post["likes"] - 1
        update_post(post)
        print(post)
        return True  # If operation is successful
    logging.info("Post has no likes")
    return True  # If operation is successful


def create_new_comment(post_id, comment: Comment):
    logging.info("Creating new comment in post with id: " + post_id)
    post = get_post_by_id_db(post_id)
    if post is None:
        return False
    post.comments.append(comment)
    update_post(post)


def create_new_post(post: Post):
    logging.info("Creating new post")
    print(post)
    post_upsert(post)


"""
def delete_post(post_id: str):
    logging.info("Deleting post with id: " + post_id)
    # TODO validate post ownership
    post_db.delete_one({"id": post_id})
    
def get_user(user_id: str):
    logging.info("Getting user with id: " + user_id)
    user = user_db.users.find_one({"user_id": user_id})
    if user:
        return user
    return None

def get_user_posts(user_id: str):
    logging.info("Getting posts from user with id: " + user_id)
    posts = post_db.find({"user_id": user_id})
    if posts is None:
        return None
    return post_db.find_all({"user_id": user_id})
"""
