class Item: 
    payRate = 0.8
    def __init__(this, name:str, price:float, quantity = 0): 
    
        # run validation
        assert price >= 0, f"{price} must be greater than or equal to zero"
        assert quantity >= 0, f"{quantity} must be greater than or equal to zero"

        # assign
        this.name = name 
        this.price = price
        this.quantity = quantity
    
    def result(this): 
        return this.price * this.quantity

    def discount(this): 
        this.price = this.price * Item.payRate

item1 = Item("Phone", 100, 5)
print(item1.result())
print(item1.name, item1.price, item1.quantity) 
print(Item.payRate)
print(item1.payRate)
print(Item.__dict__) # all the attributes of class level
print(item1.__dict__) # all the attributes of instance level

item1.discount()
print(item1.price) # 80.0