from starlette.requests import Request
from starlette.responses import JSONResponse


async def homepage(request: Request) -> JSONResponse:
    return JSONResponse({'hello': 'asgi'})
