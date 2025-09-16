from pypresence import Presence
import time

CLIENT_ID = "1417505406477013022"  
RPC = Presence(1417505406477013022)
RPC.connect()

RPC.update(
    state="...",
    details="-",
    start=time.time(),
    large_image="3373403",  # uploaded in "Art Assets" in your app
    large_text="..."
)

while True:
    time.sleep(15)  