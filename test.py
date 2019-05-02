maps = [
    ["РЕН ТВ", 0, 2, 0, {"price_to_buy" : 100, "price_to_build_branch" : 50, "price_branch" : [8, 40, 100, 300, 600]}],
    ["МАГНИТ", 0, 1, 0, {"price_to_buy" : 50, "price_to_build_branch" : 50, "price_branch" : [1, 10, 30, 90, 200]}],
    ["ПЯТЕРОЧКА", 0, 1, 0, {"price_to_buy" : 60, "price_to_build_branch" : 50, "price_branch" : [4, 15, 60, 180, 450]}],
    ["АШАН", 0, 1, 0, {"price_to_buy" : 70, "price_to_build_branch" : 50, "price_branch" : [6, 20, 80, 200, 600]}],
    ["BBC" , 0, 2, 0, {"price_to_buy" : 110, "price_to_build_branch" : 50, "price_branch" : [12, 50, 150, 350, 650]}],    
    ["ПЕРВЫЙ КАНАЛ", 0, 2, 0, {"price_to_buy" : 90, "price_to_build_branch" : 50, "price_branch" : [7, 30, 90, 250, 550]}],
]

for i in range(1, 9):
    for j in range(len(maps)):
        if(i == maps[j][2]):
            print(maps[j][0])