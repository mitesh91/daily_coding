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
