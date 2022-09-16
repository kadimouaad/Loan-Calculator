import math
import argparse
from functions import loan_interest_calculator
from functions import converting_months
from functions import converting_years

parser = argparse.ArgumentParser(description="my loan calculator")
parser.add_argument("--type", type=str)
parser.add_argument("--payment", type=float)
parser.add_argument("--principal", type=float)
parser.add_argument("--periods", type=float)
parser.add_argument("--interest", type=float)
args = parser.parse_args()
original_list = [args.payment, args.principal, args.periods, args.interest]
True_list = [i for i in original_list if i is not None]
true_list_2 = [i for i in True_list if i > 0]

my_list = ["annuity", "diff"]
if args.type not in my_list:
    print("Incorrect parameters1")
    print(args)
else:
    if args.payment is not None and args.type == "diff":
        print("Incorrect parameters2")
    elif len(true_list_2) < 3:
        print("Incorrect parameters3")
    elif args.interest is None:
        print("Incorrect parameters4")
    else:
        if args.type == "annuity":  # calculating the loan principal args.principal is None
            if args.principal is None:
                annuity_pay = args.payment
                num_months_s = args.periods
                interest_3 = args.interest

                b = loan_interest_calculator(interest_3)

                P = annuity_pay / ((b * math.pow(1 + b, num_months_s)) / (math.pow(1 + b, num_months_s) - 1))
                print("Your loan principal = {}!".format(int(P)))
                print(f"Overpayment = {math.ceil((annuity_pay * num_months_s) - P)}")

            elif args.periods is None:
                loan_principal = args.principal
                month_paym = args.payment
                intrest = args.interest
                y = loan_interest_calculator(intrest)
                n = math.log(month_paym / (month_paym - y * loan_principal), 1 + y)
                print(n)
                years = converting_years(n)
                months = converting_months(n)
                if years >= 2:
                    s = "s"
                else:
                    s = ""
                if months >= 2:
                    p = "s"
                else:
                    p = ""
                if months == 12:
                    years = years + 1
                    print("It will take {} year{} to repay this loan!".format(years, s))
                elif years == 0:
                    print("It will take {} month{} to repay this loan!".format(months, p))
                else:
                    print("It will take {} year{} and {} month{} to repay this loan!".format(years, s, months, p))
                print(f"Overpayment = {int((month_paym * math.ceil(n)) - loan_principal)}")
            elif args.payment is None:
                loan_principal = args.principal
                num_months = args.periods
                intrest_2 = args.interest
                z = loan_interest_calculator(intrest_2)
                monthly_pay = loan_principal * ((z * math.pow(1 + z, num_months)) / (math.pow(1 + z, num_months) - 1))

                print("Your annuity payment = {}!".format(math.ceil(monthly_pay)))
                print(f"Overpayment = {math.ceil((math.ceil(monthly_pay) * num_months) - loan_principal)}")
        elif args.type == "diff":
            P = args.principal
            n = args.periods
            i = loan_interest_calculator(args.interest)
            sum_months = 0

            for a in range(1, int(n + 1)):
                D = (P / n) + (i * (P - ((P * (a - 1)) / n)))
                print(f"Month {a}: payment is {math.ceil(D)}")
                sum_months = sum_months + math.ceil(D)
            print(f"Overpayment = {int(sum_months - P)}")
