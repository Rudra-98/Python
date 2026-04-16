import gc
#handling circular references
class GarbageCollection:
    def __init__(self,name):
        self.name = name
        print(f"{self.name} object created")


    def __del__(self):
        print(f"{self.name} object deleted")



obj1 = GarbageCollection("obj1")
obj2 = GarbageCollection("obj2")

#circular reference
obj1= obj2
obj2 = obj1

#using gc to manage circular reference
gc.collect()






