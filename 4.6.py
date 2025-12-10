import  json

with open("tips.json", "r", encoding="utf-8") as f:
    data = json.load(f)["tips"]

bill_lst = {}

for item in data:
    day = item["day"]
    size = int(item["size"])
    total = float(item["total_bill"])
    bill_lst.setdefault((day,size), []).append(total)

day, size = input().split()
size = int(size)
if (day,size) not in bill_lst:
    print('Invalid')
else:
    total_arr = bill_lst[(day,size)]
    print(f'{sum(total_arr)/len(total_arr):.4f}')
