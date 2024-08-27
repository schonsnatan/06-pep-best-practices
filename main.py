CONSTANTE_BONUS = 1000

# Request the name for the user:


def request_name():

    while True:
        try:
            name = input("Please enter your name: ")
            if len(name) == 0:
                raise ValueError("Please provide a name")
            elif any(char.isdigit() for char in name):
                raise ValueError("Your name must have only letters")
            elif name.isspace():
                raise ValueError("Please type something")
            else:
                break
        except ValueError as e:
            print(f"Error: {e}. Please take a look into the instructions.")

    # Request the salary:
    while True:
        try:
            sal = float(input("Please enter your salary: "))
            if sal <= 0:
                raise ValueError("Inform a positive and non-zero value")
            else:
                break
        except ValueError as e:
            print(f"Error: {e}. Please take a look into the instructions.")

    while True:
        # Request the bonus value:
        try:
            bonus = float(
                input("Please enter your bonus percentage (e.g., 0.05 for 5%): ")
            )
            if bonus < 0:
                raise ValueError("Inform a positive bonus.")
            else:
                break
        except ValueError as e:
            print(f"Error: {e}. Please take a look into the instructions.")

    # Print the informations for the user:
    final_bonus: float = CONSTANTE_BONUS + sal * bonus
    kpi: float = (sal + final_bonus) / 1000

    print(f"Your KPI is: {kpi:.2f}")
    print(
        f"{name}, your salary is ${sal:.2f} and your final bonus is ${final_bonus:.2f}"
    )
    pass


request_name()
