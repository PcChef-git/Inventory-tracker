# main.py

from inventory.parser import parse_csv
from inventory.db import initialize_db, insert_item, fetch_low_stock
from inventory.exporter import export_to_csv

if __name__ == "__main__":
    initialize_db()

    items = parse_csv("data/parsed_csv/sample.csv")
    for item in items:
        insert_item(item)

    low_stock = fetch_low_stock()

    print("🔍 Low Stock Items:")
    for item in low_stock:
        print(f"  - {item.name} ({item.quantity} {item.unit}) – needs reorder")

    export_to_csv(low_stock, "data/exports/reorder_list.csv")
    print("\n✅ Exported reorder list to data/exports/reorder_list.csv")
