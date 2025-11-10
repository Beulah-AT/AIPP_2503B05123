from typing import Dict, Tuple


def calculate_energy_charges(units: float, customer_type: str) -> float:
    """Calculate energy charges based on units consumed and customer type."""
    if customer_type == "domestic":
        if units <= 100:
            return units * 1.45
        elif units <= 200:
            return (100 * 1.45) + ((units - 100) * 2.60)
        else:
            return (100 * 1.45) + (100 * 2.60) + ((units - 200) * 3.60)
    elif customer_type == "commercial":
        if units <= 100:
            return units * 3.00
        elif units <= 200:
            return (100 * 3.00) + ((units - 100) * 4.50)
        else:
            return (100 * 3.00) + (100 * 4.50) + ((units - 200) * 6.00)
    elif customer_type == "industrial":
        if units <= 100:
            return units * 5.00
        elif units <= 200:
            return (100 * 5.00) + ((units - 100) * 6.50)
        else:
            return (100 * 5.00) + (100 * 6.50) + ((units - 200) * 7.50)
    else:
        raise ValueError("Invalid customer type")

def get_fixed_charges(customer_type: str) -> Tuple[float, float]:
    """Get fixed and customer charges based on customer type."""
    if customer_type == "domestic":
        return 30.0, 90.0  # FC, CC
    elif customer_type == "commercial":
        return 100.0, 50.0
    elif customer_type == "industrial":
        return 200.0, 100.0
    else:
        raise ValueError("Invalid customer type")

def calculate_bill(pu: float, cu: float, customer_type: str) -> Dict[str, float]:
    """Calculate the complete bill based on units and customer type."""
    units = cu - pu
    if units < 0:
        raise ValueError("Current units must be greater than previous units")
    
    # Calculate energy charges
    ec = calculate_energy_charges(units, customer_type)
    
    # Get fixed charges
    fc, cc = get_fixed_charges(customer_type)
    
    # Calculate electricity duty (1.55% of EC)
    ed = round(0.0155 * ec, 2)
    
    # Prepare charges dictionary
    charges = {
        "EC": ec,
        "FC": fc,
        "CC": cc,
        "ED": ed,
        "total": ec + fc + cc + ed
    }
    
    return charges

def print_bill(customer_name: str, customer_type: str, prev_reading: float, curr_reading: float, charges: Dict[str, float]):
    """Print the electricity bill with all charges."""
    print("\n---------- TGNPDCL ELECTRICITY BILL ----------")
    print(f"Customer Name        : {customer_name}")
    print(f"Customer Type        : {customer_type.capitalize()}")
    print(f"Previous Reading     : {prev_reading}")
    print(f"Current Reading      : {curr_reading}")
    print(f"Units Consumed       : {curr_reading - prev_reading}")
    print("----------------------------------------------")
    print(f"Energy Charges       : ₹{charges['EC']:.2f}")
    print(f"Fixed Charges        : ₹{charges['FC']:.2f}")
    print(f"Customer Charges     : ₹{charges['CC']:.2f}")
    print(f"Electricity Duty     : ₹{charges['ED']:.2f}")
    print("----------------------------------------------")
    print(f"Total Bill Amount    : ₹{charges['total']:.2f}")
    print("----------------------------------------------")


def main():
    """Take user inputs and generate electricity bill."""
    print("\nTGNPDCL Electricity Bill Generator")
    
    try:
        # Get customer details
        customer_name = input("Enter Customer Name: ").strip()
        customer_type = input("Enter Customer Type (Domestic/Commercial/Industrial): ").strip().lower()
        
        # Validate customer type
        if customer_type not in ['domestic', 'commercial', 'industrial']:
            print("Invalid customer type! Please enter Domestic, Commercial, or Industrial.")
            return
        
        # Get meter readings
        try:
            prev_reading = float(input("Enter Previous Reading: "))
            curr_reading = float(input("Enter Current Reading: "))
        except ValueError:
            print("Error: Please enter valid numeric values for meter readings")
            return
            
        # Validate readings
        if curr_reading < prev_reading:
            print("Error: Current reading cannot be less than previous reading")
            return
        
        # Calculate bill
        charges = calculate_bill(prev_reading, curr_reading, customer_type)
        
        # Print the bill
        print_bill(customer_name, customer_type, prev_reading, curr_reading, charges)
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return


if __name__ == "__main__":
    main()