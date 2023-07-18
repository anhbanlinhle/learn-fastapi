from fastapi import FastAPI, Path, Query
from pydantic import BaseModel
from typing import Annotated

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

@app.get("/update-item")
async def update_item(update: Annotated[str | None, Query(max_length = 30)] = None):
	result = {"item_id": "Foo"}
	origin = result.copy()
	if update:
		result.update({"update": update})
	return {"origin": origin, "updated": result}