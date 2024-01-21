print(type("hallo"))
print(type(3))
print(type(3.2))
print(type("17"))
print('''"Oh no", she exclaimed, "Ben's bike is broken!"''')
print(42000)
print(42,000)
print(3.14, int(3.14))
print(type(str(123.45)))
message = "What's up, Doc?"
n = 17
pi = 3.14159

print(message)
print(n)
print(pi)
print(len("hello"))
minutes = 645
hours = minutes / 60
print(hours)
print(7 / 4)
print(7 // 4)
quotient = 7 // 3     # This is the integer division operator
print(quotient)
remainder = 7 % 3
print(remainder)
n = input("Please enter your name: ")
print("Hello", n)
str_seconds = input("Please enter the number of seconds you wish to convert")
total_secs = int(str_seconds)

hours = total_secs // 3600
secs_still_remaining = total_secs % 3600
minutes =  secs_still_remaining // 60
secs_finally_remaining = secs_still_remaining  % 60

print("Hrs=", hours, "mins=", minutes, "secs=", secs_finally_remaining)


