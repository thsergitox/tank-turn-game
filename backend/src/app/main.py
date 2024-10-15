from fastapi import FastAPI, Request
from app.database.mongo.connection import MongoConnection
from app.config import settings
from app.routes import router
from prometheus_fastapi_instrumentator import Instrumentator, metrics
import jwt
from rich.console import Console
from rich.markdown import Markdown
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Print the banner
    console = Console()
    console.print(generate_markdown_banner())

    # Connect to the MongoDB database
    await MongoConnection.connect_to_mongo(settings.MONGO_URL, settings.MONGO_DB_NAME)

    # Initialize the instrumentator
    instrumentator.expose(app)
    yield
    await MongoConnection.close_mongo_connection()


# Creamos una instancia de la aplicación FastAPI
app = FastAPI(
    title="Tank Turn Game API",
    description="This is the API for the Tank Turn Gamee project",
    version="1.0.0",
    lifespan=lifespan,
)


def generate_markdown_banner():
    markdown = Markdown(
        """
# 🎮 Tank Turn Game API ⚔️
### Made with ❤️ in Perú
### By Pacheco André, Pezo Sergio, Torres Oscar 2️⃣ 0️⃣ 2️⃣ 4️⃣
- **Powered by**: FastAPI
- **Status**: Initializing...
---
Tank Turn Game API is a RESTful API that provides the backend for the Tank Turn Game project. This API is responsible for handling player registration, player login, and game data storage. The API is built using FastAPI, a modern Python web framework that is designed for building APIs quickly and efficiently.
---

"""
    )
    return markdown


app.include_router(router, prefix="/api")

instrumentator = Instrumentator().instrument(app)

instrumentator.add(
    metrics.requests(
        metric_name="http_all_requests",
    )
)
instrumentator.add(
    metrics.latency(
        metric_name="http_all_request_duration_seconds",
    )
)
