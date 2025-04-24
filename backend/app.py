import uvicorn


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        access_log=False,
        port=8000,
        reload=True,
    )