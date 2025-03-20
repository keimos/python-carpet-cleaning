import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO, # Log level can be adjusted
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("carpet_cleaning_service.log"),
        logging.StreamHandler() # Logs to the console
    ]
)


def carpet_cleaning_service():
    """Provides details of the selected carpet cleaning service."""
    services = {
        6: {
            "name": "Platinum Service",
            "details": [
                "4 bedroom and 1 hallway Power Clean",
                "carpet Shampoo",
                "Deep Rinse",
                "Steam No-Chemical Dry"
            ]
        },
        10: {
            "name": "Basic Service",
            "details": [
                "2 bedroom Basic Clean",
                "Deep Rinse"
            ]
        }
    }

    try:
        # Accept user input and convert to integer
        amount_paid = int(input("Enter the amount you paid for the service (6 or 10): "))
        logging.info(f"User entered payments amount: {amount_paid}")


        # Check if the input matches available services
        if amount_paid in services:
            logging.info(f"Service selected: {services[amount_paid]['name']}")
            print(f"You have selected {services[amount_paid]['name']}")
            for detail in services[amount_paid]["details"]:
                print(detail)
        else:
            logging.warning(f"Invalid payment amount entered: {amount_paid}")
            print("Invalid payment amount. Please select a valid service.")
    except ValueError as e:
            logging.error(f"Error occurred while processing user input: {e}")
            print("Error: Invalid input. Please enter a valid numeric amount.")    

# Example usage
carpet_cleaning_service()
