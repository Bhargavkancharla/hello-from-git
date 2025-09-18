from datetime import datetime

name=input("Enter your name:")

print("Press 1 To Display Items")
print("Press 2 To Exit")

choice=int(input("Enter Your Option:"))

price=0
price_list=[]
total_price=0
item_list=[]
quantity_list=[]
final_amount=0
plist=[]

items={'Rice':180,'Sugar':40,'Salt':15,'Oil':125,'Headnsholder':150,'Santoor Soap':35,
       'Onions':20,'Termaric':10,'Chicken Masala':5}
if choice==1:
    list='''
         Rice           : 180 RS per KG
         Sugar          : 40 RS per KG
         Salt           : 15 RS per PACKET
         Oil            : 125 RS 1 liter
         Headnsholder   :150 500 GM
         Santoor Soap   : 35 RS 250 GM
         Onions         : 20 RS 1 KG
         Termaric       : 10 RS 100 GM
         Chicken Masala :5 RS 50 GM      '''
    print(list)
    for i in range(len(items)):
        print("If you want to Buy press 1 or Exit press 2")
        inp=int(input("Enter here:"))
        if inp==2:
            break
        if inp==1:
            item=input("Enter Your item:")
            if item in items.keys():
                quantity=int(input("Enter The Quantity:"))
                price=quantity*(items[item])
                price_list.append((item,quantity,price))
                total_price=total_price+price
                item_list.append(item)
                quantity_list.append(quantity)
                plist.append(price)
                gst=(total_price*5)/100
                final_amount=gst+total_price
            else:
                print("Entered item is not found in the market")
        else:
            print("Enter Correct Number")
    inp1=input("Enter yes for Bill:")
    if inp1=='Yes' or 'yes':
        if final_amount !=0:
            print(25*"=","WELLCOME TO BHARGAV SUPER MARKET",25*"=")
            print(35*" ","GARAPADU",25*" ")
            print("SNo","Item","Quantity","Price")
            for i in range(len(price_list)):
                print(i,2*" ",item_list[i],2*" ",quantity_list[i],2*" ",plist[i])
            print(25*"-")
            print("TOTAL AMOUNT =",final_amount)
            print(25*"=","Please Visit Again:",name,25*"=")
elif choice==2:
    print("********** Thank You Visit Again **********")
