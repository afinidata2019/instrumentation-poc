from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from grpc import ssl_channel_credentials

from api.core.config import Config


settings = Config()


def setup_instrumentation_tracer(service_name: str, dataset: str):
    # resource describes app-level information that will be added to all spans
    resource = Resource(attributes={"service.name": service_name})

    # create new trace provider with our resource
    trace_provider = TracerProvider(resource=resource)

    # create exporter to send spans to Honeycomb
    otlp_exporter = OTLPSpanExporter(
        endpoint="api.honeycomb.io:443",
        insecure=False,
        credentials=ssl_channel_credentials(),
        headers=(
            ("x-honeycomb-team", settings.HONEYCOMB_API_KEY),
            ("x-honeycomb-dataset", dataset),
        ),
    )

    # register exporter with provider
    trace_provider.add_span_processor(BatchSpanProcessor(otlp_exporter))

    # register trace provider
    trace.set_tracer_provider(trace_provider)


def instrument_fastapi(app):
    from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor

    FastAPIInstrumentor.instrument_app(app)


def instrument_requests():
    from opentelemetry.instrumentation.requests import RequestsInstrumentor

    RequestsInstrumentor().instrument()


def instrument_sqlalchemy(engine):
    from opentelemetry.instrumentation.sqlalchemy import SQLAlchemyInstrumentor

    SQLAlchemyInstrumentor().instrument(engine=engine)
