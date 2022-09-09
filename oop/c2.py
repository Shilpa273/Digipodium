class Cat:

    def __init__(self,breed,color,gender = 'f',age = 1,w=1,h=1,is_tamed=True):
       self.breed= breed
       self.color= color
       self.weight = w
       self.height = h
       self.is_tamed = is_tamed
       self.age = age



    def eat(self,food= 'catfood'):
       print(f'cat is eating {food}')

    def play(self):
        print('cat is playing')

    def sleep(self):
        print('cat is sleeping')

    def info(self):
        print('--'* 15)
        print(f'Breed: {self.breed}')      
        print(f'Age: {self.age}year')
        print(f'Weight: {self.weight}kg')  
        print(f'Height: {self.height}ft')
        print(f'Color: {self.color}')
        print(f'Tamed: {self.is_tamed}')
        print('--'*15)

tom = Cat ('street cat','grey', age =100, gender= 'M')
soni = Cat('house cat','brown' ,age = 3)
snowbell = Cat('persian','white', age= 5)

print('TOM')
tom.info()
tom.eat('jerry')

print('SNOWBELL')
snowbell.info()
snowbell.eat('stuart')
