import uvicorn
from fastapi import FastAPI
from app.user import routes
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Go-Scan API",
    description="Endpoints para integração com o back-end",
    version="1.0.0"
)


origins = [
    "http://localhost:3000",
    "https://go-scan-front.vercel.app",
]

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

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
