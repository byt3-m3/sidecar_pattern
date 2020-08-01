import time
import csv
from bottle import route, run, request
import logging
import os

APP_PORT = os.getenv("APP_PORT")
DEBUG = os.getenv("DEBUG", False)

logging.basicConfig(level=logging.DEBUG)


@route('/register')
def service():
    lname = request.params.get("lname")
    fname = request.params.get("fname")

    with open('/data/dump.txt', 'a+') as f:
        writter = csv.DictWriter(f, fieldnames=['fname', 'lname'])
        writter.writerow({
            'fname': fname,
            'lname': lname
        })
        logging.info(f'Created {fname} {lname}')
    return "Success"


def main():
    logging.info("Starting Server on port 8080")
    run(host='0.0.0.0', port=APP_PORT, debug=DEBUG)


if __name__ == "__main__":
    main()
