import math
import argparse

def calc_annuity_payment(loan_principal, interest, num_payments):
    i = interest / 1200
    return math.ceil(loan_principal*i*(1+i)**num_payments/((1+i)**num_payments - 1))

def calc_loan_principal(annuity_payment,interest,num_payments):
    i = interest / 1200
    return  annuity_payment*((1+i)**num_payments - 1)/(i*(1+i)**num_payments)

def calc_num_payments(annuity_payment, loan_principal, interest):
    i = interest / 1200
    return math.ceil(math.log(annuity_payment/(annuity_payment-i*loan_principal),1+i))

def calc_diff_payment(principal, interest, periods):
    i = interest/1200
    Dm = []
    for m in range(periods):
        d = principal/periods + i*(principal - principal*m/periods)
        Dm.append(math.ceil(d))
    return Dm
def print_period(n):
    if n < 12:
        print(f'It will take {n} month{"" if n == 1 else "s"} to repay this loan!')
    elif n % 12 == 0:
        print(f'It will take {n // 12} year{"" if n / 12 == 1 else "s"} to repay this loan!')
    else:
        print(f'It will take {n // 12} year{"" if n // 12 == 1 else "s"} '
              f'and {n % 12} month{"" if n % 12 == 1 else "s"} to repay this loan!')


def main():

    # parse command line section
    parser = argparse.ArgumentParser()
    parser.add_argument('--payment',type= float)
    parser.add_argument('--principal',type= float)
    parser.add_argument('--periods',type= int)
    parser.add_argument('--interest',type= float)
    parser.add_argument("--type")
    args = parser.parse_args()

    # validate parameters section
    paramter_list = [args.principal, args.payment, args.interest, args.periods]
    if any([x is not None and x < 0 for x in paramter_list]):
        print('Incorrect parameters.')
        return

    if args.interest is None:
        print("Incorrect parameters")
        return

    if not args.type in ["diff", "annuity"]:
        print("Incorrect parameters")
        return

    # calculation
    if args.type == "annuity":
        if args.payment is None:
            payment = calc_annuity_payment(args.principal,args.interest,args.periods)
            args.payment = payment
            print(f'Your monthly payment = {payment}!')
        elif args.principal is None:
            loan = calc_loan_principal(args.payment, args.interest, args.periods)
            args.principal = loan
            print(f'Your loan principal = {loan}!')
        elif args.periods is None:
            n = math.ceil(calc_num_payments(args.payment, args.principal, args.interest))
            print_period(n)
            args.periods = n
        print(f'Overpayment = {args.payment*args.periods - args.principal}')
    elif args.type == "diff":
        if args.payment is None:
            lst = calc_diff_payment(args.principal,args.interest,args.periods)
            for i in range(len(lst)):
                print(f'Month {i+1}: payment is {lst[i]}')
            print(f'Overpayment = {sum(lst) - args.principal}')
        else:
           print('Incorrect parameters')


if __name__ == '__main__':
    main()