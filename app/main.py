from routes.users import router as user_router
from routes.availability import router as availability_router
from routes.events import router as event_router
from routes.event_type import router as event_type_router
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(user_router)
app.include_router(availability_router)
app.include_router(event_router)
app.include_router(event_type_router)


