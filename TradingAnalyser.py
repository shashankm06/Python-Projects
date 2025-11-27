# Trading Profit/Loss Analyzer

trades = []   

while True:
    print("\n Enter Trade Details")
    
    buy = float(input("Enter Buy Price: "))
    sell = float(input("Enter Sell Price: "))
    qty = int(input("Enter Quantity: "))

    profit = (sell - buy) * qty
    return_percent = ((sell - buy) / buy) * 100

    
    trade = {
        "buy": buy,
        "sell": sell,
        "qty": qty,
        "profit": profit,
        "return": return_percent
    }

    trades.append(trade)

    print(f"\nProfit/Loss: {profit:.2f}")
    print(f"Return %  : {return_percent:.2f}%")

    choice = input("\nDo you want to enter another trade? (y/n): ").lower()
    if choice != 'y':
        break


print("\n Trade Summary: ")
print("Buy\tSell\tQty\tProfit\tReturn%")
print("-------------------------------------------")

for t in trades:
    print(f"{t['buy']}\t{t['sell']}\t{t['qty']}\t{t['profit']:.2f}\t{t['return']:.2f}")


total_pl = sum(t['profit'] for t in trades)

print(f"Total Net Profit/Loss: {total_pl:.2f}")

