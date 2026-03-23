mail = input("enter mail: ")
has_at = False
has_dot = False
flag = False

for i in mail:
    if i == "@":
        has_at = True
    if i == "." and has_at:
        has_dot = True

if has_at and has_dot and not mail.endswith("."):
    flag = True

print("true" if flag else "not true")
