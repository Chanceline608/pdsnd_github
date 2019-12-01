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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while true:
          city = input("\n which city would you like to filter by? chicago,newyork city,washington(DC)?\n").lower().strip()
            if city in ('chicago','newyork city','washington').keys():
                break
            else:
                 print('Please type the full name of the city. In case of Washington DC, you should type it without "DC" part\n')
    print(city.title() + ' is chosen!\n')  
                
            
    # TO DO: get user input for month (all, january, february, ... , june)
    while true:
    month = input("\n which month would you like to filter by? january,february,march,april,may,june or  type in 'all' if you have no          choice?\n").lower().strip()
    if month in('january','february','march','april','may','june','all',):
        break
    else: 
        print("it doesn't match!,try again.")
  print(month.title() + ' is chosen!\n')
        

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
   while true:
    day = input("\nwhich day are you looking for? sunday,monday,tuesday,wednesday,thursday,friday,saturday or type in 'all' if you don't have a choice?\n").lower().strip()
    if day in('sunday','monday','tuesday','wednesday','thursday','friday','saturday','all'):
        break
       else:
            print("it doesn't match!,try again.")
  print(day.title() + ' is chosen!\n')
            
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
    df = pd.read_csv(CITY_DATA[city])
    df['start time'] = pd.to_datetime(df['start  time'])
    df['month'] = df['start time'].dt.month
    df['day_of_week'] = df['start time'].dt.weekday_name
    df['hour'] = df['start time'].dt.hour
    if month != 'all':
        month = MONTHS.index
        (month)+1
 
        df = df[df['month'] == month]
        if day != 'all':
            df[df['day_of_week'] == day.title()] 
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    favoured_month = df['month'].mode()[0]
    print('the most common month is:',favoured month)
   


    # TO DO: display the most common day of week
    favoured_day = df['the_day_of_week'].mode()[0]
    print('the most common day is:',favoured day)


    # TO DO: display the most common start hour
    df['hour'] = df['start time'].dt.hour
    favoures_hour = df['hour'].mode()[0]
    print('the most common hour is at:',favoured_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['start station'].value_counts().idxmax()
    print('the most commonly used start station is:',start_station)


    # TO DO: display most commonly used end station
    end_station = df['end station'].value_counts().idxmax()
    print('the most commonly used end station is:',end_station)


    # TO DO: display most frequent combination of start station and end station trip
    combination_station = df.groupby(['start station','end station']).count()
    print('\n the most commonly used combination of start station and end station trip is:'start_station,"&",end_station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    Total_travel_time = sum(df['trip duration'])
    print('the total travel time is:',Total_travel_time/86400,"days")


    # TO DO: display mean travel time
    Mean_travel_time = df['trip duration'].mean()
    print('the mean travel time is:',Mean_travel_time/60,"minutes")
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['user type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender
    try:
    gender_types = df['gender'].value_counts()
    print('\n gender types:\n, gender_types)
          except keyError:
          print("\n gender types are:\n No data available for this month.")
          


    # TO DO: Display earliest, most recent, and most common year of birth
          try:
          earliest_year = df['birth year'].min()
          print('\n the earliest year is:', earliest_year)
          except keyError:
          print("\n the earliest year is:\n No data available for this month")
          try:
          most_recent_year = df['birth year'].max()
          print('\n the most recent year is:',most_recent_year)
          except keyError:
          print("\n the most recent year is:\n No data available for this month")
          try:
          most_common_year = df['birth year'].value_counts().idxmax()
          print('\n the most common year is:\n',most_common_year)
          except keError:
          print("\n the most common year is:\n No data available for this month")


    print("\nThis took %s seconds." % (time.time() - start_time))
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
