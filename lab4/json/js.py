import json

with open("sample-data.json", "r") as file:
    data = json.load(file)

print("Interface Status")
print("=" * 72)
print(f"{'DN':<50} {'Description':<20} {'Speed':<8} {'MTU':<6}")
print("-" * 48,"", "-" * 20,"", "-" * 6,"", "-" * 6)

for i in data["imdata"]:
    attributes = i["l1PhysIf"] ["attributes"] 
    dn = attributes.get("dn", " ")
    descr = attributes.get("descr", " ")
    speed = attributes.get("speed", " ")
    mtu = attributes.get("mtu", " ")

    print(f"{dn:<50} {descr:<19} {speed:<9} {mtu:<6}")