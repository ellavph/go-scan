import uvicorn
from fastapi import FastAPI
from app.user import routes
from fastapi.responses import RedirectResponse
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

@app.get("/", include_in_schema=False)
def index():
    return RedirectResponse(url="/docs", status_code=302)


app.include_router(router=routes.router, prefix="/users", tags=["users"])
