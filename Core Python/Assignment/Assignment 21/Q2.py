class Television:
    def __init__(self):
        self.model_number = 0
        self.screen_size = 0
        self.price = 0

    def get_input(self):
        try:
            self.model_number = int(input("Enter Model Number (max 4 digits): "))
            self.screen_size = int(input("Enter Screen Size (12–70 inches): "))
            self.price = float(input("Enter Price (0–5000 Rs): "))

            if self.model_number > 9999:
                raise ValueError("Model number should not exceed 4 digits.")
            if self.screen_size < 12 or self.screen_size > 70:
                raise ValueError("Screen size must be between 12 and 70 inches.")
            if self.price < 0 or self.price > 5000:
                raise ValueError("Price must be between 0 and 5000 Rs.")

        except ValueError as e:
            print(f"Error: {e}")
            print("Invalid input! Resetting all values to zero...")
            self.model_number = 0
            self.screen_size = 0
            self.price = 0

    def display(self):
        print("\nTelevision Details:")
        print(f"Model Number: {self.model_number}")
        print(f"Screen Size : {self.screen_size} inches")
        print(f"Price       : Rs. {self.price}")

def main():
    tv = Television()
    tv.get_input()
    tv.display()

if __name__ == "__main__":
    main()
