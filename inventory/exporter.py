# inventory/exporter.py

import csv
from inventory.models import InventoryItem
from pathlib import Path

def export_to_csv(items: list[InventoryItem], output_path: str):
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, mode='w', newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["name", "quantity", "unit", "vendor", "price", "total_cost"])
        
        for item in items:
            writer.writerow([
                item.name, 
                item.quantity, 
                item.unit, 
                item.vendor or "Unknown",
                item.price,
                item.total_cost()
            ])