"""Student Id = 20CE063
    Student name = Preet Padariya"""
# Write a Python script to merge two Python dictionaries.
Marks1 = {
    'Preet' : 90,
    'Meet' : 98,
    'Jeet' : 88,
    'Rahul' : 82
}

Marks2 = {
    'Dev' : 87,
    'Shyam' : 79,
    'Karan' : 83,
    'Ruchit' : 92
}

print("First Dictionary :",Marks1) #Printing Marks of Marks1 dictionary
print("Second Dictionary :",Marks2) #Printing Marks of Marks2 dictionary
Marks2.update(Marks1) #Now Marks2 hase both marks of 1 and 2
print("Merging first and second Dictionary : ",Marks2) #Printing Marks of mergered Marks1 and Marks2 dictionary
