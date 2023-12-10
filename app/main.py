import uvicorn
from fastapi import FastAPI
from app.user.routes import router as user_router
from fastapi.responses import RedirectResponse


app = FastAPI()

app.include_router(user_router, prefix="/users", tags=["users"])


@app.get("/", include_in_schema=False)
def index():
    return RedirectResponse(url="/docs", status_code=302)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
