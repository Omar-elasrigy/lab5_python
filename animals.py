class Animal:
    def __init__(self,animal_name,animal_type,age):
        self.name=animal_name
        self.animal_type=animal_type
        self.age=age

    def eat(self,food):
        self.food=food
        return f"{self.name} eats {self.food}"
    def drink(self,drinks):
        self.drinks=drinks
        return f"{self.name} drinks {self.drinks}"
    def age(self):
        if self.age >10:
            return f"{self.name} is old"
        else:
            return f" {self.name} is young"
class Cat(Animal):
    meows=False
    def __init__(self,animal_name,animal_type,age,color):
        super().__init__(animal_name,animal_type,age)
        self.color=color
    @classmethod
    def meow(cls,meow):
        if meow=="y":
            cls.meow=True
            return cls.meow
        elif meow=="n":
            cls.meow=False
            return cls.meow
    def eat(self,food):
        self.food=food
        return f"{self.name} likes {self.food}"
cat1=Cat("cat","mammals",4,"brown")
elephant=Animal("elephant","mammals",20,)
print(elephant.eat("Vegetables"))
print(cat1.eat("pasta"))
print(cat1.meow("n"))
