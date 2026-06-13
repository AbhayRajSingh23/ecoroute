# Import FastAPI
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import DB and models
import models
from database import engine

# Import router
from routers import driver

# Create DB tables automatically
models.Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(title="Driver Service")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:3000",
        "https://ecoroute-service-driver-production.up.railway.app",
        "*"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include driver routes
app.include_router(driver.router)


# Root endpoint (for testing)
@app.get("/")
def root():
    return {"message": "Driver Service Running 🚀"}