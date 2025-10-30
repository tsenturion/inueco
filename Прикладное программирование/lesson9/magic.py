# str()
class Magic:
    def __init__(self, name, description, damage):
        self.name = name
        self.description = description
        self.damage = damage
    
    def __str__(self):
        return f"{self.name} - {self.description} - {self.damage} damage"
    

fireball = Magic('Fireball', 'Deals 50 damage', 50)
print(fireball)