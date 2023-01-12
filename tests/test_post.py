def test_get_all_posts(authorized_client, test_posts):
    res = authorized_client.get("/posts/")
    assert len(response.json()) ==len(test_posts)
    assert res.status_code == 200

def test_unauthorized_user_get_all_posts(client, tests_posts):
    res = client.get("/posts/")
    assert res.status_code == 401

def test_unauthorized_user_get_one_posts(client, tests_posts):
    res = client.get(f"/post/{test_post[0].id}")
    assert res.status_code == 401
