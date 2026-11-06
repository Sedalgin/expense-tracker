class Product:
    def __init__(self,name,price):
        self.name = name
        self.change_price(price)

    def change_price(self,new_price):
        if new_price < 0:
            raise ValueError("Invalid price")
        else:
            self.price = new_price

test = Product("test",10)
test_1 = Product("test",20)
test_2 = Product("test2",50)
expend = [test,test_1,test_2]
print(expend)

def calculate_product_total(products):
        calculate = 0
        if len(products)>0:
            for x in products:
                print(f"{x.name}: {x.price}")
                calculate += x.price
        else:
            print(0)
        return calculate

print(calculate_product_total(expend))