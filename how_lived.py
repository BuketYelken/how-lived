
from datetime import datetime


birthday = datetime.strptime(input("Welcome...\nPLease enter your birth day (d.m.y): "), "%d.%m.%Y")



difference = datetime.now() - birthday
print("\nYou are living since {} time".format(difference))