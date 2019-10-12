from twilio.rest import Client

account_sid = 'insert your account sid here'
auth_token = 'insert your token here'
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         from_='whatsapp:+14155238886',
         body='Reporte octubre',
         to='whatsapp:+56995863640',
         media_url=['https://i.ibb.co/LSN1V0x/blog-Como-hacer-un-reporte-de-ventas6.png']
)

print(message.sid)