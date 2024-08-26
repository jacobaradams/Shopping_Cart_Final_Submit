class ItemToPurchase:
    def __init__(self, item_name = 'none', item_price = 0, item_quantity = 0):
        self.item_name = str(item_name)
        self.item_price = float(item_price)
        self.item_quantity = int(item_quantity)
        self.item_total_cost = self.item_price * self.item_quantity
    def print_item_cost(self):
        item_total_cost = self.item_price * self.item_quantity
        print(f'{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${self.item_total_cost:.2f}')
        return

Item1 = ItemToPurchase('chocolate chips', 3, 1)
Item2 = ItemToPurchase('bottled water', 1, 10)
print('         TOTAL COST:')
Item1.print_item_cost()
Item2.print_item_cost()
print(f'        Total: ${(Item1.item_total_cost + Item2.item_total_cost):.2f}')

class ShoppingCart:
    def __init__(self, customer_name = 'none', current_date = 'January 1, 2020'):
        self.customer_name = str(customer_name)
        self.current_date = str(current_date)
    cart_items = {}
    def add_item(self):
        item_to_add = ItemToPurchase(input(), input(), input())
        self.item_description = input()
        self.cart_items[item_to_add.item_name] = [item_to_add.item_price, item_to_add.item_quantity, self.item_description]

    def remove_item(self):
        item_to_remove = input()
        if item_to_remove in self.cart_items.keys():
            self.cart_items.pop(item_to_remove)
        else:
            print('Item not found in cart. Nothing removed.')
    def modify_item(self):
        item_to_modify = ItemToPurchase(input(), input(), input())
        if item_to_modify.item_name in self.cart_items.keys():
            name_change = input('Change name? Y or N:')
            if name_change == 'Y':
                self.cart_items.pop(item_to_modify.item_name)
                self.cart_items[input()] = [item_to_modify. item_price, item_to_modify.item_quantity]
            else:
                self.cart_items[item_to_modify.item_name] = [item_to_modify.item_price, item_to_modify.item_quantity]
            modify_description = input('Add description? Y or N:')
            if modify_description == 'Y':
                self.cart_items[item_to_modify.item_name][2] = input()
        else:
            print('Item not found in cart. Nothing modified.')
    def get_num_items_in_cart(self):
        num_items = 0
        for key in self.cart_items.keys():
            num_items += self.cart_items[key][1]
        return num_items
    def get_cost_of_cart(self):
        total_cost = 0
        for key in self.cart_items.keys():
            total_cost += self.cart_items[key][0] * self.cart_items[key][1]
        return '{:.2f}'.format(total_cost)
    def print_total(self):
        if self.cart_items == {}:
            print('Shopping Cart Is Empty')
        else:
            print(f'{self.customer_name}\'s Shopping Cart - {self.current_date}')
            print(f'      Number of Items: {self.get_num_items_in_cart()}')
            for key in self.cart_items.keys():
                this_item = ItemToPurchase(key, self.cart_items[key][0], self.cart_items[key][1])
                print('    ', end = '')
                this_item.print_item_cost()
                print(f'        Total: {self.get_cost_of_cart()}')




MyCart = ShoppingCart('Jacob', 'Today')
MyCart.add_item()
MyCart.add_item()
print(MyCart.get_num_items_in_cart())
print(MyCart.get_cost_of_cart())
MyCart.print_total()
print(MyCart.cart_items)





