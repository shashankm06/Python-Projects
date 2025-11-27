# balance = 5000
# pin = 3225
# attempts = 0

# while attempts < 3:
#     try:
#         enter_pin = int(input("Enter PIN: "))
#     except ValueError:
#         print("PIN must be numbers only!")
#         attempts += 1
#         continue

#     if enter_pin == pin:
#         print("1. Check Balance")
#         print("2. Cash Withdrawal")

#         try:
#             query = int(input("Choose your action (1/2): "))
#         except ValueError:
#             print("Invalid input, numbers only!")
#             continue

#         if query == 1:
#             print("Your balance is:", balance)

#         elif query == 2:
#             amount = float(input("Enter amount: "))
#             if amount <= balance:
#                 balance -= amount
#                 print("Amount successfully withdrawn!")
#             else:
#                 print("Insufficient balance!")

#         else:
#             print("Invalid menu option")

#         break 

#     else:
#         attempts += 1
#         print("Incorrect PIN")

#         if attempts == 3:
#             print("Your card is blocked!")


balance = 5000
# pin = 3225
# attempts = 0

# while attempts < 3:  
#     try: 
#         enter_pin = int(input("enter pin: "))
#     except: ValueError

#     if enter_pin == 3225:
#         print("1. Check Balance")
#         print("2. Cash Withdrawl")
        
#         query = int(input("choose your actions (1/2): "))

#         if query == 1:
#             print(balance)

#         elif query == 2:
#             amount = float(input("Enter amount: "))
#             print("Amount successfully withdrawn, Visit Again!!!")
#             balance = balance - amount

            
#         else:
#             print("invalid input")

#         break

#     else:
#         attempts += 1
#         print("incorrect PIN")

#         if attempts == 3:
#             print("Card Bloacked!!!")





# Trading Profit/Loss Analyzer

# trades = []   

# while True:
#     print("\n Enter Trade Details")
    
#     buy = float(input("Enter Buy Price: "))
#     sell = float(input("Enter Sell Price: "))
#     qty = int(input("Enter Quantity: "))

#     profit = (sell - buy) * qty
#     return_percent = ((sell - buy) / buy) * 100

    
#     trade = {
#         "buy": buy,
#         "sell": sell,
#         "qty": qty,
#         "profit": profit,
#         "return": return_percent
#     }

#     trades.append(trade)

#     print(f"\nProfit/Loss: {profit:.2f}")
#     print(f"Return %  : {return_percent:.2f}%")

#     choice = input("\nDo you want to enter another trade? (y/n): ").lower()
#     if choice != 'y':
#         break


# print("\n Trade Summary: ")
# print("Buy\tSell\tQty\tProfit\tReturn%")
# # print("-------------------------------------------")

# for t in trades:
#     print(f"{t['buy']}\t{t['sell']}\t{t['qty']}\t{t['profit']:.2f}\t{t['return']:.2f}")


# total_pl = sum(t['profit'] for t in trades)
# print("\n-------------------------------------------")
# print(f"Total Net Profit/Loss: {total_pl:.2f}")
# print("===========================================\n")





# from twilio.rest import Client

# # Twilio credentials
# account_sid = "YOUR_ACCOUNT_SID"
# auth_token = "YOUR_AUTH_TOKEN"
# client = Client(account_sid, auth_token)

# message = client.messages.create(
#     body="Hello! This is a test message from Python.",
#     from_="+1234567890",   # Your Twilio phone number
#     to="+91XXXXXXXXXX"     # Receiver's number
# )

# print("Message sent! SID:", message.sid)




# import smtplib
# import ssl
# from email.message import EmailMessage

# EMAIL = "shashankmish96@gmail.com"
# APP_PASSWORD = "XXXXXXXXXXX"
# RECIEVER = "24tec2aids175@vgu.ac.in"

# msg = EmailMessage()

# msg["From"] = EMAIL
# msg["To"] = RECIEVER
# msg["Subject"] = "Hello From Python..."

# msg.set_content("This email was sent through python")

# context = ssl.create_default_context()

# with smtplib.SMTP_SSL("smtp.gmail.com",465, context=context)as server:
#     server.login(EMAIL, APP_PASSWORD)
#     server.send_message(msg)