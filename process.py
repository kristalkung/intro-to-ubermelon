log_file = open("um-server-01.txt")


def sales_reports(log_file):
    """Prints sales reports for Monday"""
    for line in log_file:
    # loop through each item in log_file
        line = line.rstrip()
        # removes trailing characters at the end of each line
        day = line[0:3]
        # sets variable day as the first 3 characters of line
        if day == "Mon":
        # if the day is Monday
            print(line)
            #prints the log


sales_reports(log_file)
