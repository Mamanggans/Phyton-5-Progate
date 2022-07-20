#latihan 2 menentukan class ini adalah blueprint 
from unittest import result


class MenuItem:
  pass

#latiham 3 menetapkan instance 
class MenuItem:
    pass
# Buat instance untuk class MenuItem 

menu_item1 = MenuItem()

# latihan 4 instance

class MenuItem:
    pass


menu_item1 = MenuItem()

menu_item1.name = 'Roti Lapis' #"name adalah variabel instance sedangkan roti lapis adalah isian nya "
print(menu_item1.name)

# Tentukan price menu_item1 ke 5
menu_item1.price = 5 
print(menu_item1.price)

# Cetak price dari menu_item1


#latihan 5 banyak instance 
class MenuItem:
    pass


menu_item1 = MenuItem()

menu_item1.name = 'Roti Lapis'
print(menu_item1.name)

menu_item1.price = 5
print(menu_item1.price)

# Buat instance dari class MenuItem
menu_item2 = MenuItem()

# Tetapkan name milik menu_item2 ke 'Kue Coklat'
menu_item2.name = 'Kue Coklat'

# Cetak nama dari menu_item2
print(menu_item1.name)

# Tetapkan price dari menu_item2 ke 4
menu_item2.price = 4

# Cetak price dari menu_item2
print(menu_item2.price)


# latihan 6 memanggil sebuah method 
class MenuItem:
    # Definiskan method info 
    def info(self):
      print('Tampilkan nama dan harga dari menu item')


menu_item1 = MenuItem()
menu_item1.name = 'Roti Lapis'
menu_item1.price = 5

# Panggil method info dari menu_item1
menu_item1.info()

menu_item2 = MenuItem()
menu_item2.name = 'Kue Coklat'
menu_item2.price = 4

# Panggil method info dari menu_item2
menu_item2.info()


#latihan 7 menggunakan self untuk mengeprint semua menu item 
class MenuItem:
    def info(self):
        # Cetak dengan format '____: $____'
        print(self.name+' : '+str(self.price))


menu_item1 = MenuItem()
menu_item1.name = 'Roti Lapis'
menu_item1.price = 5

menu_item1.info()

menu_item2 = MenuItem()
menu_item2.name = 'Kue Coklat'
menu_item2.price = 4

menu_item2.info()


# latihan 8 menggunakan return di instance
class MenuItem:
    def info(self):
        # Return kontent dari print() sebagai nilai return
        return self.name + ': $' + str(self.price)


menu_item1 = MenuItem()
menu_item1.name = 'Roti Lapis'
menu_item1.price = 5

# Cetak nilai dari menu_item1.info()
print(menu_item1.info())

menu_item2 = MenuItem()
menu_item2.name = 'Kue Coklat'
menu_item2.price = 4

# Cetak nilai dari menu_item2.info()
print(menu_item2.info())

#latihan 9 method instance banyak parameter 

class MenuItem:
    def info(self):
        return self.name + ': $' + str(self.price) # why self price karna ngambil nya dari self yg ada di instance info 

    # Definiskan method get_total_price
    def get_total_price(self,count):
        total_price = self.price * count
        return total_price


menu_item1 = MenuItem()
menu_item1.name = 'Roti Lapis'
menu_item1.price = 5

print(menu_item1.info())

# Panggil method get_total_price 
result = menu_item1.get_total_price(4) # ingat result itu adalah variable njd kl
#suruh masukin ke variabel yah nulis nya kek gini 

# Cetak 'Total harga adalah $____' 
print('Total harga adalah $' + str(result)) # inget kalau number mau dijadiin di masukin ke string harus dijadiin string dulu


#latihan 10 method init 
class MenuItem:
    # Definisikan method __init__
    def __init__(self):
        print('Instance dari class MenuItem telah di ciptakan!')

    def info(self):
        return self.name + ': $' + str(self.price)

    def get_total_price(self, count):
        total_price = self.price * count
        return total_price


menu_item1 = MenuItem()
menu_item1.name = 'Roti Lapis'
menu_item1.price = 5

print(menu_item1.info())

result = menu_item1.get_total_price(4)
print('Total harga adalah $' + str(result))


#latihan 11 mengatur init jadi kalau ada init lau bisa 
#langsung tarok aja menuitem nya dibawah init tapi variabel nya diganti jadi self 
class MenuItem:
    def __init__(self):
        # Tetapkan self.name ke 'Roti Lapis'
        self.name = 'Roti Lapis'
        # Tetapkan self.price ke 5
        self.price = 5

    def info(self):
        return self.name + ': $' + str(self.price)

    def get_total_price(self, count):
        total_price = self.price * count
        return total_price


menu_item1 = MenuItem()

print(menu_item1.info())

result = menu_item1.get_total_price(4)
print('Total harga adalah $' + str(result))

#latihan 12 menulis method init yang baik dan benar 
class MenuItem:
    # Tambahkan parameter name dan price
    def __init__(self,name,price):
        # Gantikan 'Roti Lapis' ke parameter name
        self.name = name
        
        # Gantikan 5 ke parameter price
        self.price = price

    def info(self):
        return self.name + ': $' + str(self.price)

    def get_total_price(self, count):
        total_price = self.price * count
        return total_price


# Tambahkan 'Roti Lapis' dan 5 sebagai argument
menu_item1 = MenuItem('Roti Lapis',5)


print(menu_item1.info())

result = menu_item1.get_total_price(4)
print('Total harga adalah $' + str(result))

#latihan 13 memisahkan item yang sudah kita buat 
