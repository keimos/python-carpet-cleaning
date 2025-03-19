def carpet_cleaning_service(amount_paid):
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

    if amount_paid in services:
        print(f"You have selected {services[amount_paid]['name']}")
        for detail in services[amount_paid]["details"]:
            print(detail)    

# Example usage
carpet_cleaning_service(6)
