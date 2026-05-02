from fastapi import FastAPI

app = FastAPI(title="DynamicOS API")

@app.get("/api/v1/health")
def health():
    return {"status": "ok"}
