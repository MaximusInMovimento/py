from time import sleep, localtime, strftime

for i in range(5):
    print(strftime("%H:%M:%S", localtime()))
    sleep(1)
