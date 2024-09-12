import uvicorn
from fastapi import FastAPI, HTTPException, Depends
import models
import shemas
from sqlalchemy.orm import Session
import crud
from database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/products", response_model=list[shemas.Product])
def read_products(db: Session = Depends(get_db)):
    db_products = crud.get_products(db)
    if db_products is None:
        raise HTTPException(status_code=404, detail="Products not found")
    return db_products


@app.post("/products", response_model=shemas.Product)
def create_product(product: shemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.add_product(db=db, product=product)


@app.get("/products/{id}", response_model=list[shemas.Product])
def read_product(id: int, db: Session = Depends(get_db)):
    db_product = crud.get_product(db=db, product_id=id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_product


@app.post("/products/type/{type_id}", response_model=list[shemas.Product])
def read_products_type(type_id: int, db: Session = Depends(get_db)):
    db_products_type = crud.get_products_type(db=db, type_id=type_id)
    if db_products_type is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_products_type


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)