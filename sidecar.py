import csv
import time
import logging

logging.basicConfig(level=logging.DEBUG)


def sidecar():
    collection = {}
    logging.info("Starting Sidecar")
    while True:
        time.sleep(2)
        with open('/data/dump.txt', 'r') as f:
            reader = csv.DictReader(f, fieldnames=['fname', 'lname'])

            for row in reader:
                if row.get("fname") not in collection:
                    logging.info(f"Sending Email Sent to '{row.get('fname')}'")
                    collection[row.get("fname")] = row


def main():
    sidecar()


if __name__ == "__main__":
    main()
