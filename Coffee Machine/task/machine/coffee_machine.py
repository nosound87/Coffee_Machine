class CoffeMAchine():
    amount_water = 400
    amount_milk = 540
    amount_beans = 120
    amount_disposable = 9
    money = 550

    def __init__(self):
        print("")
        return self.action(input("Write action (buy, fill, take, remaining, exit): \n "))

    def action(self, choice):
        self.choice = choice
        while choice != "exit":
            if choice == "buy":
                print("")
                coffee_type = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n ")
                if coffee_type == "1":
                    self.espresso()
                elif coffee_type == "2":
                    self.latte()
                elif coffee_type == "3":
                    self.cappuccino()
                else:
                    return self.__init__()
            elif choice == "fill":
                print("")
                fill_water = int(input("Write how many ml of water do you want to add:\n> "))
                self.amount_water += fill_water
                fill_milk = int(input("Write how many ml of milk do you want to add:\n> "))
                self.amount_milk += fill_milk
                fill_beans = int(input("Write how many grams of coffee beans do you want to add:\n> "))
                self.amount_beans += fill_beans
                fill_disposable = int(input("Write how many disposable cups of coffee do you want to add:\n> "))
                self.amount_disposable += fill_disposable
                return self.__init__()
            elif choice == "take":
                print("")
                print("I gave you {}".format(self.money))
                self.money -= self.money
                return self.__init__()
            elif choice == "remaining":
                print("")
                self.status_machine()
                return self.__init__()
        return None

    def status_machine(self):
        print("The coffee machine has:")
        print("{} of water".format(self.amount_water))
        print("{} of milk".format(self.amount_milk))
        print("{} of coffee beans".format(self.amount_beans))
        print("{} of disposable cups".format(self.amount_disposable))
        print("{} of money".format(self.money))

    def espresso(self):
        if self.amount_water - 250 > 0 and self.amount_beans - 16 > 0 and self.amount_disposable -1 > 0:
            print("I have enough resources, making you a coffee!")
            self.amount_water -= 250
            self.amount_beans -= 16
            self.amount_disposable -= 1
            self.money += 4
        elif self.amount_water - 250 <= 0:
            print("Sorry, not enough water!")
        elif self.amount_beans - 16 <= 0:
            print("Sorry, not enough beans!")
        elif self.amount_disposable - 1 <= 0:
            print("Sorry, not enough disposable cups!")

    def latte(self):
        if self.amount_water - 350 > 0 and self.amount_milk - 75 > 0 and self.amount_beans - 20 > 0 and self.amount_disposable - 1 > 0:
            print("I have enough resources, making you a coffee!")
            self.amount_water -= 350
            self.amount_milk -= 75
            self.amount_beans -= 20
            self.amount_disposable -= 1
            self.money += 7
        elif self.amount_water - 350 <= 0:
            print("Sorry, not enough water!")
        elif self.amount_milk - 75 <= 0:
            print("Sorry, not enough milk!")
        elif self.amount_beans - 20 <= 0:
            print("Sorry, not enough beans!")
        elif self.amount_disposable - 1 <= 0:
            print("Sorry, not enough disposable cups!")

    def cappuccino(self):
        if self.amount_water - 200 > 0 and self.amount_milk - 100 > 0 and self.amount_beans - 12 > 0 and self.amount_disposable - 1 > 0:
            print("I have enough resources, making you a coffee!")
            self.amount_water -= 200
            self.amount_milk -= 100
            self.amount_beans -= 12
            self.amount_disposable -= 1
            self.money += 6
        elif self.amount_water - 200 <= 0:
            print("Sorry, not enough water!")
        elif self.amount_milk - 100 <= 0:
            print("Sorry, not enough milk!")
        elif self.amount_beans - 12 <= 0:
            print("Sorry, not enough beans!")
        elif self.amount_disposable - 1 <= 0:
            print("Sorry, not enough disposable cups!")

my_express = CoffeMAchine()