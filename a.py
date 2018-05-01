import math



m = int(input('Please enter the number of minutes parked: '))

if m <= 60:
  x = m/60
  fee = math.ceil(x) * 5
  print('Parking fee for',m,'minutes is $',fee)

elif m>60 and m<=300:
  x = m/60
  fee = math.ceil(x) * 4
  print('Parking fee for',m,'minutes is $',fee)

elif m>300:
  x = m/60
  print (x)
  fee = math.ceil(x) * 3
  print('Parking fee for',m,'minutes is $',fee)

else:
  print('Invalid input')

if 600 <= Time.total_seconds() <= 25200 and Type == 1 :