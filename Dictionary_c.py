"""Student Id = 20CE063
    Student name = Preet Padariya"""
# Write a Python program to sum all the items in a dictionary.
Mark = {
    'Mark1' : 30,
    'Mark2' : 40,
    'Mark3' : 50,
    'Mark4' : 60,
    'Mark5' : 70,
}
sum = 0
for i in Mark.values() : #loop to make sum
    sum = sum +i

print("Sum of values : ",sum) #Print sum
