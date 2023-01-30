





def getitemslist(path = r"./Tarkitems.csv") -> list:
    fichierliste = open(path , "r")
    itemlist = fichierliste.read().split("\n")
    for i in range(len(itemlist)):
        itemlist[i] = itemlist[i].split(",")
    return itemlist