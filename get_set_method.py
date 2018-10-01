# Write a map implementation with a get function that lets you retrieve the value of a key at a particular time.

# It should contain the following methods:

# set(key, value, time): sets key to value for t = time.
# get(key, time): gets the key at t = time.
# The map should work like this. If we set a key at a particular time, it will maintain that value forever or until it gets set at a later time. In other words, when we get a key at a time, it should return the value that was set for that key set at the most recent time.

# Consider the following examples:

# d.set(1, 1, 0) # set key 1 to value 1 at time 0
# d.set(1, 2, 2) # set key 1 to value 2 at time 2
# d.get(1, 1) # get key 1 at time 1 should be 1
# d.get(1, 3) # get key 1 at time 3 should be 2
# d.set(1, 1, 5) # set key 1 to value 1 at time 5
# d.get(1, 0) # get key 1 at time 0 should be null
# d.get(1, 10) # get key 1 at time 10 should be 1
# d.set(1, 1, 0) # set key 1 to value 1 at time 0
# d.set(1, 2, 0) # set key 1 to value 2 at time 0
# d.get(1, 0) # get key 1 at time 0 should be 2

import collections
class Mapfunc(object):

    def __init__(self):
        self.dict_set = set()
        self.dicts = collections.defaultdict(dict)

    def set(self, key, value, time):
        new_dict = {time: value}
        self.dicts[key].update(new_dict)

    def get(self, key, time):

        if key in self.dicts:
            if time in self.dicts[key]:
                return self.dicts[key].get(time)
            else:
                max_time = -1
                for times in self.dicts[key]:
                    if times < time:
                        max_time = max(max_time, times)
                return self.dicts[key].get(max_time)

class Solution(object):
    if __name__ == "__main__":
        mymap = Mapfunc()
        type(mymap)
        mymap.set(1,1,0)
        mymap.set(1, 1, 5)
        mymap.set(1, 2, 2)
        print(mymap.get(1, 1))
        print(mymap.get(1, 3))
        print(mymap.get(1, 0))
        print(mymap.get(1, 10)
        mymap.set(1, 1, 0)
        mymap.set(1, 2, 0)
        print(mymap.get(1, 0))
