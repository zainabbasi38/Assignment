"""
Problem:
Use pyhton to calculate seconds in a year

"""
DAYS_PER_YEAR = 365
HOURS_PER_DAY = 24
MINS_PER_HOUR = 60
SECS_PER_MIN = 60

def main():
    # print out and calculate seconds in a year
    print("There are "+str(DAYS_PER_YEAR*HOURS_PER_DAY*MINS_PER_HOUR*SECS_PER_MIN)+ " second in year")

if __name__=="__main__":
    main()