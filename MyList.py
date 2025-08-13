import random

class MyList(list):
    'customized list with some randomness'
    
    def __init__(self, lst = []):
        for item in lst:
            self.append(item)

    def __sub__(self, anotherList):
        diffList = set()
        for item in anotherList:
            for i in range(0,len(self)):
                o = self[i]
                if item != o:
                    diffList.add(o)

        return list(diffList)


    def choice(self):
        'return item from list chosen uniformly at random'
        return random.choice(self)
    
