from flask import url_for
import pytest

# def test_user_exists(client):
#     data = {'email': 'guest@fake.com'}
#     url = url_for('auth.checkUserExists')

#     res = client.post(url, json=data)
#     print(f'{res.json}')

#     assert res.json == {'userExists': False}

@pytest.mark.parametrize("email,",['guest@fake.com','jsalaz1989@gmail.com'])
def test_user_exists(client, email):
    data = {'email': email}
    url = url_for('auth.checkUserExists')

    res = client.post(url, json=data)
    print(f'{res.json}')

    assert res.json == {'userExists': True}
