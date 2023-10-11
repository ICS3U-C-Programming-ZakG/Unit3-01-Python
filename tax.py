#!/usr/bin/env python3
# Created by: Zak Goneau
# Created on: Oct. 10, 2023
# This program calculates the total and tax of an item with a given subtotal.

import constants


def main():
    # Get subtotal from user
    print("This program calculates the total and tax of an item with a given subtotal.")
    subtotal = float(input("Please enter a subtotal: "))

    # Calculate the total and tax
    tax = subtotal * constants.HST
    total = subtotal + tax

    # Display the total and tax
    print("The total cost is: ${:.2f} and the tax is: ${:.2f}.".format(total, tax))


if __name__ == "__main__":
    main()
