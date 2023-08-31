import uvicorn
from dotenv import load_dotenv
import os

load_dotenv()

if __name__ == "__main__":
    uvicorn.run("website.asgi:application", port=int(os.getenv('PORT', 8000)), log_level="info")