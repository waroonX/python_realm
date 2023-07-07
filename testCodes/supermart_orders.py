from collections import OrderedDict as od

def summarise_orders(order_list: list) -> None:
    order_dict = od()
    for order in order_list:
        item, count = order[:order.rindex(' ')], int(order[order.rindex(' ')+1:])
        if item in order_dict:
            order_dict[item] = order_dict.get(item) + count
        else:
            order_dict[item] = count
    for item, count in order_dict.items():
        print(item,count)

if __name__ == "__main__":
    n = int(input())
    
    order_list = []
    for _ in range(n):
        order_list.append(input())
        
    summarise_orders(order_list)