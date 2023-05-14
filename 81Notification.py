#|----------------------------------------------------------------|
#|Description    :    Notification Program
#|----------------------------------------------------------------|
#|Author         :    ABHISHEK KUMAR, Computer Science Student
#|----------------------------------------------------------------|
#|Organization   :    NMAMIT, Nitte
#|----------------------------------------------------------------|
#|E-Mail         :    abhishekkumar8399@gmail.com
#|----------------------------------------------------------------|
import os
import time
REPEAT_INTERVAL=3600

while True:
    command="osascript -e \'say \"Hey Man drink Water\"\'; osascript -e \'display alert \"Hey Man drink Water\"\'"
    os.system(command)
    time.sleep(REPEAT_INTERVAL)