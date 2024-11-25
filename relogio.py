from datetime import datetime
import time
while True:
    horaa=datetime.now().strftime("%H:%M:%S")
    print(horaa)
    time.sleep(1)
if datetime.now().hour>=16 and datetime.now().minute>=35 and datetime.now()secon