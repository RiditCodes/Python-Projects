import schedule
import time

def show_message():
    print("Python is an object-oriented programming language.")
    print('It was developed by Guido van Rossum.')
    print('It was released in 1991.')

schedule.every(1).seconds.do(show_message)

#while 1:
#    schedule.run_pending()
#    time.sleep(1)

for i in range(5):
    schedule.run_pending()
    time.sleep(1)