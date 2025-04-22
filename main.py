from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def root():
    return {"msg": "🚀 API online y funcionando"}

if __name__ == "__main__":
    print("🔥 Lanzando Uvicorn...")
    uvicorn.run("main:app", host="0.0.0.0", port=8000)

