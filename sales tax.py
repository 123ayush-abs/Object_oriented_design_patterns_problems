from math import ceil
class Sales_Tax:
    extempGoods = ['books', 'food', 'meds']
    def __init__(self,itemlist):
         self.itemlist=itemlist
         self.finalPrice =[]
         self. finalOutList = []
         self.oldSum = 0
         self.rnd=20 
         self.newSum=0
    def Generate_bill(self):
        for items in self.itemlist:
            tempListItem = items.split()
            tempListItem = [x.replace(' ','') for x in tempListItem]
            exemptFlag = False
            for item in tempListItem:
                if item in Sales_Tax.extempGoods:
                    exemptFlag = True
            if exemptFlag:
                self.oldSum += float(tempListItem[-1])
                priceOfOne = float(tempListItem[-1])/float(tempListItem[0])
                newPrice = (float(tempListItem[-1]) * 0.05)+float(tempListItem[-1])
                newPrice = newPrice * float(tempListItem[0])
                newPrice = ceil(round(newPrice, 2) * self.rnd) / self.rnd
                self.newSum += newPrice
                tempstr = ' '.join(tempListItem[:-1])
                print( tempstr+' ' + str(newPrice))
                self.finalPrice.append(newPrice)
            else:
                if 'imported' in tempListItem:
                    self.oldSum += float(tempListItem[-1])
                    priceOfOne = float(tempListItem[-1])/float(tempListItem[0])
                    newPrice = (float(priceOfOne) * 0.15)+float(priceOfOne)
                    newPrice = newPrice * float(tempListItem[0])
                    self.newSum += newPrice
                    newPrice = ceil(round(newPrice, 2) *  self.rnd) /  self.rnd
                    tempstr = ' '.join(tempListItem[:-1])
                    print( tempstr+' ' + str(newPrice))
                    self.finalPrice.append(newPrice)
                else:
                    self.oldSum += float(tempListItem[-1])
                    priceOfOne = float(tempListItem[-1])/float(tempListItem[0])
                    newPrice = (float(priceOfOne) * 0.10)+float(tempListItem[-1])
                    newPrice = newPrice * float(tempListItem[0])
                    self.newSum += newPrice
                    newPrice = ceil(round(newPrice, 2) *  self.rnd) /  self.rnd
                    tempstr = ' '.join(tempListItem[:-1])
                    print( tempstr+' ' + str(newPrice))
                    self.finalPrice.append(newPrice)
    def print_sales_taxes_stuffs(self):
        print(ceil(round(self.newSum, 2) *  self.rnd) /  self.rnd)
        print(round((ceil(round(self.newSum, 2) *  self.rnd) /  self.rnd)-self.oldSum,2))

itemlist = ['1 book at 12.49','1 music CD at 14.99','1 chocolate bar at 0.85']    
tax=Sales_Tax(itemlist)
tax.Generate_bill()
tax.print_sales_taxes_stuffs()
