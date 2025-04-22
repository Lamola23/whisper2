from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Whisper API funcionando ✅"}

if __name__ == "__main__":
    print("🔊 Lanzando Uvicorn...")
    uvicorn.run(app, host="0.0.0.0", port=8080)

