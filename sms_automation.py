from twilio.rest import Client

# Twilio credentials
account_sid = "YOUR_ACCOUNT_SID"
auth_token = "YOUR_AUTH_TOKEN"
client = Client(account_sid, auth_token)

message = client.messages.create(
    body="Hello! This is a test message from Python.",
    from_="+1234567890",   # Your Twilio phone number
    to="+91XXXXXXXXXX"     # Receiver's number
)

print("Message sent! SID:", message.sid)