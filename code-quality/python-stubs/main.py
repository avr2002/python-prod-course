from mymodule.core import add, greet
from mymodule.person import Person

result = add(5, '22')  # Error in 2nd number
greeting = greet('Mona')

amit = Person("Amit", '21')  # Error in age
mona = Person("Mona", 22)


print(result)
print(greeting)

print(amit.greet())
print(mona.greet())