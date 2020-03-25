from math import floor

lenght = float (input ())
width = float (input ())
side_of_wardrobe = float (input())

area_of_hall = lenght * width * 10000
area_of_wardrobe = side_of_wardrobe * side_of_wardrobe * 10000

bench = area_of_hall / 10

free_space = area_of_hall - area_of_wardrobe - bench

dancers = free_space / 7040

print (floor(dancers))