import csv
import sys

class Cookies:

    def __init__(self, filename, date):
        self.filename = filename
        self.date = date
        # Read file
        self.read_file()
        # Get file info into list
        self.get_cookie_and_time()
        # Get cookie count for date
        self.cookies_count()
        # Get cookies with highest count
        self.get_cookies_with_highest_count()

    # Read csv file into dictionary
    def read_file(self):
        self.cookie_file = []
        with open(self.filename, 'r') as file:
            csv_file = csv.DictReader(file)
            for dict in csv_file:
                self.cookie_file.append(dict)
        return self.cookie_file

    '''
        Extract cookie and date from original list with a dictionary inside
        for a new list with just cookie and date
    '''
    def get_cookie_and_time(self):
        self.cookie_file_info = []
        for cookie_dict in self.cookie_file:
            temp_list = []
            for key, val in cookie_dict.items(): temp_list.append(val)
            self.cookie_file_info.append(temp_list)
        return self.cookie_file_info

    # Get count of each cookie for day
    def cookies_count(self):
        self.cookie_count = {}
        for cookie in self.cookie_file_info:
            curr_day = cookie[1]
            curr_day = curr_day[:10]
            if cookie[0] not in self.cookie_count and curr_day == self.date:
                self.cookie_count[cookie[0]] = 1
            elif cookie[0] in self.cookie_count and curr_day == self.date:
                temp_count = self.cookie_count[cookie[0]]
                temp_count += 1
                self.cookie_count[cookie[0]] = temp_count
        return self.cookie_count

    # Return cookies with highest count
    def get_cookies_with_highest_count(self):
        self.cookies_with_highest_count = []
        max_count = float('-inf')
        for cookie, count in self.cookie_count.items():
            if count > max_count: max_count = count
        for cookie, count in self.cookie_count.items():
            if count == max_count: self.cookies_with_highest_count.append(cookie)
        for cookie in self.cookies_with_highest_count: print(cookie)
        return self.cookies_with_highest_count

def main():
    if len(sys.argv) < 3:
        print("Please enter filename and date as arguments")
        exit(0)
    # Get filename and date as arguments from command line
    filename, date = sys.argv[1], sys.argv[2]
    cookie = Cookies(filename, date)

if __name__ == "__main__":
    main()
