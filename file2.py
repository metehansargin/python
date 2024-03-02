file=open("employee_revenue.txt","r")
data=file.read()
print(data)
print("\n")
print("\n")
print("\n")

lines=data.splitlines()
print(lines) 
print("\n")
print("\n")
print("\n")

string=lines[0]
print(string)
print("\n")
print("\n")

string=string.strip(" ")
print(string)

print("\n")
print("\n")
string=string.lower()
print(string)
string=string.capitalize()
print(string)

split_s=string.split(" ")
print(split_s)

name=split_s[0]
print(name)

for i in split_s:
    if "$" in i:
        averange_deal_size=i.split("$")[0]
print(averange_deal_size)

print("\n")
print("\n")
print("\n")
ids=list(range(0,11))
print(ids)
print(len(ids))
print("\n")
print("\n")

dictionary=dict(zip(ids,string))
print(dictionary)

string=string.strip(" ")
print(string)


