#3. Write a Python program to display calendar?
import calendar

yy = int(input("enter year: "))
mm = int(input("enter month: "))

print(calendar.month(yy, mm))