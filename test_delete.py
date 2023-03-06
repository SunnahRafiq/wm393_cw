import pytest
from main import Users

@pytest.fixture
def test_user():
    return Users('testuser', 'testpass', 'student', 'BS', 'Test User', '2023')

def test_get_student_by_username(test_user):
    assert test_user.username == 'testuser'
    assert test_user.password == 'testpass'
    assert test_user.role == 'student'
    assert test_user.degree == 'BS'
    assert test_user.name == 'Test User'
    assert test_user.year == '2023'
