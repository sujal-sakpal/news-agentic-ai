from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
from crew import run_news_crew
import asyncio 
from concurrent.futures import ThreadPoolExecutor

executor = ThreadPoolExecutor()

# Initialize FastAPI app
app = FastAPI(
    title="AI News Agent API",
    description="An API to get summarized news on any topic using a CrewAI-powered agent.",
    version="1.0.0",
)

# Configure CORS (Cross-Origin Resource Sharing)
# This allows the frontend (running on a different port) to communicate with the backend.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Pydantic model for the request body
# This ensures that the incoming data has the correct format.
class TopicRequest(BaseModel):
    topic: str

# Define the API endpoint
@app.post("/get-news-summary")
async def get_news_summary(request: TopicRequest):
    """
    This endpoint accepts a news topic, runs the AI crew to research and
    summarize it, and returns the final report.
    """
    loop = asyncio.get_running_loop()
    result = await loop.run_in_executor(executor,run_news_crew,request.topic)
    return {"summary":result}

# Root endpoint for basic API health check
@app.get("/")
def read_root():
    return {"status": "AI News Agent API is running!"}

# To run the server, use the command: uvicorn main:app --reload
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
