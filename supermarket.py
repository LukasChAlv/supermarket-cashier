#a function to create the purchase receipt with all the products
def buys():
    cart = []
    while True:
        p_name = input("Please enter a product: ")
        p_price = float(input("Please enter the price: "))
        p_quantity = int(input("Please enter the quantity: "))
        product = {
            "name" : p_name,
            "price" : p_price,
            "quantity" : p_quantity
        }
        cart.append(product)
        while True:
            more = input("Do you wish to buy something more? Y/N ").strip().lower()
            if more == "n":
                return cart
            elif more == "y":
                break
            else: print("Please select a valid option (Y/N)")

#a function that outputs the shopping receipt
def print_ticket(sh_cart):
    total = 0
    print("\n---TICKET---")
    for i in sh_cart:
        print(f"{i["quantity"]} x {i["name"]} - ${i["price"]}")
        total += i["price"] * i["quantity"]
    IVA = (22 * total) / 100
    print(f"------------\nTOTAL: ${total:.2f}\nIVA: ${IVA:.2f}\nTOTAL + IVA: ${(total + IVA):.2f}\n------------")
    return total + IVA

#a function that simulates the checkout process
def process_payment(price):
    while True:
        method = input("\nChoose your payment method: Cash | Card\n--- ").strip().lower()
        if method == "card":
            print("Payment successful.\nThank you for your purchase!")
            break
        elif method == "cash":
            while True:
                try:
                    pay = float(input("Type your amount of money: "))
                    if pay >= price:
                        change = pay - price
                        print(f"Payment successful, Change: ${change:.2f}\n")
                        return
                    else:
                        print("Not enough money, pls try again")
                except ValueError:
                    print("Invalid amount. Please enter a number")
        else: 
            print("\nPlease select a valid payment method: 'Cash' or 'Card' ")
                    

def main():
    shop = buys()
    total = print_ticket(shop)
    process_payment(total)

if __name__ == "__main__":
    main()
