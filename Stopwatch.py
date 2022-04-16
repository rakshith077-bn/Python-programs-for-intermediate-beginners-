import time

print("Press the ENTER key to start the stopwatch")
print("Press the CTRL + C keys to stop the stopwatch")

while True:
    try:
        input("Enter your choice of operation: ")
        start_time = time.time()
        print("Stopwatch started...")

    except KeyboardInterrupt:
        print("Stopping our stopwatch......")
        end_time = time.time()
        print("The total time: ", round(end_time - start_time, 2), "seconds")
        print("Thank you for using this simple python program that depicts a stopwatch")
