from fastapi import FastAPI

app = FastAPI(title="Open Library - Backend")

@app.get("/healthz")
def health():
    return {"status": "ok"}
