# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest import Client
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACf28cacb30364d4a804199893780e7348"
auth_token = "be1e711a203191f8101170ffcd01eb55"
client = Client(account_sid, auth_token)
call = client.calls.create(
to="+8615813081353",
from_="+18506608337",
url="http://demo.twilio.com/docs/voice.xml",
method="GET",
status_callback="https://www.myapp.com/events",
status_callback_method="POST",
status_callback_event=["initiated", "ringing", "answered", "completed"]
)
print(call.sid)