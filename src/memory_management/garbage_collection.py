import gc

gc.enable()


print(gc.collect())


#get garbage collection stats


print(gc.get_stats())

#get unreachable objects

print(gc.garbage)