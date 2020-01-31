minerals_dict= {
    "coke": 25,
    "water": 28,
    "fanta": 23,
    "mi wadi": 15
} 

cereal_dict= {
    "weetabix": 18,
    "porridge": 17,
    "coco pops": 12,
    "cornflakes": 8
}

intfood_dict= {
    "rice": 25,
    "pasta": 22,
    "noodels": 30,
    "cury powder": 19
}

freshmeat_dict= {
    "chicken breast": 8,
    "sausages": 14,
    "steak mince": 12,
    "turkey burgers": 7
}

#Method 
def check_stock_levels(stock_dict,item):
    for values in stock_dict:
        if values == item:
            return stock_dict[values]

#Call
check_item = "water"
mineral_stock = check_stock_levels(minerals_dict, check_item)
print(check_item,":", mineral_stock)

check_item = "rice"
int_stock = check_stock_levels(intfood_dict, check_item)
print(check_item,":", int_stock)

check_item = "pasta"
int_stock = check_stock_levels(intfood_dict, check_item)
print(check_item,":",int_stock)

check_item = "fanta"
mineral_stock = check_stock_levels(minerals_dict, check_item)
print(check_item,":", mineral_stock)