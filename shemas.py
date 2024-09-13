from typing import Union
from pydantic import BaseModel


class Product_typeBase(BaseModel):
    name: Union[str, None] = None


class Product_typeCreate(Product_typeBase):
    pass


class Product_type(Product_typeBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True


class ProductBase(BaseModel):
    name: str


class ProductCreate(ProductBase):
    name: str


class Product(ProductBase):
    id: int
    name: str
    type: list[Product_type] = []

    class Config:
        from_attributes = True
