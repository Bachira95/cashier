def main():
        # write code here
        #inp=0
        con=True
        listofItems=[]
        dicti={}
        i=0
        while con:
                inp=input("Item (enter \"done\" when finished): ")
                if inp=="done":
                        con=False
                        break
                else:
                        price=float(input("Price: "))
                        quantity=int(input("Quantity: "))
                        dicti.update({"name":inp})
                        dicti.update({"price":price})
                        dicti.update({"Quantity":quantity})
                        #listofItems.insert(i,dicti)
                        #print(listofItems)
                #print (dicti)        
                listofItems.append(dict(dicti))
                i+=1

        print()
        print ("--------------")        
        print ("receipt")
        print ("--------------")
        total=0
        for d in range(0,len(listofItems)):
                
                print(str(listofItems[d]["Quantity"])+" "+listofItems[d]["name"]+" "+str(listofItems[d]["Quantity"]*listofItems[d]["price"]))
                total=total+listofItems[d]["Quantity"]*listofItems[d]["price"]
        print ("--------")
        print(f"Total Price:{str(total)} KD")
                #for key in d:
                    #print("{}:{}".format (key, d[key))
                                        
        #print(listofItems)
if __name__ == '__main__':
        main()

