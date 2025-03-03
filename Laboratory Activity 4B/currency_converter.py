import csv

# Function to read currency rates from the CSV file
def read_currency_rates(filename):
    rates = {}
    with open(filename, mode='r') as file:
        for line in file:
            # Split the line into currency code and rate
            parts = line.split()
            if len(parts) >= 2:
                currency_code = parts[0].strip()  # Strip any extra spaces
                try:
                    rate = float(parts[-1])  # Get the last part as the rate
                    rates[currency_code] = rate
                except ValueError:
                    continue  # Skip lines with invalid rates
    return rates


def currency_converter():
    # Read currency rates from the CSV file
    rates = read_currency_rates('currency.csv')

    # Prompt user for input
    try:
        dollars = float(input("How much dollar do you have? "))
        target_currency = input("What currency do you want to have? ").strip().upper()

        
        if target_currency in rates:
            conversion_rate = rates[target_currency]
            converted_amount = dollars * conversion_rate
            
            # Using a dictionary to store the results
            conversion_result = {
                "Dollar": dollars,
                "Converted Currency": converted_amount,
                "Currency Code": target_currency
            }

            
            print(f"Dollar: {conversion_result['Dollar']} USD")
            print(f"{conversion_result['Currency Code']}: {conversion_result['Converted Currency']:.2f}")
        else:
            print("Currency not found in the exchange rates.")
    except ValueError:
        print("Invalid input. Please enter a numeric value for dollars.")

# Run the currency converter
currency_converter()