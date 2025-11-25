information = {
    "first name": "Aiman",
    "Age": 19,
    "Country": "Pakistan",
    "City": "Lahore",
    "University": "BSU",
    "Degree": "BSCS"
}
print(information)
print(information["first name"])
del information["City"]
x=information.get("Country")
print(x)
information.pop("Degree")
print(information)
information.update({"Age": 20})
print(information)