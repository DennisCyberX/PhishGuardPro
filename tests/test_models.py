from api.models import User

def test_user_model():
    user = User(username="test", password="test")
    assert user.username == "test"
