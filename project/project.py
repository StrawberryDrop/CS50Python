import csv
code = 31250

def main():
    type = input("Are you a customer or producer? ")
    type = type.strip().lower()
    if(type == "customer"):
        ordered = input("New or Current order? ").strip().lower().replace("order"," ")

        if(ordered == "new"):
            exist = True
            size = input("What Size? Type S for small, M for medium, and L for large? ")
            Numtoppings = input("How many toppings? ")
            Whattoppings = input("What toppings do you want? (comma seperated list) ").strip()
            while(exist):
                name = input("What is the name of the order? ")
                nprint,exist = new (name,size,Numtoppings,Whattoppings)
            print (nprint)
        elif(ordered == "current"):
            name = input("What is the name of the order? ")
            x = current(name)
            if (x == 4):
                checkout = input("Would you like to pick up your order? Y or N ").strip()
                print(pickup(checkout,name))
    elif(type == "producer"):
        check = 0
        while(check != code):
         check = int(input("Code: ").strip())
        name = input("What is the name of the order? ")
        update = input("Do you want to update Status? Y or N ").strip().lower()
        print(produce(name, update))





def new(ordern,size,Numtoppings,Whattoppings):
    exist = False
    with open ("project.csv","r+") as file:
        try:
            reader = csv.DictReader(file,fieldnames=['Order name','Size','Number of toppings','Toppings','Status of Order'])
            for row in reader:
                 if (row['Order name'] == ordern):
                    exist = True
                    raise Exception()
            writer = csv.DictWriter(file, fieldnames=['Order name','Size','Number of toppings','Toppings','Status of Order'])
            writer.writerow({'Order name':ordern ,'Size': size ,'Number of toppings': Numtoppings , "Toppings":Whattoppings , 'Status of Order': "0" })
        except:
            print("Name already exists")
        return "Order Placed:  \n Order name:"+ ordern +" \n Size:"+size+"\n Number of toppings: "+ Numtoppings+ "\n Toppings: "+Whattoppings+"\n Status of Order: "+stat(0),exist





def current(orderc):
    orders =[]
    with open("project.csv") as file:
        reader = csv.DictReader(file,fieldnames=['Order name','Size','Number of toppings','Toppings','Status of Order'])
        for row in reader:
            orders.append({"Order name": row['Order name'], "Size": row['Size'], "Number of toppings": row['Number of toppings'], "Toppings": row['Toppings'], "Status of Order": row['Status of Order'] })
        for order in orders:
            if(order["Order name"] == orderc):
                print(f"Order name: "+order['Order name']+"  Size: "+order["Size"]+"  Number of toppings: "+order['Number of toppings']+" Toppings: "+order['Toppings']+"  Status of Order: "+ stat(int(order['Status of Order'])))
                return int(order["Status of Order"])


def pickup(check,orderm):
    if check == "y" or check == "Y":
        che = True
        orders =[]
        with open("project.csv","r+") as file:
            reader = csv.DictReader(file,fieldnames=['Order name','Size','Number of toppings','Toppings','Status of Order'])
            for row in reader:
                orders.append({"Order name": row['Order name'], "Size": row['Size'], "Number of toppings": row['Number of toppings'], "Toppings": row['Toppings'], "Status of Order": row['Status of Order'] })
            for order in orders:
                    if(order["Order name"] == orderm):
                        orders.remove(order)
            file.truncate(0)
            file.seek(0)
            writer = csv.DictWriter(file,fieldnames=['Order name','Size','Number of toppings','Toppings','Status of Order'])
            for order in orders:
                if(order["Order name"] != orderm):
                    writer.writerow(order)
            if(che):
                return "Pick up for "+orderm
    else:
        return "Okay! Come back when you are Ready!"


def stat(level):
    match level:
        case 0: return "Ordered"
        case 1: return "Prepared"
        case 2: return "In the Oven"
        case 3: return "Packing"
        case 4: return "Ready for Pickup"

def produce(orderp,update):
    orders =[]
    old = 0
    new = 0
    with open("project.csv","r+") as file:
        reader = csv.DictReader(file,fieldnames=['Order name','Size','Number of toppings','Toppings','Status of Order'])
        for row in reader:
            orders.append({"Order name": row['Order name'], "Size": row['Size'], "Number of toppings": row['Number of toppings'], "Toppings": row['Toppings'], "Status of Order": row['Status of Order'] })
        for order in orders:
            if(order["Order name"] == orderp):
                print(f"Order name: "+order['Order name']+"  Size: "+order["Size"]+"  Number of toppings: "+order['Number of toppings']+" Toppings: "+order['Toppings']+"  Status of Order: "+ stat(int(order['Status of Order'])))
                old = order['Status of Order']
                if (update == "Y" or update == "y"):
                    order['Status of Order'] = str(int(order['Status of Order'])+1)
        file.truncate(0)
        file.seek(0)
        writer = csv.DictWriter(file,fieldnames=['Order name','Size','Number of toppings','Toppings','Status of Order'])
        for order in orders:
            if(order["Order name"] == orderp):
                new = order['Status of Order']
            writer.writerow(order)
    return "Status: old: " + stat(int(old))+" --> new: "+stat(int(new))



if __name__ == "__main__":
    main()



