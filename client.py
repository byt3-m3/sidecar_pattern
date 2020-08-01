import requests

def main():
    response = requests.get("http://udev.bits.local:8080/register?fname=jack&lname=doe")


if __name__ == "__main__":
    main()
