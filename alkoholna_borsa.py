price_of_whiskey = float (input ())
beer_liters = float (input ())
wine_liters = float (input ())
rakia_liters = float (input ())
whiskey_liters = float (input ())

price_of_rakia = price_of_whiskey / 2
price_of_wine = price_of_rakia * 0.60
price_of_beer = price_of_rakia * 0.20

money_for_whiskey = price_of_whiskey * whiskey_liters
money_for_rakia = price_of_rakia * rakia_liters
money_for_wine = price_of_wine * wine_liters
money_for_beer = price_of_beer * beer_liters

money = money_for_whiskey + money_for_rakia + money_for_wine + money_for_beer
print (f"{money:.2f}")