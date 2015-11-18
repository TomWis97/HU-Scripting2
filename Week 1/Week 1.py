# Weekopdracht 1
import customer

klant1 = customer.Customer("Henk", "01-23456789", "dingen@iets.com")
klant2 = customer.Customer("Jan", "9876543210", "hoi@doei.com")
print(klant1.check_telephone_number())
print(klant2.check_telephone_number())
print(klant1.uid)
print(klant2.uid)

print(klant1.password)
klant1.reset_password()
print(klant1.password)

print(klant1)
print(klant2)