a = "Golam Kibria "
b = str(22)
print(a + b) 
########
a = "Golam Kibria {}"
c = 22
print(a.format(c))
######
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
########
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))