#
# words=("spam","white","black")
#
# # words[0]="red"
# print(words[2])
#
# persom=("alice",30,'engineer')
#
# name,age,profession=persom
#
# print(name,"s", "profession is",profession,"and she is",age,"years old")

# Dictionaries

# contact_info={
#     "alice":"555-1234",
#     "bob":"5559875"
# }
#
# alice_phone=contact_info['alice']
# print(alice_phone)
#
# contact_info['daris']='045875875'
#
# print(contact_info)
#
# # del contact_info["bob"]
# # print(contact_info)
#
# keys=contact_info.keys()
# print(keys)
#
# values=contact_info.values()
# print(values)
#
# items=contact_info.items()
# print(items)

# contact_info={
#     "alice":{
#         "phone":"555-1111",
#         "email":"alice@gmail.com"
#     }
#
# }

contact_info={
    "alice":("555-1111","alice@gmail.com")


}
alice_info=contact_info['alice']
phone=alice_info[0]
print(alice_info)
a