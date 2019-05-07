import unittest

from blueprint.client import Client


class ClientTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_posts_get(self):
        response = self.client.posts_get()
        assert response.status_code == 200
        assert len(response.json()) == 100

    def test_post_get(self):
        response = self.client.post_get(post_id=1)
        assert response.status_code == 200
        content = response.json()
        assert content['id'] == 1
        assert content['title'] == 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit'

    def test_post_create(self):
        response = self.client.post_create(title='sample', body='sample', user_id='sample')
        assert response.status_code == 201
        content = response.json()
        assert content['title'] == 'sample'
        assert content['body'] == 'sample'
        assert content['user_id'] == 'sample'

    def test_post_update(self):
        response = self.client.post_update(post_id=1, title='sample', body='sample', user_id='sample')
        assert response.status_code == 200

    def test_post_delete(self):
        response = self.client.post_delete(post_id=1)
        assert response.status_code == 200
