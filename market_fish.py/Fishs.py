from dataclasses import dataclass

@dataclass(slots=True)
class Fish:
    product_name: str
    view: str
    preparetion: str
    date_of_manufacture: str
    weight: float
    price: int 
    size: str   
    id: int | None = None

@dataclass(slots=True)
class Drink:
    drink_name: str
    volume: float
    price: int
    quantity: int
    id: int | None = None
