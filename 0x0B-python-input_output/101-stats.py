#!/usr/bin/python3
"""reads stdin line by line and computes metrics
"""


def print_stats(filesize, status_stats):
    """prints stats collected
    """
    print("File size: {}".format(filesize))
    for code in status_stats:
        if status_stats[code] > 0:
            print("{}: {}".format(code, status_stats[code]))


def main():
    """main function
    """
    filesize = 0
    status_codes = {
            200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0
            }
    i = 0
    try:
        while True:
            i += 1
            line = input("")
            data_list = line.split(" ")
            status_in = data_list[-2]
            filesize_in = data_list[-1]
            status_codes[int(status_in)] += 1
            filesize += int(filesize_in)
            if i % 10 == 0:
                print_stats(filesize, status_codes)
    except KeyboardInterrupt as ki:
        print_stats(filesize, status_codes)
        raise


if __name__ == '__main__':
    main()
