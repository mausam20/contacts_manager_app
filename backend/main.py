from fastapi import FastAPI
from database import Base, engine
from fastapi.middleware.cors import CORSMiddleware
import contact_views

def create_application() -> FastAPI:
    app = FastAPI(
        title="Contact Book",
    )
    Base.metadata.create_all(bind=engine)
    configure(app)
    return app


def configure(app):
    configure_routing(app)


def configure_routing(app):
    app.include_router(contact_views.router)


app = create_application()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)