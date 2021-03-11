class Restaurant(object):
    def __init__(self,flavors='food'):
        self.flavors=flavors
class IceCreamStand(Restaurant):
    def __init__(self,flavors):
        super().__init__(self)
        self.flavors=flavors
    def getflavors(self):
        print(' my flavors'+self.flavors)

feed=IceCreamStand(flavors='ice')
feed.getflavors()
