SALESPERSON_INDEX = 0
INTERNET_INDEX = 1
DORKY_LINE_LENGTH = 80

print("*" * DORKY_LINE_LENGTH)
f = open("orders-by-type.txt")
melon_tallies = {"Musk": 0, "Hybrid": 0, "Watermelon": 0, "Winter": 0}

for l in f:
    # starts looping through orders
    data = l.split("|")
    # splits orders
    melon_type = data[1]
    # saves melon type to a variable
    melon_count = int(data[2])
    # saves melon count to a variable
    melon_tallies[melon_type] += melon_count
    # counts melons and saves to dict

f.close()
# closes file
melon_prices = {"Musk": 1.15, "Hybrid": 1.30,
                "Watermelon": 1.75, "Winter": 4.00}
# make prices dict
total_revenue = 0
# init revenue accumulator
for melon_type in melon_tallies:
    price = melon_prices[melon_type]
    revenue = price * melon_tallies[melon_type]
    total_revenue += revenue
    # print("We sold %d %s melons at %0.2f each for a total of %0.2f" % (melon_tallies[melon_type], melon_type, price, revenue))
    print(
        f"We sold {melon_tallies[melon_type]} {melon_type} melons at {price:.2f} each for a total of {revenue:.2f}")
print("******************************************")
f = open("orders-with-sales.txt")
sales = [0, 0]
for line in f:
    d = line.split("|")
    if d[1] == "0":
        sales[0] += float(d[3])
    else:
        sales[1] += float(d[3])
print(f"Salespeople generated ${sales[1]:.2f} in revenue.")
print(f"Internet sales generated ${sales[0]:.2f} in revenue.")
if sales[1] > sales[0]:
    print("Guess there's some value to those salespeople after all.")
else:
    print("Time to fire the sales team! Online sales rule all!")
print("******************************************")
