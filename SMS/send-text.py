from twilio.rest import Client

# Find these values at https://twilio.com/user/account
account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXX"
auth_token = "a1XXXXXXXXXXXXXXXXXXXXXXXXX"
client = Client(account_sid, auth_token)

#to = "phone number to which you want to send a text"
#from = "phone number given by twilio"
message = client.api.account.messages.create(to="+190XXXXXXXX",
                                             from_="+1903776XXXX ",
                                             body="Hello there!")
