# grocery_string = "item:apples,quantity:4,price:1.50\n"
# split_item = grocery_string.split(",")
# print split_item

# item_data = split_item[0]
# print item_data

# item = item_data.split(":")
# print item[1]

# my_name = "Sonia"
# print list(my_name)

# numbers = "1,2,3,4,5"
# numberslist = numbers.split(",")
# print numberslist 

# for numbers in numberslist:
#     int(numbers)
#     print numbers

# suess = "one fish two fish red fish blue fish"
# print suess.split("fish")

grocery_string = "item:apples,quantity:4,price:1.50\n"
def string_split(grocery_string):

#this function splits the items in the string grocery_string 
    split_item = grocery_string.split(",") 
    quantity_data = split_item[1]
    quantity = quantity_data.split(":")
    real_quantity = int(quantity[1])
    price_data = split_item[2]
    price = price_data.split(":")
    real_price = float(price[1].strip())
    return (real_quantity, real_price)

def bill(quantity, real_price):
    #this function will get the bill total for each item * quantity
    total_bill = real_quantity * real_price
    return total_bill




grocery_list = ["item:apples,quantity:4,price:1.50\n",
                "item:pears,quantity:5,price:2.00\n",
                "item:cereal,quantity:1,price:4.49\n"]

total_bill = 0 #must be named outside of the for loop 

for item in grocery_list:
 #turns the list into several strings, applies the function string_split
 #and applies the bill function
    real_quantity, real_price = string_split(item)
    my_bill = bill(real_quantity, real_price)
    print my_bill
    total_bill += my_bill #adds total_bill to each total in my_bill

print total_bill #prints the total for all of the items
