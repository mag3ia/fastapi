import pytest
from typing import List
from app import schemas

def test_get_all_posts(authorized_client, test_posts):
    res = authorized_client.get("/posts/")
#    print(res.json())
#     assert len(res.json())==len(test_posts)
    assert res.status_code == 200

def test_unauthorized_user_get_all_posts(client, test_posts):
    res = client.get("/posts/")
    assert res.status_code == 401

def test_get_one_post_not_exist(authorized_client, test_posts):
    res = authorized_client.get(f"/posts/99999")
    assert res.status_code == 404

def test_delete_post_non_exist(authorized_client, test_user, test_posts):
    res = authorized_client.delete(
        f"/posts/99999")

    assert res.status_code == 404

def test_unauthorized_user_create_post(client, test_user, test_posts):
    res = client.post(
        "/posts/", json={"title": "title", "content": "content"})
    assert res.status_code == 401

@pytest.mark.parametrize("title, content, published", [
    ("Titre du post", "Contenu du post", True),
    ("La politique", "Quos vult perdere Jupiter dementat", False),
    ("rm -rf /", "yes", True),
])
def test_create_post(authorized_client, test_user, test_posts, title, content, published):
    res = authorized_client.post(
        "/posts/", json={"title": title, "content": content, "published": published})

    created_post = schemas.Post(**res.json())
    assert res.status_code == 201
    assert created_post.title == title
    assert created_post.content == content
    assert created_post.published == published
    assert created_post.owner_id == test_user['id']

def test_create_post_default_published_true(authorized_client, test_user, test_posts):
    res = authorized_client.post(
        "/posts/", json={"title": "Can't keep checking my phone", "content": "Everyone acts crazy nowadays"})

    created_post = schemas.Post(**res.json())
    assert res.status_code == 201
    assert created_post.title == "Can't keep checking my phone"
    assert created_post.content == "Everyone acts crazy nowadays"
    assert created_post.published == True
    assert created_post.owner_id == test_user['id']
