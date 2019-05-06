from starlette.exceptions import HTTPException
from starlette.requests import Request
from starlette.responses import JSONResponse


async def not_found(request: Request, exc: HTTPException) -> JSONResponse:
    return JSONResponse({"detail": "not found"}, status_code=exc.status_code)
