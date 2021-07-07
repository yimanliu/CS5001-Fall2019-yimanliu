import random

if __name__ == '__main__':
    lastNumber = -1
    count = 0;
    while True:
        next_num = random.randint(0, 99)
        print(next_num)
        if lastNumber > 90:
            count += 1
            if count == 2:
                break;
        lastNumber = next_num

    print(str)
