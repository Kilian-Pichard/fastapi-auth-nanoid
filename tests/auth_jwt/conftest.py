import pytest
from fastapi_auth_nanoid.auth_jwt import AuthJWT


@pytest.fixture(scope="module")
def Authorize():
    return AuthJWT()
