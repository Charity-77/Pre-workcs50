def main():
    time = input("What time is it? ")  # keep as string, not .split()
    convert_time = convert(time)

    if 7 <= convert_time < 8:
        print("breakfast time")
    elif 12 <= convert_time < 13.5:
        print("lunch time")
    elif 18 <= convert_time < 19:
        print("dinner time")


def convert(time):
    x, y = time.split(":")
    x = int(x)
    y = int(y)
    return x + y / 60  # convert minutes into decimal


if __name__ == "__main__":
    main()

