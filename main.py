# main.py

from inventory.parser import parse_csv
from inventory.processor import check_below_par
from inventory.exporter import export_to_csv

if __name__ == "__main__":
    # Load data
    inventory = parse_csv("data/parsed_csv/sample.csv")

    # Check for low stock
    low_stock = check_below_par(inventory)

    print("🔍 Low Stock Items:")
    for item in low_stock:
        print(f"  - {item.name} ({item.quantity} {item.unit}) – needs reorder")

    # Export results
    export_to_csv(low_stock, "data/exports/reorder_list.csv")
    print("\n✅ Exported reorder list to data/exports/reorder_list.csv")
