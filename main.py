from Problem import Company,Product,Basket

c1 = Company("Apple", 1990, "Steve Jobs")
pr1 = Product("iPhone 15 Pro", 800, 10, c1)
pr2 = Product("iPhone 15 Pro", 800, 5, c1)
pr3 = Product("iPhone 14", 700, 3, c1)

b = Basket()
b.add(pr1)
b.add(pr2)
b.add(pr3)

print("Products:")
b.view()
print(f"Total: {b.total()} USD")

b.remove("iPhone 14")
print("Products removed from cart:")
b.view()
