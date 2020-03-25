count_table = int(input())
lenght_in_meters = float(input())
width_in_meters = float(input())

area_of_table = count_table * (lenght_in_meters + 2 * 0.30) * (width_in_meters + 2 * 0.30)
area_of_quads = count_table * (lenght_in_meters / 2) * (lenght_in_meters / 2)

price_in_usd = area_of_table * 7 + area_of_quads * 9
print (f"{price_in_usd:.2f} USD")

price_in_bgn = price_in_usd * 1.85
print(f"{price_in_bgn:.2f} BGN")