"""PS1 — Paying off credit-card debt.

Fill in each function. All rates are annual; interest compounds monthly.
Round money to 2 decimals only when the assignment asks you to.
"""


def balance_after_year(balance: float, annual_rate: float, monthly_pay_fraction: float) -> float:
    """Part A: remaining balance after 12 months when you pay a fixed FRACTION each month.

    Each month:
        unpaid = balance - (monthly_pay_fraction * balance)
        balance = unpaid + (annual_rate / 12) * unpaid
    """
    raise NotImplementedError("Implement Part A")


def min_fixed_payment_bruteforce(balance: float, annual_rate: float) -> int:
    """Part B: smallest fixed monthly payment (a multiple of 10) that clears the
    balance within 12 months. Solve by trying 10, 20, 30, ... until it works."""
    raise NotImplementedError("Implement Part B")


def min_fixed_payment_bisection(balance: float, annual_rate: float) -> float:
    """Part C: same as Part B but via bisection search, accurate to the cent.

    Lower bound = balance / 12
    Upper bound = (balance * (1 + annual_rate/12) ** 12) / 12
    """
    raise NotImplementedError("Implement Part C")
