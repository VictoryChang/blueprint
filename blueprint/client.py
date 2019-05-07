import requests


class Client(object):
    """
    Communicate with the <host> API
    """
    def __init__(self):
        self.host = 'https://jsonplaceholder.typicode.com'

    def posts_get(self):
        """
        Get the content of all of the posts
        """
        url = self.host + '/posts'
        return self.request(url, method='GET')

    def post_get(self, post_id):
        """
        Get the content of a single post

        :param int post_id: Post ID
        """
        url = self.host + '/posts/%s' % post_id
        return self.request(url, method='GET')

    def post_update(self, post_id, title, body, user_id):
        """
        Update a post

        :param int post_id: Post ID
        :param str title: Update for post title
        :param str body: Update for post body
        :param int user_id: Update for post user id
        """
        url = self.host + '/posts/%s' % post_id

        json_data = {
            'title': title,
            'body': body,
            'user_id': user_id
        }

        return self.request(url, method='PUT', json=json_data)

    def post_create(self, title, body, user_id):
        """
        Create a post

        :param str title: Update for post title
        :param str body: Update for post body
        :param int user_id: Update for post user id
        """
        url = self.host + '/posts'

        json_data = {
            'title': title,
            'body': body,
            'user_id': user_id
        }

        return self.request(url, method='POST', json=json_data)

    def post_delete(self, post_id):
        """
        Delete a post

        :param int post_id:
        """
        url = self.host + '/posts/%s' % post_id
        return self.request(url, method='DELETE')

    def request(self, url, method, json=None):
        """
        Make general requests with the API

        :param str url: Request URL
        :param str method: Request method
        :param Dict(str, str) json: Request data
        """
        response = requests.request(
            url=url,
            method=method,
            json=json
        )
        return response
