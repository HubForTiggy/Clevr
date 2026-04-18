from fastapi import FastAPI
from pymongo import MongoClient


# Create FastAPI app instance
app = FastAPI()

uri = "mongodb+srv://Ash:Happyness44@cluster0.52ctye9.mongodb.net/?appName=Cluster0"
client = MongoClient(uri)

# Define a simple GET endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to Clevr"}