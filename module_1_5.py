immutable_var="Aleksei",40,True,8.1
print("Immutable tuple: ",immutable_var)
#immutable_var[1]=42 shows error "tuples don't support item assignment"
mutable_list=["temporary element",2024,11.09,False]
mutable_list[0]="new_item"
mutable_list[1]=2022
mutable_list[2]=24.02
mutable_list[-1]=True
print("Mutable list: ",mutable_list)