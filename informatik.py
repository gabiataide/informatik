import random

chores = ["Clean WC", "Laundry (Bedding)", "Relax", "Laundry (Clothes)", "Vacuuming", "Grocery shopping",
          "Fold Clothes (if any)", "Meal Prep", "Clean Shower", "Change Bedsheets", "Relax", "Reorganize Cabinet Contents", "Relax",
          "Clean Kitchen", "Mop Floors", "Relax", "Dust the Living Room", "Relax", "Declutter Living Room"]
week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

random.shuffle(chores)


class GabiKondo:
    """
    A class used to distribute household chores to up to 3 users.

    A
    """

    def __init__(self):
        """
        Receive input on number of people living in household and redirects to corresponding function based on input.
        """

        how_many = int(input("\n How many people live under your roof? (Max. of 3)  "))
        if how_many == int(1):
            self.onlyone()
        else:
            self.morethanone()

    def onlyone(self):
        """
        generate a row of strings based on 'name' input.

        :return: row of strings with randomized chores for one user.
        :rtype: str
        """
        names = []
        add_name = input("\n Enter your name: ")
        names.append(add_name)
        print("\n *** Weekly household chores for", add_name, "*** \n")
        for day in week:
            for name in names:
                chore = chores.pop()
                if name == "Jonas":
                    assign = day + " " + " - " + chore + " and Cook Dinner"
                    print(assign)
                else:
                    assign = day + " " + " - " + chore
                    print(assign)

    def morethanone(self):
        """
        generate a row of strings based on 'name' and number of participants 'how_many' input.

        :return: row of strings with randomized chores for up to three user.
        :rtype: str
        """
        how_many = int(input("\n How many of those are willing to bring joy to your place? "))
        for i in range(int(how_many)):
            names = []
            add_name = input("\nEnter your name: ")
            names.append(add_name)

            for day in week:
                for name in names:
                    chore = chores.pop()
                    if name == "Jonas":
                        assign = day + " " + " - " + chore + " and Cook Dinner"
                        print(assign)
                    else:
                        assign = day + " " + " - " + chore
                        print(assign)


GabiKondo()
