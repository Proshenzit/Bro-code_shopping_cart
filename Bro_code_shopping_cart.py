item = input("what   item   would  you like to  buy?: ")
price = float(input("what is the price?: "))
quantitiy = int ( input("how many would you like?: "))

total = price*quantitiy

print(f"you  have  bought {quantitiy} x {item}/s ")
print(f"your  total is: ${round(total,2)}")
