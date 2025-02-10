class Juice:
    def __init__(self, name, capacity, price):
        self.name = name
        self.capacity = capacity
        self.price = price

    def __str__(self):
        return f"{self.name} ({self.capacity:.2f}L) {self.price:.2f} €"

    def __add__(self, other):
        new_price = self.price + other.price
        return Juice(
            self.name + "&" + other.name, self.capacity + other.capacity, new_price
        )

    def pour(self, percentage):
        assert 0.0 < percentage <= 1.0
        print(f"Pouring {percentage*100}% from {str(self)}")
        new_capacity = self.capacity * percentage
        new_price = self.price * percentage
        self.capacity -= new_capacity
        self.price -=  new_price
        return Juice(self.name, new_capacity, new_price)


a = Juice("Orange", 1.5, 3.5)
b = Juice("Apple", 2.0, 3.0)
print(a)
print(b)

result = a + b
print(result)

c = result.pour(0.4)
print(result)
print(c)
