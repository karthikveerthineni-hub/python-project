'''Question 1

Write a function electricity(rate_per_unit).

-   The outer function receives the cost per unit.
-   The inner function receives the number of units consumed.
-   Print the total electricity bill.
-   Return the inner function.'''

def electricity(rate_per_unit):
    def inner():
        number_of_units = 100
        return f"Total electricity bill:{number_of_units*rate_per_unit}"
    return inner()
obj = electricity(1.95)
print(obj)



'''Question 2

Write a function salary(bonus).

-   The outer function receives the bonus amount.
-   The inner function receives the employee’s basic salary.
-   Print the total salary after adding the bonus.
-   Return the inner function.'''

def salary(bonus):
    def inner():
        basic_salary= 25000
        return f"Total salary:{basic_salary+bonus}"
    return inner()
obj = salary(5000)
print(obj)

'''Question 3

Write a function discount(percent).

-   The outer function receives the discount percentage.
-   The inner function receives the product price.
-   Print the final price after applying the discount.
-   Return the inner function.'''

def discount(percent):
    def inner():
        product_price = 25000
        return f"Total discount:{product_price-product_price*percent/100}"
    return inner()
obj = discount(5)
print(obj)

'''Question 4

Write a function bank_account(balance).

-   The outer function receives the initial balance.
-   The inner function receives an amount to withdraw.
-   Print the remaining balance.
-   Return the inner function.'''

def bank_acc():
    balance = 100000
    def inner(withdraw):
        if balance >= withdraw:
            return f"withdraw money is :{withdraw}"
        else:
            return "balance is insufficient"
    return inner
obj = bank_acc()
print(obj(10000))


