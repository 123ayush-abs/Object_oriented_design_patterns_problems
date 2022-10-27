from math import ceil
def salesTax(itemList):
    
    extempGoods = ['books', 'food', 'meds']
    
    finalOutList = []
    finalPrice =[]
    oldSum = 0
    newSum = 0
    rnd = 20
    
    for items in itemList:
        tempListItem = items.split()
        
        tempListItem = [x.replace(' ','') for x in tempListItem]
        
        
        exemptFlag = False
        
        for item in tempListItem:
            if item in extempGoods:
                exemptFlag = True
                
        
        if exemptFlag:
            oldSum += float(tempListItem[-1])
            priceOfOne = float(tempListItem[-1])/float(tempListItem[0])
            
            newPrice = (float(tempListItem[-1]) * 0.05)+float(tempListItem[-1])
            
            newPrice = newPrice * float(tempListItem[0])
            newPrice = ceil(round(newPrice, 2) * rnd) / rnd
            newSum += newPrice
            tempstr = ' '.join(tempListItem[:-1])
            print( tempstr+' ' + str(newPrice))
            finalPrice.append(newPrice)
        else:
            if 'imported' in tempListItem:
                oldSum += float(tempListItem[-1])
                priceOfOne = float(tempListItem[-1])/float(tempListItem[0])
                
                newPrice = (float(priceOfOne) * 0.15)+float(priceOfOne)
                
                newPrice = newPrice * float(tempListItem[0])
                newSum += newPrice
                newPrice = ceil(round(newPrice, 2) * rnd) / rnd
                tempstr = ' '.join(tempListItem[:-1])
                print( tempstr+' ' + str(newPrice))
                finalPrice.append(newPrice)
            else:
                oldSum += float(tempListItem[-1])
                priceOfOne = float(tempListItem[-1])/float(tempListItem[0])
                
                newPrice = (float(priceOfOne) * 0.10)+float(tempListItem[-1])
                
                newPrice = newPrice * float(tempListItem[0])
                newSum += newPrice
                newPrice = ceil(round(newPrice, 2) * rnd) / rnd
                tempstr = ' '.join(tempListItem[:-1])
                print( tempstr+' ' + str(newPrice))
                finalPrice.append(newPrice)
                 
    print(oldSum)  
    print(ceil(round(newSum, 2) * rnd) / rnd)   
    print(round((ceil(round(newSum, 2) * rnd) / rnd)-oldSum,2))
           
            
itemlist = ['1 imported box of food at 10.00','1 imported bottle of perfume at 47.50']        

salesTax(itemlist)