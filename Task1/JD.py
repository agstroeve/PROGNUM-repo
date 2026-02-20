Y = eval(input("Enter the year of your birth: "))
M = eval(input("Enter the month of your birth: "))
D = eval(input("Enter the day of your birth: "))
JD = 367*Y -7*(Y+(M+9)/12)/4 - 3*((Y+(M-9)/7)/100 + 1)/4 + (275*M)/9 + D + 1721029-0.5
Y2 = eval(input("Enter the current year: "))
M2 = eval(input("Enter the current month: "))
D2 = eval(input("Enter the current day: "))
JD2 = 367*Y2 -7*(Y2+(M2+9)/12)/4 - 3*((Y2+(M2-9)/7)/100 + 1)/4 + (275*M2)/9 + D2 + 1721029-0.5
Diff = JD2 - JD
print(" Your age in days is", Diff,)