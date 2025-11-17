item_price_str = input("Enter the item price")
vat_rate_str = input("Enter the VAT rate (e.g., 20 for 20%): ")
try:
    item_price = float(item_price_str)
    vat_rate = float(vat_rate_str)
except ValueError:
    print("invalid input. Please enter number only for price and VAT rate")
vat_amount = item_price * (vat_rate / 100)
total_bill = item_price + vat_amount
print("Vat amount: ", round(vat_amount, 2))
print("Total Bill: ", round(total_bill, 2))
