import random

chores = ["Clean WC", "Laundry (Bedding)", "Laundry (Clothes)", "Vacuuming", "Groceries", "Fold Clothes",
          "Meal Prep", "Clean Bathroom", "Change Bedsheets", "Reorganize Cabinets", "Hang Clothes to dry",
          "Clean Kitchen", "Mop Floors", "Dust the Living Room"]
random.shuffle(chores)


def gabiclean():
    week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    names = []
    add_name = input("\nEnter your name: ")
    names.append(add_name)
    print("\n*** Weekly household chores for", add_name, "*** \n")

    for day in week:
        for name in names:
            chore = chores.pop()
            if name == "Jonas":
                assign = day + " " + " - " + chore + " and Cook Dinner"
                print(assign)

            else:
                assign = day + " " + " - " + chore
                print(assign)


