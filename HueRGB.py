import requests

# Replace with your bridge's IP address and API key
bridge_ip = "INSERT BRIDGE IP ADDRESS"
api_key = "INSERT BRIDGE-GIVEN API KEY"

light_id = ___ #Insert light ID you wish to have RGB
x = 0
while x < 65535:
    requests.put(f"http://{bridge_ip}/api/{api_key}/lights/{light_id}/state", json={
    "on": True,
    "sat": 254,
    "bri": 254,
    "hue": x
    })
    print(f"Light Value is... {x}")
    if x > 63000:
        x = 0
    #increment x, skips colors, make as gradual as you wish
    x += 1000