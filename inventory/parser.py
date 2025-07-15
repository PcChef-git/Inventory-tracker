import csv
from inventory.models import InventoryItem
from pathlib import Path

def parse_csv(file_path: str) -> list[InventoryItem]:
    inventory_items = []

    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            item = InventoryItem(
                name=row["name"],
                category=row["category"],
                quantity=float(row["quantity"]),
                unit=row["unit"],
                price=float(row["price"]),
                vendor=row.get("vendor")

            )
            inventory_items.append(item)

    return inventory_items