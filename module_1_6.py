my_dict={"Aleksei":1983,"Pavel":1984,"Mark":1984}
print("Dict: ",my_dict)
print("Existing value: ",my_dict["Pavel"])
print("Unexisting value: ",my_dict.get("Jesus"))#print unexisting item
my_dict.update({"Alex":1982,"Oleg":1981})#add two new items
print("Deleted value: ",my_dict.pop("Pavel"))#print and delete existing item
print("Modified dict: ",my_dict)
#
my_set={"Hello",1,7043,('y','o','u'),7043,1,"Hello"}
print("Set: ",my_set)
my_set.add("fool")
my_set.add(False)
print("Modified set: ",my_set)
