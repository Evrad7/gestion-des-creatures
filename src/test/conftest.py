import pytest
from model.explorer import Explorer
from model.creature import Creature
from model.explorer import Explorer
from model.user import InnerUser, CreateUser, User
from fake.data.creature import get_all as get_all_creatures
from fake.data.explorer import get_all as get_all_explorers
from fake.data.user import get_all as get_all_users

@pytest.fixture
def explorer():
    pass

@pytest.fixture
def creature() -> Creature:
    return Creature(
        name="Yeti Test",
        country="CN",
        area="Himalayas",
        description="Hirsute Himalayan",
        aka="Abominable Snowman",
    )
@pytest.fixture
def creatures():
    return get_all_creatures() 

@pytest.fixture
def explorer():
    return Explorer(
        name="Gilber Test",
        country="CM",
        description="Experencied explorer hunter"
    )

@pytest.fixture
def explorers():
    return get_all_explorers() 

@pytest.fixture
def user():
    return InnerUser(name="username", hash="abcxyz")


@pytest.fixture
def create_user():
    return CreateUser(name="username", password="password")

@pytest.fixture
def users():
    return get_all_users() 