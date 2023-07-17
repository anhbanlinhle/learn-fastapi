from fastapi import FastAPI, Path
from pydantic import BaseModel

class Item(BaseModel):
	name: str
	price: float
	tax: float = None
	description: str = None
	is_offer: bool = None


app = FastAPI()

@app.get("/")
async def root():
	return {"message": "Hello World"}

@app.post("/items/")
async def create_item(item: Item):
	item_dict = item.dict()
	if item.tax:
		price_with_tax = item.price + item.tax
		item_dict.update({"price_with_tax": price_with_tax})
	print(item_dict)
	return item_dict