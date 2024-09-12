from sqlalchemy.orm import Session
import models
import shemas


# Получение всех товаров
def get_products(db: Session) -> list[models.Product]:
    result = db.query(models.Product).all()
    return result


# Получение товара по id
def get_product(db: Session, product_id: int) -> models.Product:
    db_product = db.query(models.Product).filter(models.Product.id == product_id).all()
    return db_product


# Добавление нового товара
def add_product(db: Session, product: shemas.ProductCreate) -> models.Product:
    db_user = models.Product(**product.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# Получение всех товаров по типу
def get_products_type(db: Session, type_id: int) -> models.Product:
    result = db.query(models.Product).filter(models.Product.product_type_id == type_id).all()
    return result