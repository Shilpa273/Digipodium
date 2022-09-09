from re import T


class Cat:
    breed = None
    gender = None
    color = None
    age = None
    weight = None
    height = None
    is_tamed = None

    def eat(self, food='catfood'):
        print(f' 🐈 is eaing {food}')

    def play(self):
        print('🐈 is playing')

    def sleep(self):
        print('🐈 is sleeping')    

billu = Cat() # constructor calling
tom = Cat()
bagadbilla = Cat()


billu.breed = 'persian'
billu.weight = 2
billu.age = 2
billu.color = 'white'
billu.height = 1
billu.is_tamed = True
billu.gender = 'M'

tom.breed = 'street cat'
tom.weight = 1.5
tom.age = '100'
tom.color = 'grey'
tom.height = 1.1
tom.is_tamed = True
tom.gender = 'M'

bagadbilla.breed = 'wild cat'
bagadbilla.weight = 3
bagadbilla.age = '50'
bagadbilla.color = 'grey'
bagadbilla.height = 2.3
bagadbilla.is_tamed = True
bagadbilla.gender = 'M'

print("Billu details")
print('breed:',billu.breed)
print('weight:',billu.weight)
print('gender:',billu.gender)
print('age:',billu.age)
print('height:',billu.height)
print('pet:','yes' if billu.is_tamed else 'no')
print('color:',billu.color)
billu.sleep()
billu.eat()
billu.play()

print("tom details")
print('breed:',tom.breed)
print('weight:',tom.weight)
print('gender:',tom.gender)
print('age:',tom.age)
print('height:',tom.height)
print('pet:','yes' if tom.is_tamed else 'no')
print('color:',tom.color)
tom.sleep()
tom.eat()
tom.play()


print("bagadbilla details")
print('breed:',bagadbilla.breed)
print('weight:',bagadbilla.weight)
print('gender:',bagadbilla.gender)
print('age:',bagadbilla.age)
print('height:',bagadbilla.height)
print('pet:','yes' if bagadbilla.is_tamed else 'no')
print('color:',bagadbilla.color)
bagadbilla.sleep()
bagadbilla.eat('mouse')
bagadbilla.eat('bird')
bagadbilla.eat('bird')



