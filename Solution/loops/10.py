# 10. Exponential Backoff
# Problem: Implement an exponential backoff strategy that doubles the wait time between retries, starting from 1 second, but stops after 5 retries.

import time
a=1
for i in range(1,6):
    input("enter the input:")
    if i==5:
        print("sorry, enough entries")
        break
    time.sleep(a)
    a=a*2

