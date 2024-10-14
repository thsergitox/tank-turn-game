from fastapi import FastAPI
from app.database.mongo.connection import MongoConnection
from app.config import settings
from app.routes import router
from prometheus_fastapi_instrumentator import Instrumentator, metrics
from fastapi import Request
import jwt
from rich.console import Console
from rich.markdown import Markdown

# Creamos una instancia de la aplicación FastAPI
app = FastAPI(
    title="Tank Turn Game API",
    description="This is the API for the Tank Turn Gamee project",
    version="1.0.0",
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
Console Quest RPG is a turn-based role-playing game developed as a software project for the CC3S2 course at the National University of Engineering. The game uses FastAPI for the backend and is designed to be played through API calls.
---

"""
    )
    return markdown


@app.middleware("http")
async def token_middleware(request: Request, call_next):
    token = request.cookies.get("access_token")
    if token:
        try:
            payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=["HS256"])
            request.state.user = payload.get("name")
        except jwt.ExpiredSignatureError:
            request.state.user = None
    return await call_next(request)


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


@app.on_event("startup")
async def startup_event():
    # Print the banner
    console = Console()
    console.print(generate_markdown_banner())

    # Connect to the MongoDB database
    MongoConnection.connect_to_mongo(settings.MONGO_URL, settings.MONGO_DB_NAME)

    # Initialize the instrumentator
    instrumentator.expose(app)


@app.on_event("shutdown")
async def shutdown_db_client():
    MongoConnection.close_mongo_connection()
