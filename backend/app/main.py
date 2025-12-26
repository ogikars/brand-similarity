from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional

# Initialize FastAPI application
app = FastAPI(
    title="Brand Similarity API",
    description="API for comparing brand similarities using visual and word-based analysis",
    version="1.0.0",
)

# Configure CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure as needed for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Health Check Endpoint
@app.get("/health", tags=["Health"])
async def health_check():
    """
    Health check endpoint to verify API is running.
    
    Returns:
        dict: Status of the API
    """
    return {
        "status": "healthy",
        "message": "Brand Similarity API is running",
        "version": "1.0.0",
    }


# Root Endpoint
@app.get("/", tags=["Root"])
async def root():
    """
    Root endpoint providing API information.
    
    Returns:
        dict: API information and available endpoints
    """
    return {
        "name": "Brand Similarity API",
        "version": "1.0.0",
        "endpoints": {
            "health": "/health",
            "visual_comparison": "/api/v1/compare/visual",
            "word_comparison": "/api/v1/compare/word",
        },
    }


# Visual Comparison Router
@app.post("/api/v1/compare/visual", tags=["Visual Comparison"])
async def visual_comparison(image1_path: str, image2_path: str):
    """
    Compare two brand logos/images visually.
    
    Args:
        image1_path (str): Path to the first image
        image2_path (str): Path to the second image
    
    Returns:
        dict: Similarity score and analysis results
    """
    return {
        "status": "success",
        "comparison_type": "visual",
        "image1": image1_path,
        "image2": image2_path,
        "similarity_score": 0.0,
        "message": "Visual comparison endpoint - implementation pending",
    }


# Word Comparison Router
@app.post("/api/v1/compare/word", tags=["Word Comparison"])
async def word_comparison(text1: str, text2: str):
    """
    Compare two brand names/text using word-based similarity.
    
    Args:
        text1 (str): First text/brand name
        text2 (str): Second text/brand name
    
    Returns:
        dict: Similarity score and analysis results
    """
    return {
        "status": "success",
        "comparison_type": "word",
        "text1": text1,
        "text2": text2,
        "similarity_score": 0.0,
        "message": "Word comparison endpoint - implementation pending",
    }


# Error Handlers
@app.exception_handler(Exception)
async def general_exception_handler(request, exc):
    """
    Handle general exceptions and return error response.
    
    Args:
        request: Request object
        exc: Exception object
    
    Returns:
        dict: Error response
    """
    return {
        "status": "error",
        "message": str(exc),
        "error_type": type(exc).__name__,
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
