dt = {}
with open("input.txt", "r") as f:
    for line in f.readlines():
        name, product, count = line.split()
        count = int(count)

        if dt.get(name) == None:
            dt[name] = {}
        if dt[name].get(product) == None:
            dt[name][product] = 0

        dt[name][product] += count

dt = dict(sorted(dt.items()))
for name, products in dt.items():
    print(f"{name}:")
    products = dict(sorted(products.items()))
    for pname, count in products.items():
        print(pname, count)