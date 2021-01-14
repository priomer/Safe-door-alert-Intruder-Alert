from BoltIot importBolt, Sms
import json, time

API_KEY = "__"
DEVICE_ID = "__"

SID = "__"
AUTH_TOKEN = "__"
FROM_NO = "__"
TO_NO = "__"

mybolt= Bolt(API_KEY, DEVICE_ID)
sms = Sms(SID, AUTH_TOKEN, FROM_NO, TO_NO)
while True:
