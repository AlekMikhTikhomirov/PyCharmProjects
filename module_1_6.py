my_dict={"Aleksei":1983,"Pavel":1984,"Mark":1984}
print("Dict: ",my_dict)
print("Existing value: ",my_dict["Pavel"])
print("Unexisting value: ",my_dict.get("Jesus"))#print unexisting value
my_dict.update({"Alex":1982,"Oleg":1981})#add two new items
print("Deleted value: ",my_dict.pop("Pavel"))#print and delete existing value
print("Modified dict: ",my_dict)
#
my_set={"Hello",1,7043,('y','o','u'),7043,1,"Hello"}
print("Set: ",my_set)
my_set.add("fool")#add first item
my_set.add(False)#add second item
my_set.remove(7043)#delete item 7043 from the set
print("Modified set: ",my_set)
