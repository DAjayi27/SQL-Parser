test  = ("Val",33,False)

formatted = []

for val in test:
    if isinstance(val,str):
        formatted.append(f'"{val}"')
    else:
        formatted.append(str(val))



joined  = ",".join(formatted)
out  = f"({joined})"

print(out)