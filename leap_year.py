
import datetime  
from datetime import date 
year = int(input())
def findDay(date): 
    day, month, year = (int(i) for i in date.split(' '))     
    born = datetime.date(year, month, day) 
    return born.strftime("%A") 

def is_a_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
if (is_a_leap(year)):
        leap_date = '29 02 '+str(year)
        print(findDay(leap_date))
else:
    offset = year%4
    prev_leap = year - offset
    next_leap = year + offset
    if (is_a_leap(prev_leap) and not(is_a_leap(next_leap))):
        leap_date = '29 02 '+str(prev_leap)
        next_leap = prev_leap + 4
        if (next_leap - year < year - prev_leap):
            if(is_a_leap(next_leap)):
                leap_date = '29 02 '+str(next_leap)
                print('This is not a leap year')
                print('Closest leap year:',next_leap)
                print(findDay(leap_date))
        elif (next_leap - year > year - prev_leap):
                leap_date = '29 02 '+str(prev_leap)
                print('This is not a leap year')
                print('Closest leap year:',prev_leap)
                print(findDay(leap_date))
        
    elif (not(is_a_leap(next_leap)) and not(is_a_leap(prev_leap))):
        offset = year%4
        offset = 4-offset
        leap_date = '29 02 '+str(offset)
        print('This is not a leap year')
        print('Closest leap year:',next_leap)
        print(findDay(leap_date))
                    
        
    else:
        prev_leap = year - offset
        next_leap = year + offset 
        next_leap_date = '29 02 '+str(next_leap)
        prev_leap_date = '29 02 '+str(prev_leap)
        print(findDay(prev_leap_date))
        print(findDay(next_leap_date))