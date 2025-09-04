from fastapi  import FastAPI
from typing import Optional


app = FastAPI()


products = [
    {"id": 1, "name": "Laptop", "category": "Electronics", "price": 55000},
    {"id": 2, "name": "Smartphone", "category": "Electronics", "price": 25000},
    {"id": 3, "name": "Desk Chair", "category": "Furniture", "price": 7000},
    {"id": 4, "name": "Water Bottle", "category": "Kitchen", "price": 5000},
    {"id": 5, "name": "Headphones", "category": "Electronics", "price": 3500}
]


@app.get('/products')
def search_products(category:Optional[str] = None,max_price:Optional[int] = None):
    filter_products =products 

    if category:
        filter_products = [p for p in filter_products if p['category'].lower() == category.lower()]
  
    if max_price:
        filter_products = [p for p in filter_products if p['price'] <= max_price] 
 
    return filter_products
