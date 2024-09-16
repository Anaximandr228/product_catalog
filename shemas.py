from pydantic import BaseModel


class Product_typeBase(BaseModel):
    name: str


class Product_typeCreate(Product_typeBase):
    name: str


class Product_type(Product_typeBase):
    id: int
    name: str

    class Config:
        from_attributes = True


class ProductBase(BaseModel):
    name: str


class ProductCreate(ProductBase):
    name: str
    product_type_id: int


class Product(ProductBase):
    id: int
    name: str
    product_type_id: int
    type: Product_type

    class Config:
        from_attributes = True
