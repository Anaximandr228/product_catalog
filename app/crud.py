from sqlalchemy.orm import Session
from app import models
from app import shemas


# Получение всех товаров
def get_products(db: Session) -> list[models.Product]:
    result = db.query(models.Product).all()
    return result


# Получение товара по id
def get_product_id(db: Session, product_id: int) -> models.Product:
    db_product = \
        db.query(models.Product).filter(models.Product.id == product_id).all()
    return db_product


# Добавление нового товара
def add_product(db: Session, product: shemas.ProductCreate) -> models.Product:
    db_product = models.Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


# Добавление нового типа продукта
def add_product_type(db: Session,
                     product_type: shemas.ProductTypeCreate) \
        -> models.ProductType:
    db_product_type = models.ProductType(**product_type.dict())
    db.add(db_product_type)
    db.commit()
    db.refresh(db_product_type)
    return db_product_type


# Получение всех товаров по типу
def get_products_type(db: Session,
                      type_id: int) -> models.Product:
    result = db.query(models.Product).\
        filter(models.Product.product_type_id == type_id).all()
    return result
