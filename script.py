#latihan 2 

#mpty

#latihan 3 

# Import class Food dan class Drink 
from food import Food 
from drink import Drink


# Buat instance class Food dan berikan ke variable food1 
food1 = Food('Roti Lapis',5)
print(food1.info())


# Panggil method info dari food1 dan cetak nilai return


# Buat instance class Drink dan berikan ke variable drink1 
drink1 = Drink('Kopi',3)
print(drink1.info())

# Panggil method info dari drink1 dan cetak nilai return

#latihan 4 
from food import Food
from drink import Drink

food1 = Food('Roti Lapis', 5, 330)

# Tetapkan variable calorie_count milik food1 ke 330
food1.calorie_count = 330

# Panggil method calorie_info dari food1

calorie_info = food1

#latihan 5 
from food import Food
from drink import Drink

food1 = Food('Roti Lapis', 5)
food1.calorie_count = 330

# Panggil method info dari food1 dan cetak nilai return
print(food1.info()) #memanggil dan ngepritn sebuah method 


#latihan 6 

from food import Food
from drink import Drink

food1 = Food('Roti Lapis', 5)
food1.calorie_count = 330
print(food1.info())

# Buat instance class Drink dan tetapkan ke variable drink1
drink1 = Drink('Kopi',3)

# Tetapkan volume variable drink1 ke 180
drink1.volume = 180

# Panggil method info dari drink1 dan cetak nilai return
print(drink1.info())

#latihan 7 
from food import Food
from drink import Drink

# Tambahkan argument ke Food()
food1 = Food('Roti Lapis', 5, 330)


print(food1.info())

drink1 = Drink('Kopi', 3)
drink1.volume = 180
print(drink1.info())
