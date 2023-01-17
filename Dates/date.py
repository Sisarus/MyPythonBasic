from datetime import datetime
from datetime import date

print(datetime.now())
print(date.today())
print(datetime.now().time())
print(datetime.now().year)
print(datetime.now().month)
print(datetime.now().day)

now = datetime.now()
print(now)


print(now.strftime("%d/%m/%Y/ %H:%H:%S"))
print(now.strftime("%d/%B/%Y/ %H:%H:%S"))
print(now.strftime("%d/%b/%Y/ %H:%H:%S"))
print(date.today().strftime("%d-%m-%Y"))
print(date.today().strftime("%d-%B-%Y"))
