N_Hours = 0
Incremented_pay = 0

print('Enter the Hours')
hours = input('')
print('Enter hourly rate')
hourly_rate = input()

try:
    hours = float(hours)
    hourly_rate = float(hourly_rate)
except:
    print('Please enter a numerical value')
    
if hours > 40:
    Incremented_hourly_rate = hourly_rate * 1.5
    Incremented_pay = Incremented_hourly_rate * (hours-40)
    N_Hours = 40
else:
    N_Hours = hours
    
Normal_gross_pay = N_Hours * hourly_rate
gross_pay = Normal_gross_pay + Incremented_pay
    
print(gross_pay)
