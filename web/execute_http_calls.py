import http.client

host = 'example.com'
port = 80
cid = 'channelID'
uid = 'userID'
frame = 0
signal = 'AAAABBBBCCCC00001111'

# Post signal
conn = http.client.HTTPConnection(host, port)
conn.request('POST', f'/postS.php?CID={cid}&UID={uid}&frame={frame}&signal={signal}')
response = conn.getresponse()
print(response.status, response.reason)
conn.close()

# Get receiver state
conn = http.client.HTTPConnection(host, port)
conn.request('GET', f'/getR.php?CID={cid}&UID={uid}')
response = conn.getresponse()
receiver_state = response.read().decode()
print(receiver_state)
conn.close()

# Get current clock
conn = http.client.HTTPConnection(host, port)
conn.request('GET', f'/getclock.php?CID={cid}&UID={uid}')
response = conn.getresponse()
clock = response.read().decode()
print(clock)
conn.close()