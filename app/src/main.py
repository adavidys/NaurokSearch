import uvicorn

from fastapi import FastAPI

from api_v1 import api_v1


app = FastAPI()
app.include_router(api_v1)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, host="0.0.0.0", port=8000)