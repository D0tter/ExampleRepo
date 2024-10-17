def test_password(x):
    print(x)
    
#This is how we learned to concatenate strings in the ITF+ class.
a = "String 1"
b = "String 2"
print("a =" + a + " and  b=" + b)

#This syntax utilizes the concept of the f-string, which makes things easier. No + sign needed!
x = "String 3"
y = "String 4"
print(f"x = {x} and y = {y}")

#We could also use an f-string like this:
print("c = {c} and d = {d}".format(c=1, d=2))

job_list = {'John': 'Doctor', 'Jane': 'Engineer', 'Jim': 'Teacher'}

for name, job in job_list.items():
    print(f"{name} is a {job}")

Password = 'SuperSecretAdminPass'
test_password(Password)