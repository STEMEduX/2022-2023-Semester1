##
## cal.py

def main():
    sum = 0
    count = 1

    while True:
        sum = sum + count
        count = count + 1

        if count > 100:
            break;


    print("Sum: ", sum)

main()

