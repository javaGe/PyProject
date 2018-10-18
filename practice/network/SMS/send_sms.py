#!/usr/bin/env python
# -*- coding: utf-8 -*-

from twilio.rest import Client
# Your Account SID from twilio.com/console
account_sid = "ACf28cacb30364d4a804199893780e7348"
# Your Auth Token from twilio.com/console
auth_token  = "be1e711a203191f8101170ffcd01eb55"
client = Client(account_sid, auth_token)
message = client.messages.create(
# 这里中国的号码前面需要加86
to="+8615813081353",
from_="+18506608337",
body="中文可以发送吗!")
print(message.sid)