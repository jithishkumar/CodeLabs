print('Enter the Hours')
hours = input('')
print('Enter hourly rate')
hourly_rate = input()

try:
    hours = float(hours)
    hourly_rate = float(hourly_rate)
except:
    print('Please enter a numerical value')
    
gross_pay = hours * hourly_rate
print(gross_pay)
