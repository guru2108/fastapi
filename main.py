from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pywhatkit
app = FastAPI()

# origins = ["*"]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/songs/{title}")
async def geturl(title):
    url=pywhatkit.playonyt(title)
    return {"url":url}
