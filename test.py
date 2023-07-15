#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new object --")
my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
my_model.save()
print(my_model)
# from datetime import datetime

# time_created = datetime.now()

# 2023-07-15 14:19:18.874658
# 2023-07-15T14:19:18.874658
# 2023-07-15 14:19:18.874658
# <class 'datetime.datetime'>
# <class 'str'>
# <class 'datetime.datetime'>
# print(type(time_created))
# print(type(time_created.isoformat()))
# print(type(datetime.fromisoformat(time_created.isoformat())))
