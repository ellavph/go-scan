import uvicorn
from fastapi import FastAPI
from app.user import routes
from fastapi.responses import RedirectResponse

app = FastAPI()


@app.get("/", include_in_schema=False)
def index():
    return RedirectResponse(url="/docs", status_code=302)


app.include_router(router=routes.router, prefix="/users", tags=["users"])
