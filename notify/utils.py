import requests
from django.conf import settings

def send_line_notify(message):
    line_notify_token = settings.LINE_NOTIFY_TOKEN
    url="https://notify-api.line.me/api/notify"
    headers={"Authorization": f"Bearer {line_notify_token}"}
    data={"message": message}
    response=requests.post(url, headers=headers, data=data)
    if response.status_code==200:
        print("Send Line Notify Success")
    else:
        print("Send Line Notify Error")