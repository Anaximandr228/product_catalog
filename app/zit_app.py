import uvicorn
from fastapi import FastAPI, HTTPException, Depends
from app import models
from app import shemas
from sqlalchemy.orm import Session
from app import crud
from app.database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/products", response_model=list[shemas.Product],
         summary="Получение продукта",
         description="При запросе выводятся все "
                     "продукты, содержащиеся в базе данных")
def read_products(db: Session = Depends(get_db)):
    db_products = crud.get_products(db)
    if db_products is None:
        raise HTTPException(status_code=404, detail="Products not found")
    return db_products


@app.post("/products", response_model=shemas.Product,
          summary="Добавление продукта",
          description="При отправке запросе в "
                      "базу данных добавляется новый продукт")
def create_product(product: shemas.ProductCreate,
                   db: Session = Depends(get_db)):
    return crud.add_product(db=db, product=product)


@app.post("/type", response_model=shemas.ProductType,
          summary="Добавление типов продукта",
          description="При отправке запросе в базу "
                      "данных добавляется новый тип продуктов")
def create_product_type(product_type: shemas.ProductTypeCreate,
                        db: Session = Depends(get_db)):
    return crud.add_product_type(db=db, product_type=product_type)


@app.get("/products/{id}", response_model=list[shemas.Product],
         summary="Получение продукта по его id",
         description="При отправке запросе выводится запрашиваемый продукт")
def read_product(id: int, db: Session = Depends(get_db)):
    db_product = crud.get_product_id(db=db, product_id=id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_product


@app.get("/products/type/{type_id}", response_model=list[shemas.Product],
         summary="Получение продуктов по типу",
         description="При отправке запросе выводятся "
                     "продукты по запрашиваемому типу")
def read_products_type(type_id: int, db: Session = Depends(get_db)):
    db_products_type = crud.get_products_type(db=db, type_id=type_id)
    if db_products_type is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_products_type


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
