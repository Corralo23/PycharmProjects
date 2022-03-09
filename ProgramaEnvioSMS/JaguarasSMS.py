from twilio.rest import Client


#Your Account SID from twilio.com/console
account_sid = "ACfbe0b6709f5a3ff9082f03a3c29192a1"
#Your Auth Token from twilio.com/console
auth_token = "b24300e020356fad375caa15ca0ef8e5"
client = Client(account_sid, auth_token)

message = client.messages.create(
    to=("+5554999432585", "+5521999688993", "+5521981053925", "+5551997971758", "+5551981148658"),
    from_="+18065152715",
    body='Faz 84 anos que não fazemos mais um churrasco....vocês só querem festa e pegação hahahaha.' )
print(message.sid)