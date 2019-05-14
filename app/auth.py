import base64
import binascii
from typing import Optional, Tuple

from starlette.authentication import AuthCredentials, AuthenticationBackend, AuthenticationError, SimpleUser
from starlette.requests import HTTPConnection, Request
from starlette.responses import JSONResponse


class BasicAuthBackend(AuthenticationBackend):
    async def authenticate(self, request: HTTPConnection) -> Optional[Tuple[AuthCredentials, SimpleUser]]:
        if "Authorization" not in request.headers:
            return None

        auth = request.headers["Authorization"]

        try:
            scheme, credentials = auth.split()
            if scheme.lower() != "basic":
                return None
            decoded = base64.b64decode(credentials).decode("ascii")
        except (ValueError, UnicodeDecodeError, binascii.Error):
            raise AuthenticationError("Invalid basic auth credentials")

        username, _, password = decoded.partition(":")
        if not password == "asgi>wsgi":
            return None

        return AuthCredentials(["authenticated"]), SimpleUser(username)


def auth_error(request: Request, exc: Exception) -> JSONResponse:
    return JSONResponse({"detail": "auth error"}, status_code=400)
