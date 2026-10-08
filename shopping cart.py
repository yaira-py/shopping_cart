class Item:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    
        
class Cart:
    def __init__(self):
        self.items=[]
        self.coupon_used=False
    def add_to_cart(self,item_obj):
        self.items.append(item_obj)
         
    def get_total(self):
        total=0
        for item in self.items:
            print(f'scanning item {item.name} which cost {item.price}')
            total+=item.price
            if self.coupon_used==True:
                total=total*0.90
                print('Discount applied: -10%')
            print(f'Your final bill: ${total}')

    def apply_discounts(self,code_input):
        if code_input=='save10' and self.coupon_used==False:
            self.coupon_used=True
            print(' coupon applied! 10% off will be deducted at checkout.')

        else:
            print('invalid coupon or coupon code already used!')


try:
    item=input('enter item name : ')
    amount=input('enter price: ')
    amount=int(amount)
    ur_item=Item(item,amount)
    
    my_cart=Cart()
    my_cart.add_to_cart(ur_item)

    my_cart.apply_discounts('save10')
    my_cart.get_total()

except ValueError:
    print('pls enter a whole number')
