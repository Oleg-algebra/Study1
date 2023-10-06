import base64
base64_message='VW5kZXIgY2xvdWQgYW5kIHVuZGVyIHN0YXIs'
message_bytes=base64.b64decode(base64_message)
message=message_bytes.decode('ascii')
print(message)