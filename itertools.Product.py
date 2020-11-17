from itertools import product
recipies = ["chicken","mutton","fish"]
dishes = ["biryani","curry","fried rice"]
dishes = list(product(recipies, dishes))
print(dishes)
for dish in dishes:
    print (f"{dish[0]} - {dish[1]}")
print ( [f"{dish[0]}-{dish[1]}" for dish in dishes]    )
