# latihan 2 
# Import class MenuItem menggunakan 'from' 'import'
from menu_item import MenuItem

# Wariskan class MenuItem dan definisikan class Food 

class Food(MenuItem):
    pass

# latihan 3
#same as before

# latiha 4

#latihan 4 
from food import Food
from drink import Drink

food1 = Food('Roti Lapis', 5)

# Tetapkan variable calorie_count milik food1 ke 330
food1 = calorie_info(330)

# Panggil method calorie_info dari food1
food1.calorie_count

#latihan 5 

from menu_item import MenuItem

class Food(MenuItem):
    # Definisikan method info
    def info(self):
        return self.name + ': $' + str(self.price) + ' (' + str(self.calorie_count) + 'kkal)'
    
    
    def calorie_info(self):
        print('kkal: ' + str(self.calorie_count))


