x = 0

while x < 10:
    print(f"x is {x}")
    # x = x + 1
    x += 1    # infinite loop without this
    if x > 4:
        break

print("hello world")
