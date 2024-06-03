import random

class Management():
    def __init__(self):
        self.myInventory = []
        self.salesHistory = []

    def generateUniqueID(self):
        RandomNumber = random.randint(100000,999999)
        return RandomNumber

    def addItem(self, ItemName):
        self.myInventory.append({"Item": ItemName, "Id": self.generateUniqueID()})

    def removeItem(self, ItemID):
        for i in self.myInventory:
            for index, value in i.items():
                try:
                    int(value)
                except ValueError:
                    continue

                if int(value) == int(ItemID):
                    print("[Removed]: Item")
                    self.salesHistory.append(i)
                    self.myInventory.remove(i)

    def getInventory(self):
        return self.myInventory
    
    def salesReport(self):
        return self.salesHistory
    
    def inventoryLevel(self):
        return len(self.myInventory)


if __name__ == "__main__":
    Inventory = Management()
    while True:
        OptionsInput = input("[ What would you like to do? [1]: View Inventory [2]: Add Item [3]: Remove Item [4]: Provide Report: [5]: Inventory Levels ]: ")

        try:
            Input = int(OptionsInput)
        except ValueError:
            print("[Invalid Input] Please enter a valid number!")
            continue
    
        if int(OptionsInput) == 1:
            print(f"Inventory: {Inventory.getInventory()}")
        elif int(OptionsInput) == 2:
            ItemName = input("Enter The Item's Name You Wish To Add: ")
            print(f"[Added]: {ItemName}")
            Inventory.addItem(ItemName)
        elif int(OptionsInput) == 3:
            ItemID = input("Enter The Item's ID You Wish To Remove: ")
            Inventory.removeItem(ItemID)
        elif int(OptionsInput) == 4:
            print(Inventory.salesReport())
        elif int(OptionsInput) == 5:
            print(Inventory.inventoryLevel())

