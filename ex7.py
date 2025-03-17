studentNames=["Lisa","Liam","Leo","Larry","Linda"]
for name in studentNames:
print(f"{name} Evans")
new_name = input("enter a new name")
studentNames.append(new_name)
print("\nreprint the list:")
for name in studentNames:
print(f"{name} Evans")

