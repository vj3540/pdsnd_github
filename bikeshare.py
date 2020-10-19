import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data for Chicago, New York City and Washington!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Would you like to see data for Chicago, New york city or Washington? \n")
        city = city.lower()
        if city in ['chicago', 'new york city', 'washington']:
            break
        else:
            print("Invalid City.  Please enter a valid city i.e. Chicago, New York city or Washington")

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Which of the first 6 months would you like to filter data by i.e. January, February, March, April, May, June or All?\n")
        month = month.lower()
        if month in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
            break
        else:
            print("Invalid Month. Please enter a valid month from the first 6 months or 'All'\n")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Which day of the week would you like to filter by? Specify a day or 'All' for the whole week\n")
        day = day.lower()
        if day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
            break
        else:
            print("Invalid Day. Please enter a valid day of the week or 'All'\n")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("The most common month is: ", df['month'].mode()[0], "\n")

    # TO DO: display the most common day of week
    print("The most common day of week is: ", df['day_of_week'].mode()[0], "\n")

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print("The most common start hour is: ", df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""


    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most commonly used start station is: ", df['Start Station'].mode()[0], "\n")

    # TO DO: display most commonly used end station
    print("The most commonly used end station is: ", df['End Station'].mode()[0], "\n")

    # TO DO: display most frequent combination of start station and end station trip
    df['freq_combination'] = df['Start Station'] + " " + df['End Station']
    print("The most frequent combination of start and end station trip is: ", df['freq_combination'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("The total travel time is: ", df['Trip Duration'].sum(), "\n")

    # TO DO: display mean travel time
    print("The mean travel time is: ", df['Trip Duration'].mean(), "\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types_cnt = df.groupby(['User Type'])['User Type'].count()
    print("User Types count: ", user_types_cnt, "\n")

    # TO DO: Display counts of gender
    if city != 'washington':
        gender_cnt = df.groupby(['Gender'])['Gender'].count()
        print("Gender count: ", gender_cnt, "\n")

    # TO DO: Display earliest, most recent, and most common year of birth
        earliest_yob = sorted(df.groupby(['Birth Year'])['Birth Year'])[0][0]
        print("The earier year of birth is: ", earliest_yob, "\n")

        most_recent_yob = sorted(df.groupby(['Birth Year'])['Birth Year'], reverse=True)[0][0]
        print("The most recent year of birth is: ", most_recent_yob, "\n")

        most_common_yob = df['Birth Year'].mode()[0]
        print("The most common year of birth is: ", most_common_yob, "\n")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    # TO DO: Solicit user input and diplay raw data 5 lines at a time

    rows = 1
    while True:
        rd = input("\nWould you like to see 5 lines of raw data? Enter Yes or No.\n")
        if rd.lower() == 'yes':
            print(df.iloc[rows:rows+5])
            rows = rows+5
        elif rd.lower() == "no":
            break
        else:
            rd = input("Invalid response.  Please enter Yes or No:\n")

    #rd = ""
    #while rd.lower() != "yes" or rd.lower()!!="no"


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
