import requests


class ReqresException(Exception):
    pass


class ReqresClient(object):
    def __init__(self):
        self.base_url = 'https://reqres.in/api'

    def user_get(self, user_id):
        url = f'{self.base_url}/users/{user_id}'
        return self.request(url, method='GET')

    def users_get(self, page):
        url = f'{self.base_url}/users'
        params = {'page': page}
        return self.request(url, method='GET', params=params)

    def user_post(self, name, job):
        url = f'{self.base_url}/users'
        json = {'name': name, 'job': job}
        return self.request(url, method='POST', json=json)

    def user_put(self, user_id, name, job):
        url = f'{self.base_url}/users/{user_id}'
        json = {'name': name, 'job': job}
        return self.request(url, method='PUT', json=json)

    def user_delete(self, user_id):
        url = f'{self.base_url}/users/{user_id}'
        return self.request(url, method='DELETE')

    def request(self, url, method, params=None, json=None, timeout=30.0):
        try:
            response = requests.request(
                url=url,
                method=method,
                params=params,
                json=json,
                timeout=timeout)
            print(f'{method}: {response.url}')
            print(response.status_code)
            return response
        except requests.exceptions.RequestException:
            raise ReqresException('RequestException')


if __name__ == '__main__':
    client = ReqresClient()
    response = client.user_get(2)
    assert response.status_code == 200
    print(response.json())

    response = client.user_get(23)
    assert response.status_code == 404

    response = client.users_get(2)
    assert response.status_code == 200
    print(response.json())

    response = client.user_post(
        name='morpheus', job='leader')
    assert response.status_code == 201
    print(response.json())

    response = client.user_delete(2)
    assert response.status_code == 204

    response = client.user_put(
        user_id=2, name='morpheus', job='zion resident')
    assert response.status_code == 200
    print(response.json())