import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': '.CSV/chicago.csv',
              'new york city': '.CSV/new_york_city.csv',
              'washington': '.CSV/washington.csv' }

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
    
    while True:
         city = input('Please enter a city (chicago, new york city, washington):\n')
         city = city.lower() #set string to lowercase
         temp = city.replace(" ", "")  #delete spaces
         if city == 'chicago':
             break
         elif temp == 'newyorkcity':
             break
         elif city == 'washington':
             break
         print('plesae enter a valid city')
     
    # TO DO: get user input for month (all, january, february, ... , june)  
    months = ['all','january', 'february', 'march', 'april', 'may', 'june']
    while True:
       
        month = input('Please enter a month (all, january, february, ... , june):\n')
        month = month.lower() #set string to lowercase
        if month in months:
            break
        print('please enter a valid month')
    


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all', 'monday', 'tuseday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    while True:
        day = input('please enter day of week(all, monday, tuesday, ... sunday):\n')
        day = day.lower() #set string to lowercase
        
        if day in days:
            break
        print('please enter a valid day')
    


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
    
    
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
  
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    if not month == 'all':
      
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if not day == 'all':
       
        df = df[df['day_of_week'] == day.title()]
   
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    
    print('Most common month: ', df['month'].value_counts().idxmax())
    

    # TO DO: display the most common day of week
    print('Most common day of week: ', df['day_of_week'].value_counts().idxmax())

    # TO DO: display the most common start hour
    print('Most common start hour: ',df['Start Time'].dt.hour.value_counts().idxmax())
   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
 

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    # TO DO: display most commonly used start station
    
    print('Most commonly used start station: ',df['Start Station'].value_counts().idxmax())
    
    # TO DO: display most commonly used end station
    print('Most commonly used end station: ', df['End Station'].value_counts().idxmax())
  

    # TO DO: display most frequent combination of start station and end station trip
    df['Combination Station'] = df['Start Station'] + df['End Station']
    print('Most requent combination of start station and end station trip: ', df['Combination Station'].value_counts().idxmax())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total travel time', df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print('mean travel time' ,df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('counts of user types:\n' ,df['User Type'].value_counts())
    print('Most common user type: ', df['User Type'].value_counts().idxmax())
    # Counting total of users
    print('counts of users:\n' ,df.iloc[:, :1].count())
    
    # TO DO: Display counts of gender
    if 'Gender' in df:
        print('counts of gender:\n', df['Gender'].value_counts())
        print('Most common gender: ', df['Gender'].value_counts().idxmax())
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        print("Most common year of birth: ",int(df['Birth Year'].value_counts().idxmax()))
        print("Most earliest year of birth: ",int(df['Birth Year'].max()))
        print("Most recent year of birth: ",int(df['Birth Year'].min()))
              
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def Display(df): 
    
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
    if view_data == 'yes':
        start_loc = 0
        while (True):
            print(df.iloc[start_loc:(start_loc+5)])
            start_loc += 5
            view_data = input("Do you wish to continue?:\n ").lower()
            if view_data == 'yes':
                continue
            break
    elif view_data == 'no':
         return
    





def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
           
        Display(df)    
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
