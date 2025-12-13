import time

wait_time = 1
max_attempts = 5
currAttempt = 1

while currAttempt < max_attempts:
    print(f"Your current attempt is {currAttempt} - taken time {wait_time}")
    time.sleep(wait_time)
    wait_time *= 2
    currAttempt += 1
    
