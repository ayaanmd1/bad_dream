from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import PlainTextResponse

app = FastAPI()

# 1. Enable CORS (Cross-Origin Resource Sharing)
# This is crucial for "opening it anywhere." It allows browsers 
# and other apps to access your API without security blocks.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows ALL origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows ALL methods (GET, POST, etc.)
    allow_headers=["*"],
)

# Option A: Returns JSON (Best for apps/code)
# Access at: http://your-url.com/
@app.get("/")
async def root():
    return {"message": "i will never leave you and i love  u more than anything in this universe."}

# Option B: Returns Plain Text (Best for humans reading in a browser)
# Access at: http://your-url.com/text
@app.get("/text", response_class=PlainTextResponse)
async def read_text():
    return "i will never leave you and i love u more than anything in this universe."

if __name__ == "__main__":
    import uvicorn
    # Use host="0.0.0.0" to make it accessible on your local network
    uvicorn.run(app, host="0.0.0.0", port=8000)