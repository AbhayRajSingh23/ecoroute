# FastAPI app
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import models
from database import engine
from routers import order

# Create tables automatically
models.Base.metadata.create_all(bind=engine)

# Initialize app
app = FastAPI(title="Order Service")

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

# Include routes
app.include_router(order.router)


# Root endpoint
@app.get("/")
def root():
    return {"message": "Order Service Running 🚀"}