import google.generativeai as geneai
key = "ENTER_YOUR_KEY"
geneai.configure(api_key=key)
model = geneai.GenerativeModel("gemini-2.5-flash")
while True:
    user = input("enter what you want to search or type exit to close")
    if user.lower() == "exit":
        print("bye bye")
        break
    response = model.generate_content(user)
    print("BOT: ", response.text)