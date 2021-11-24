from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from api.db.base import Base
from api.db.session import engine
from api.endpoints import router
from api.core.config import Config
from api.core.instrumentation import (
    setup_instrumentation_tracer,
    instrument_fastapi,
    instrument_requests,
    instrument_sqlalchemy,
)


def get_app() -> FastAPI:

    # inspired from https://github.com/tiangolo/fastapi/issues/508#issuecomment-532368194
    settings = Config()  # see example above

    server = FastAPI(
        title=settings.project_name,
        openapi_url=settings.openapi_route,
        debug=settings.DEBUG,
    )

    setup_instrumentation_tracer(
        service_name="service", dataset=settings.HONEYCOMB_DATASET
    )
    instrument_fastapi(app=server)
    instrument_requests()
    instrument_sqlalchemy(engine=engine)

    @server.get("/", include_in_schema=False)
    def redirect_to_docs() -> RedirectResponse:
        return RedirectResponse("/docs")

    server.include_router(router, prefix="/api/v1/service")

    return server
