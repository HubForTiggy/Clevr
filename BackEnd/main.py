from fastapi import FastAPI
from pymongo import MongoClient
from pydantic import BaseModel


# Create FastAPI app instance
app = FastAPI()

uri = "mongodb+srv://Ash:Happyness44@cluster0.52ctye9.mongodb.net/?appName=Cluster0"
client = MongoClient(uri)
db = client["Hackathon"]
collection = db["object"]

class Event(BaseModel):
    eventName: str
    date: str
    

# Define a simple GET endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to Clevr"}

@app.post("/event", status_code=201)
async def create_student(event: Event):
    result = collection.insert_one(event.model_dump())
    return {"id": str(result.inserted_id)}