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
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Which city would you like to analyze?\n')
    while(city.lower() != 'chicago' and city.lower() != 'new york city' and city.lower() != 'washington'):
        city = input('Invalid input! Which city would you like to analyze?\n')


    # get user input for month (all, january, february, ... , june)
    month = input('Which month would you like to analyze? Or all for no filter\n')
    while(month.lower() != 'january' and month.lower() != 'february' and month.lower() != 'march' and month.lower() != 'april' and month.lower() != 'may' and month.lower() != 'june' and month.lower() != 'all'):
        month = input('Invalid input! Which month would you like to analyze? Or all for no filter\n')
    
    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Which day would you like to analyze? Or all for no filter\n')
    while(day.lower() != 'sunday' and day.lower() != 'monday' and day.lower() != 'tuesday' and day.lower() != 'wednesday' and day.lower() != 'thursday' and day.lower() != 'friday' and day.lower() != 'saturday' and day.lower() != 'all'):
        day = input('Invalid input! Which day would you like to analyze? Or all for no filter\n')

    print('-'*40)
    return city.lower(), month.lower(), day.lower()


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
    
    #sets file name based on city
    fileName = 'chicago.csv'
    if(city == 'new york city'):
        fileName = 'new_york_city.csv'
    if(city == 'washington'):
        fileName = 'washington.csv'

    df = pd.read_csv(fileName)

    #converting start time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    #creating month and day columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.strftime('%A')

    #filter to matching month
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        df = df[df['month'] == month]

    #filter to matching day
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...')
    start_time = time.time()

    # display the most common month
    popular_month = df['month'].mode()[0]
    print('\nMost Popular Month:', popular_month)

    # display the most common day of week
    popular_weekday = df['day_of_week'].mode()[0]
    print('\nMost Popular Day of the Week:', popular_weekday)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('\nMost Popular Hour:', popular_hour)

    print("\nThis took %s seconds." % round(time.time() - start_time, 2))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...')
    start_time = time.time()

    # display most commonly used start station
    popular_start = df['Start Station'].mode()[0]
    print('\nMost Popular Start Station:', popular_start)

    # display most commonly used end station
    popular_end = df['End Station'].mode()[0]
    print('\nMost Popular End Station:', popular_end)

    # display most frequent combination of start station and end station trip.
    # this combines every start and end combination into one column, can then check the most common combination by
    # checking the most common combination of start + end.
    df['combination'] = df['Start Station'] + ' to ' + df['End Station']
    popular_combo = df['combination'].mode()[0]
    print('\nMost Popular Combo:', popular_combo)

    print("\nThis took %s seconds." % round(time.time() - start_time, 2))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...')
    start_time = time.time()

    # display total travel time
    total_time = df['Trip Duration'].sum()
    print('\nTotal Travel Duration:', round(total_time, 2), ' seconds')

    # display mean travel time
    average_time = total_time / df['Trip Duration'].count()
    print('\nAverage Travel Duration:', round(average_time, 2), ' seconds')

    print("\nThis took %s seconds." % round(time.time() - start_time, 2))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('\nCustomer types:\n',user_types.to_string())

    # Display counts of gender
    if 'Gender' in df:
        genders = df['Gender'].value_counts()
        print('\nGenders:\n',genders.to_string())
    else:
        print('\nNo genders found in file')

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        birth_years = df['Birth Year']
        print('\nEarliest birth year: ',round(birth_years.min()))
        print('\nMost recent birth year: ',round(birth_years.max()))
        print('\nMost common birth year: ',round(birth_years.mode()[0]))
    else:
        print('\nNo birth years found in file')

    print("\nThis took %s seconds." % round(time.time() - start_time, 2))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
