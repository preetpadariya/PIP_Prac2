"""Student Id = 20CE063
    Student name = Preet Padariya"""
# Write a Python script to check whether a given key already exists in a dictionary.
def check(a):
    if a in Disk1:
         print("given key already exists in a dictionary.")
    else:
         print("given key not exists in a dictionary.")

Disk1 = {
    "ID" : "20CE063",
    "Name" : "Preet",
    "Marks" : "90",
    "Skills" : ['Python','HTML','CSS','Kotlin']
}
b = input("Enter any key name: ")
check(b) #This will check the inpuct as key exists or not
