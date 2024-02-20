hour = 12
minute = 0

if 6 < hour < 11:
    print("Good morning!")
elif hour < 14:
    print("Good day!")
    if minute == 0:
        print("Lunch time!")
elif hour < 18:
    print("Good afternoon!")
elif hour < 22:
    print("Good evening!")
else:
    print("Good night!")


count = 10
print("Begin countdown")
while count:  # 0 is falsy and will break the loop
    print(count)
    count -= 1  # count = count - 1
print("Happy new year!")

my_str = "hello world"
for char in my_str[:5]:
    print("Next iteration")
    print(char)

for i in range(5):
    if i == 3:
        break
    print(i)

for i in range(5, 12):
    if i % 2 == 1:
        continue
    print(i)

for i in range(1, 11, 2):
    print(i)
