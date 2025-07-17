from inventory.models import InventoryItem
# Here we are going to add a simple "par level" check

PAR_LEVELS = {
    "Olive Oil": 4.0,
    "Salt": 5.0,
    "Pepper": 5.0,
    "Flour": 6.0,
    "Tomatoes": 5.0
}

def check_below_par(items: list[InventoryItem]) -> list[InventoryItem]:
    low_stock = []
    
    for item in items:
        par = PAR_LEVELS.get(item.name, None)
        if par is not None and item.quantity < par:
            low_stock.append(item)
            
    return low_stock