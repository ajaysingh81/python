#************************* P0LYMORPHISM ***************

# P0LY = MANY
# MORPHISM = FORMS

# Example:-

# adding a no.

# function polymorphism

def add(*a):
    print(sum(a))
add()
add(6)
add(1,2,3,4)


# mathod polymorphism

class cat:
    def color(self):
        print("cats are white")

class dog:
    def color(self):
        print("dogs are brown")

c = cat()
d = dog()
c.color()
d.color()