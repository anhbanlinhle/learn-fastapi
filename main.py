from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/")
async def root():
	return {"message": "Hello World"}
