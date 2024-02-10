import time

while True:
    time0 = time.time()
    text = input("Enter the text: ")
    time1 = time.time()
    word_count = len(text.split())
    time_taken = time1-time0
    word_per_minute = word_count/time_taken
    print(f"Word count: {word_count}")
    print(f"Word per minute = {word_per_minute}")
    print(f"Time taken: {time_taken}")