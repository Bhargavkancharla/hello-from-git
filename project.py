veg=['tomato','carrot','brinjal','cabbage','onions','cauliflower','beetroot',
         'potato','peas','bitter gourd','green beens','mushroom','spinach','capsicum',
         'green mrichi','cucumber']
quantity=[30,10,15,9,50,15,10,15,5,10,7,5,10,5,25,7]
price=[20,45,45,30,35,20,45,50,65,25,40,150,10,55,30,45]
original_cost=[15,40,35,25,30,15,35,40,45,12,27,100,7,45,15,40]
report=[]
items_list1=[]
quantity_list1=[]
price_list1=[]
amount_list1=[]
user_name=[]
user_phone=[]
s=[]
while True:
    print('*'*25,"SUPER MARKET",'*'*25)
    print("1.Shop Owner ")
    print("2.Customer")
    print("3.Exit")
    ch=input("Chooese one option:")

    if ch=='1':
        username=input("Enter Username:")
        password=input("Enter password:")
        if username=='bhargav' and password=='1234':
            while True:
                
                print("1.Add item ")
                print("2.Remove item")
                print("3.User details")
                print("4.View items")
                print("5.Update item")
                print("6.View report")
                print("7.Total Revenu")
                print("8.Exit")
                ch1=input("Enter your option:")
                if ch1=='1':
                    print("1.add items")
                    print("2.add quantity")
                    print("3.add price")
                    print("4.exit")
                    while True:
                        ch2=int(input("Enter your option:"))
                        if ch2==1:
                            item=input("Enter item to add:")
                            veg.append(item)
                        if ch2==2:
                            qut=int(input("Enter the quantity:"))
                            quantity.append(qut)
                        if ch2==3:
                            pri=int(input("Enter the price:"))
                            price.append(pri)
                        if ch2==4:
                            print("exiting from updation")
                            break
                elif ch1=='2':
                    print("1.remove item")
                    print("2.exit")
                    while True:
                        ch2=int(input("Enter the option:"))
                        if ch2==1:
                            item=input("Enter the item to remove:")
                            idx=veg.index(item)
                            print(idx)
                            veg.pop(idx)
                            quantity.pop(idx)
                            price.pop(idx)
                            print(veg)
                            print(quantity)
                            print(price)
                        if ch2==2:
                            print("exiting from the removing data")
                            break
                elif ch1=='3':
                    print('*'*25,'USER DETAILS','*'*25)
                    print("-"*100)
                    print(f"{'User Name':^20} {'Phone Number':^20}")
                    print("-"*100)
                    for i,j in zip(user_name,user_phone):
                        print(f"{i:^20} {j:^20}")
                elif ch1=='4':
                    print("Items in our Cart")
                    print("-"*100)
                    print(f"{'vegtable name':^20} {'price per kg':^10}")
                    print("-"*100)
                    for i,j in zip(veg,price):
                        print(f"{i:^20} {j:^10}")
                elif ch1=='5':
                    a=int(input("Enter 1 for update quantity 2 for update the price:"))
                    if a==1:
                        inpu=input("enter the item to update the quantity:")
                        idx=veg.index(inpu)
                        quantity[idx]=int(input("enter the  quantity:"))
                        print(quantity)
                    elif a==2:
                        inpu=input("enter the item to update price:")
                        idx=veg.index(inpu)
                        price[idx]=int(input("enter the price:"))
                        print(price)
                    else:
                        break
                elif ch1=='6':
                    print("----------------------VIEW REPORT-----------------------")
                    for i in items_list1:
                        idx=veg.index(i)
                        idx1=items_list1.index(i)
                        quantity[idx]=quantity[idx]-quantity_list1[idx1]
                    print("-"*100)
                    print(f"{'vegtable name':^20} {'quantity':^10}")
                    print("-"*100)
                    for i,j in zip(veg,quantity):
                        print(f"{i:^20} {j:^10}")
                    print("---------------------------------------------------------")
                elif ch1=='7':
                    for i in items_list1:
                        idx=veg.index(i)
                        report.append(price[idx]-original_cost[idx])
                    for j in items_list1:
                        idx=items_list1.index(j)
                        c=quantity_list1[idx]*report[idx]
                        s.append(c)
                    print("-"*100)
                    print(f"{'vegtables':^20} {'quantity':^20} {'profit':^20} {'profit based on quantity':^20}")
                    print("-"*100)
                    for k,l,m,n in zip(items_list1,quantity_list1,report,s):
                        print(f"{k:^20} {l:^20} {m:^20} {n:^20}")
                    print("-"*100)
                    print("TOTAL PROFITE:",sum(s))
                    print("-"*100)

                    
                elif ch1=='8':
                    break
                else:
                    print("chooese correct option")
        else:
            print("Please Enter correct username and password")
    elif ch=='2':
        total_amount=0
        amount_list=[]
        items_list=[]
        quantity_list=[]
        price_list=[]
        items_list1.clear()
        quantity_list1.clear()
        price_list1.clear()
        s.clear()
        while True:
                
                print('*'*25,'WELCOME TO SUPER MARKET','*'*25)
                print("1.Add to cart")
                print("2.Remove Cart")
                print("3.Modify cart")
                print("4.View cart")
                print("5.Billing")
                print("6.Exit")
                op=input("Enter your option:")
                if op=='1':
                    print("-"*100)
                    print(f"{'vegtable':^20} {'quantity':^20} {'price':^20}")
                    print("-"*100)
                    for i,j,k in zip(veg,quantity,price):
                        print(f"{i:^20}{j:^20} {k:^20}")
                    while True:
                        inp=input("Enter  your item to buy:")
                        if inp in veg:
                            qut=int(input("Enter how many kgs you want:"))
                            idx=veg.index(inp)
                            if qut<=quantity[idx]:
                                if inp in items_list:
                                    print("chooese option 3 if you want to modify the same item")
                                    break
                                else:
                        
                                    items_list.append(inp)
                                    quantity_list.append(qut)
                                    price_list.append(price[idx])
                            else:
                                print("Out Of Stock")
                        else:
                            print("Item is not in the cart")
                        inp1=input("Do You Want To Buy more items press yes/No:")
                        if inp1=='no' or inp1=='No':
                            break
                           
                elif op=='2':
                    print("TO REMOVE ITEM FROM THE CART")
                    item=input("Enter your item to remove from the cart:")
                    if item in items_list:
                        idx=items_list.index(item)
                        items_list.pop(idx)
                        quantity_list.pop(idx)
                        price_list.pop(idx)
                    else:
                        print("item is not in your cart")
                elif op=='3':
                    inp1=input("Enter your item:")
                    if inp1 in items_list:
                        idx=items_list.index(inp1)
                        quantity_list[idx]=int(input("Enter the quantity to modify:"))
                    else:
                        print("Item is not in your cart:")
                elif op=='4':
                    print("*"*100)
                    print(f"{'vegtable names':^20} {'quantity':^10}")
                    print("*"*100)
                    for i,j in zip(items_list,quantity_list):
                        print(f"{i:^20} {j:10}")
                elif op=='5':
                    name=input("Enter your name:")
                    phone=input("enter your mobile number:")
                    a = ['1','2','3','4','5','6','7','8','9','0']
                    for i in phone:
                        if i not in a:
                            print('phone number having only digits')
                            break
                    else:
                        if name.isalpha()or name.count(' ')==1:
                            
                            if phone.isdigit() and len(phone) == 10 and phone[0] >= '6':
                                            user_name.append(name)
                                            user_phone.append(phone)
                                            items_list1.extend(items_list)
                                            quantity_list1.extend(quantity_list)
                                            price_list1.extend(price_list)
                                            print(items_list1)
                                            print(quantity_list1)
                                            print(price_list1)
                                            print('*'*25,'THIS IS YOUR BILL','*'*25)
                                            for i in range(len(items_list)):
                                                amount=quantity_list[i]*price_list[i]
                                                amount_list.append(amount)
                                            total_amount=sum(amount_list)
                                            if total_amount!=0:
                                                
                                                print("*"*100)
                                                print(f"{'items':^20} {'qunatity':^20} {'price':^20} {'amount':^20}")
                                                print("*"*100)
                                                for i,j,k,l in zip(items_list,quantity_list,price_list,amount_list):
                                                
                                                    print(f"{i:^20} {j:^20} {k:^20} {l:^20}")

                                                print("TOTAL AMOUNT=",total_amount)
                                            else:
                                                print("THEIR IS NO BILL YOU BECAUSE YOU NOT BUY ANY ITEMS") 
                                
                            else:
                                print("Enter the valide number")
                        else:
                            print("Please enter a valide name not numbers or specail charchters")
                elif op=='6':
                    print('*'*25,'THANK YOU VISIT AGAIN','*'*25)
                    break
                else:
                    print("chooese correct option")
                
    elif ch=='3':
        break
    else:
        print("Chooese correct option")
