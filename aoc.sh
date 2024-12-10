# Get the current date and year
# If date is between 1st Dec to 25 Dec
# Create directory in the form of
# ./YYYY/dayDD
# where YYYY is the year and DD is the day of the month

# Get the current date
date=$(date +%d)
# Get the current year
year=$(date +%Y)

# Check if the date is between 1st Dec to 25th Dec
if [ $date -ge 1 ] && [ $date -le 25 ]; then
    # Create the directory
    mkdir -p ./$year/day$date
    echo "Directory created: ./$year/day$date"
    # Create the files
    touch ./$year/day$date/test.in
    touch ./$year/day$date/input.in
    touch ./$year/day$date/solution.py
else
    echo "Date is not between 1st Dec to 25th Dec"
fi
