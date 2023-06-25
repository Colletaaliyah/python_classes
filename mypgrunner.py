from  mytestpostgres import insert_product,fetch_data

# p1=insert_product(('waffles',25,40,10))
# print(p1)

# data = fetch_data("products")
# print(data)


#request user for 4 inputs,insert to the products table and 
# return only that record with its ID.Print that record.
name=input("Enter the product name: ")
buying_price=float(input("Enter buying price: "))
selling_price=float(input("Enter selling price: "))
quantity=int(input("Enter the quantity: "))
 
data=(name,buying_price,selling_price,quantity)
insert_product(data)
res=fetch_data('products')
print(res[-1])
# print(newrecord)
# data = fetch_data("products")
# print(data)

