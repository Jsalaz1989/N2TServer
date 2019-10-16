# Based off: https://www.patricksoftwareblog.com/testing-a-flask-application-using-pytest/

def test_new_user(test_client, new_user):
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check that the email, hashed_password, active, confirmedAt, and roles fields are defined correctly
    """
    assert new_user.email == 'guest@fake.com'
    assert new_user.password != 'test123'
    assert not new_user.active
    assert not new_user.confirmedAt
    assert new_user.roles == []