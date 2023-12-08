from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()

# main.py
from fastapi import FastAPI
from app.user.routes import router as user_router

app = FastAPI()

app.include_router(user_router, prefix="/users", tags=["users"])


@app.get("/", include_in_schema=False)
def read_root():
    return RedirectResponse(url="/docs", status_code=302)
