from inventory.parser import parse_csv

def main():
    items = parse_csv("data/parsed_csv/sample.csv")
    for item in items:
        print(item)
        print("Total cost:", item.total_cost())

if __name__ == "__main__":
    main()