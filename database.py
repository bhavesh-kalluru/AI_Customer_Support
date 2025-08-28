import json

def load_faqs():
    with open("data/faqs.txt", "r") as f:
        return [line.strip() for line in f.readlines() if line.strip()]

def load_orders():
    with open("data/orders.json", "r") as f:
        return json.load(f)
