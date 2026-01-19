"""
Simple household budget calculator.

Calculates total income, fixed expenses, variable expenses,
loan costs and remaining monthly budget.
"""

def main():
    print("Ange personer i hushållet. Skriv stop när du är klar. ")

    names = []

    while True:
        name = input("Namn:").strip()
        if name.lower() == "stop":
            break
        names.append(name)

    total_names = len(names)
    print("Ni är", total_names, "i hushållet.")

    incomes = []
    for name in names:
        income = float(input(f"Ange inkomst för {name}:"))
        income = income * 0.66
        incomes.append(income)
        total_income = sum(incomes)
    print("Hushållet har", total_income, "totalt i inkomst.")

    print("Ange fasta utgifter nedan: ")

    categories = ["El", "Bredband"]
    expenses = []

    for category in categories:
        cost = float(input(f"{category}: "))
        expenses.append(cost)

    
    other_expenses = {}
    total_expenses = 0.0
    while True:
        other_costs = input("Har du fler fasta utgifter? (ja/nej):")
        if other_costs.lower() != "ja":
            break
        other_costs1 = input("Namn på utgiften:")
        other_costs_sum = float(input("Kostnad:"))
        other_expenses[other_costs1] = other_costs_sum
        
    total_expenses = sum(expenses) + sum(other_expenses.values())
        
    if total_expenses > 0.0:
        print("Dina fasta utgifter är:", total_expenses)


    print("Ange rörliga utgifter nedan:")

    variable_categories = ["Mat", "Kläder"]
    variable_expenses = []

    for variable_category in variable_categories:
        cost = float(input(f"{variable_category}: "))
        variable_expenses.append(cost)


    other_v_expenses = {}

    while True:
        svar = input("Har du fler rörliga utgifter? (ja/nej):")
        if svar.lower() != "ja":
            break
        other_v_name = input("Skriv namn på rörlig utgift:")
        other_v_sum = float(input("Kostnad:"))
        other_v_expenses[other_v_name] = other_v_sum
   
    total_v_expenses = sum(variable_expenses) + \
    sum(other_v_expenses.values())
    total_var_expenses = total_expenses + total_v_expenses

    if total_v_expenses > 0:
        print("Dina rörliga utgifter är:", total_v_expenses)


    house_loan_total = 0.0
    print("Har du bolån?")
    answer = input("Svar: (ja/nej:) ")
    if answer.lower() == "ja": 
        house_loan = float(input("Hur mycket har du i bolån?"))
        interest = float(input("Vilken årlig ränta har du på bolånet? (i %, t.ex. 4.25)"))
        ammortering = float(input("Hur stor årlig amomrtering har du? (ange i procent av lånet, t.ex. 1.0)"))


        house_loan_interest = (0.01 * interest)
        house_loan_ammortering = (0.01 * ammortering)


        house_loan_sum = (house_loan * house_loan_interest / 12)
        house_loan_am = (house_loan_ammortering * house_loan / 12)
        house_loan_total = (house_loan_sum + house_loan_am)
        print(f"Ditt huslån kostar {house_loan_total:.2f} i månaden.")


    other_loans = []
    total = 0.0

    while True:
        other_loans1 = input("Har du andra lån? (ja/nej):")
        if other_loans1.lower() != "ja":
            break


        other_loans2 = input("Skriv namn på lånet:")
        other_loans3 = float(input("Vilket belopp är lånet på?"))
        other_interest = float(input("Vilken årlig ränta har du på lånet? (Skriv i procent t.ex. 4.5)"))
        other_ammortering = float(input("Hur stor årlig ammortering har du på lånet? Skriv i procent t.ex. 3.0)"))
        
        interest_sum = (other_interest * 0.01)
        other_ammortering_sum = (other_ammortering * 0.01)
        
        other_loans_sum = (other_loans3 * interest_sum / 12)
        other_sum_loans = (other_ammortering_sum * other_loans3 / 12)
        other_loans_total = (other_loans_sum + other_sum_loans)

        print(f"{other_loans2} kostar {other_loans_total:.2f} i månaden.")

        other_loans.append(other_loans_total)

        total = sum(other_loans)
    if other_loans:
        print(f"Kostnaden för dina övriga lån är {total:.2f} i månaden.")     
    else:
        total = 0.0

    total_all_expenses = total_var_expenses + house_loan_total + total
    budget = total_income - total_all_expenses

    print(f"Din budget är: {budget:.2f}")
    print(f"Totala utgifter: {total_all_expenses:.2f}")


if __name__ == "__main__":
    main()
