from dataclasses import dataclass
from typing import Optional

@dataclass
class InventoryItem:
    name:str
    category:str
    quantity:float
    unit:str
    price:float
    vendor:Optional[str] = None

    def total_cost(self) -> float:
        return round(self.quantity * self.price, 2) 