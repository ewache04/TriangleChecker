# Author name: Jeremiah E. Ochepo
# last Edited: 2/15/2020 (7PM)
# Description: Check if the given sides can form a triangle.

def is_triangle(side1, side2, side3):
    """
    Check if the given sides can form a triangle.

    Parameters:
    - side1, side2, side3: Lengths of the sides.

    Returns:
    - True if the sides can form a triangle, False otherwise.
    """
    return side1 <= side2 + side3 and side2 <= side1 + side3 and side3 <= side1 + side2


def make_triangle():
    """
    Prompt the user to enter three side lengths and check if they form a triangle.
    """
    while True:
        print("Enter side lengths to check if they form a triangle.")
        try:
            side1 = int(input("Enter side one: "))
            side2 = int(input("Enter side two: "))
            side3 = int(input("Enter side three: "))

            if is_triangle(side1, side2, side3):
                print("The entered values can form a triangle.")
            else:
                print("The entered values cannot form a triangle.")

        except ValueError:
            print("Invalid entry! Please enter a number.")
        except Exception as e:
            print(f"An error occurred: {e}")

        choice = input("Do you want to check another triangle (T), or quit (Q)? ").upper()

        if choice == 'Q':
            print("Exiting the program. Goodbye!")
            break
        elif choice != 'T':
            print("Invalid choice. Please enter 'T' to check another triangle or 'Q' to quit.")


if __name__ == "__main__":
    make_triangle()
