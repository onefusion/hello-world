def calculate_tax(amount, rate):
    """
    Calculate the tax owed based on amount and tax rate.

    amount: Number applying tax to
    rate: Tax rate as decimal
    """
    tax = amount * rate
    return tax

# Ask for amount and tax rate
amount_input = float(input("Enter amount: "))
rate_input = float(input("Enter the tax rate as a decimal: "))

# Call function and store returned value
tax_owed = calculate_tax(amount_input, rate_input)

# Display result
print(f"Tax owed: ${tax_owed:.2f}")