from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
import num2words
import copy
width,height = 595.27,841.89
def drawOutline(c):
    c.rect(inch, inch, width - 2 * inch, height - 2 * inch, fill=0)
    c.line(inch, inch + (3/5 * (height - inch)), width - inch,  inch + (3/5 * (height - inch)))
    c.line(inch, 2.75 * inch + (3 / 5 * (height - inch)), (width * 0.5) , 2.75 * inch + (3 / 5 * (height - inch)))
    c.line(width * 0.5, height - inch, width * 0.5, inch + (3/5 * (height - inch)))

    xCoor,yCoor = width * 0.5, height - inch
    for i in range(7):
        c.line(xCoor,yCoor,xCoor * 2 - inch,yCoor)
        yCoor -= inch * 0.34


    c.line(width * 0.75 - inch / 2,height - inch,width * 0.75 - inch / 2,yCoor + inch * 0.34)
    c.line(inch,(3/5 * (height - inch)) + inch / 2,width - inch,(3/5 * (height - inch)) + inch / 2)

    yCoor = height - inch * 1.15
    xCoor = width * 0.5 + inch / 10
    listOfStrs = ["Invoice No.",
                  "Date",
                  "Due Date",
                  "Place of Supply",
                  "Project Code"]
    counter = 0

    otherInfo = {}
    for i in range(len(listOfStrs)//2 + (1 if len(listOfStrs) % 2 == 1 else 0)):
        for j in range(2 if (len(listOfStrs)%2==1) and (i != len(listOfStrs)//2 - 1) else 1):
            try:
                dataToWrite = otherInfo[listOfStrs[counter]]
                if not len(dataToWrite) > 22:
                    dataToWrite = dataToWrite[:23]

            except:
                dataToWrite = "yyyyyyyyyyyyyyyyyyyyyy"
            c.setFont("Times-Roman", 10)
            c.drawString(xCoor + j * inch * 1.5, yCoor, listOfStrs[counter])
            c.setFont("Times-Bold", 10)
            c.drawString(xCoor + j * inch * 1.5, yCoor - 10, dataToWrite)
            counter += 1
        yCoor -= inch * 0.34


def getInput():
    noOfItems = 0
    allItems = []
    while True:
        Desc = input("Enter desc")
        HSN = input("Enter HSN")
        Quantity = input("Enter qty")
        Rate = input("Rate? ")
        per = input("Per? ")
        Continue = input("Continue?")

        allItems.append([Desc,HSN,Quantity,Rate,per])

        if Continue.lower() == "no":
            return allItems

def drawOutline2(c,allItems):
    global height,width
    lastY = None
    heightReq =  0#2 * inch
    billTitles = ["SNO.",
                  "DETAILS",
                  "Quantity",
                  "Rate",
                  "Amount"]

    for itemRow in allItems:
            #if heightReq <= inch + (3/5 * (height - inch)):
        heightReq += inch/3


    inchesProducts = [inch * 0.4, 2.5 * inch + 0.7 * inch, 0.7 * inch, 0.7 * inch, 0]
    if heightReq <= (3 / 5 * (height - inch)):

        allItemsDeleted = copy.deepcopy(allItems)
        LOGO = "LOGO.jpeg"
        c.drawImage(LOGO,inch + 5, 2.75 * inch + (3 / 5 * (height - inch)) - inch * 0.2, preserveAspectRatio=True, mask='auto',width=200)
        fromStr = ["HomePlanGuru Civil Consultants P Ltd",
        "1st Floor, 2, Voltas Colony, II Street",
        "Nanganallur, Chennai",
        "Tamilnadu 600061 IN",
        "Phone:+9144-43585013",
        "www.HomePlanGuru.com"]
        yCoor4 = (3/5 * (height - inch)) + inch * 2 + 7
        c.setFont("Times-Roman", 10)
        for i in fromStr:
            c.drawString(width * 0.5 + 10,yCoor4,i)
            yCoor4 -= inch * 0.2
        xCoor2 = inch
        yCoor = inch + (3 / 5 * (height - inch))
        c.setFont("Times-Bold", 10)
        for heightCount in range(len(billTitles)):
            c.drawString(xCoor2 + 4, inch + (3 / 5 * (height - inch)) - inch / 5, billTitles[heightCount])
            xCoor2 += inchesProducts[heightCount]
        yCoor2 = (3/5 * (height - inch)) + inch/2 - 10
        for row in allItemsDeleted:
            xCoor3 = inch
            for col in range(len(row)):
                c.drawString(xCoor3 + 5, yCoor2, str(row[col]))
                xCoor3 += inchesProducts[col]
            yCoor2 -= (2 * inch) / 7
        xCoor = inch

        for heightCount in range(len(inchesProducts)):
            xCoor += inchesProducts[heightCount]
            c.line(xCoor, yCoor, xCoor,
                   yCoor - heightReq)

        c.line(inch,inch + (3/5 * (height - inch)) - heightReq,width - inch,inch + (3/5 * (height - inch)) - heightReq)
        c.line(inch, inch + (3 / 5 * (height - inch)) - heightReq - (inch * 0.5), width - inch,
               inch + (3 / 5 * (height - inch)) - heightReq - (inch * 0.5))

        lastY = inch + (3/5 * (height - inch)) - heightReq
        if height - inch * 3.5 - lastY > height/4:
            c.showPage()
            c.setFont("Times-Bold", 10)
            c.rect(inch, inch, width - 2 * inch, height - 2 * inch, fill=0)
            lastY = 0

    else:

        allItemsDeleted = copy.deepcopy(allItems)
        excessHeight = heightReq
        heightReq = (3 / 5 * (height - inch))
        iCount = 0
        row = col = 0
        while heightReq <= (height - inch * 2) and heightReq > 0:
            iCount += 1
            xCoor = inch
            xCoor2 = inch
            if iCount == 1:
                yCoor = inch + (3 / 5 * (height - inch))
                for heightCount in range(len(billTitles)):

                    c.drawString(xCoor2 + 4, inch + (3 / 5 * (height - inch)) - inch / 5, billTitles[heightCount])
                    xCoor2 += inchesProducts[heightCount]
            else:
                yCoor = height - inch
                c.showPage()
                c.setFont("Times-Bold", 10)
                c.rect(inch, inch, width - 2 * inch, height - 2 * inch, fill=0)

            for heightCount in range(len(inchesProducts)):
                xCoor += inchesProducts[heightCount]
                c.line(xCoor, yCoor, xCoor,
                       yCoor - heightReq)
            #if excessHeight > (height - inch * 2):


            if iCount == 1:
                yCoor2 = heightReq + inch/5
                reqItemsPerPage = int((heightReq - inch / 2) // (inch / 3))
            else:
                yCoor2 = height - inch * (4/3) + 5
                reqItemsPerPage = int((heightReq) // (inch / 3))

            #print(int(inch),heightReqInt,int(inch//3))
            #print(inch,heightReqInt,inch//3)

            #reqItemsPerPage = int((heightReq) // (inch/3))
            #print((3 / 5 * (height - inch)) // (inch / 3))
            #print(reqItemsPerPage,heightReq)

            for j in range(reqItemsPerPage):
                xCoor3 = inch

                for k in range(len(inchesProducts)):
                    try:
                        c.drawString(xCoor3 + 5,yCoor2,str(allItemsDeleted[row][k]))


                    except:
                        print(allItemsDeleted)

                    xCoor3 += inchesProducts[k]
                row += 1
                yCoor2 -= inch/3
                #allItemsDeleted.remove(allItemsDeleted[0])
            excessHeight -= heightReq
            noOfPagesLeft = (excessHeight // (height - inch * 2))
            if not (noOfPagesLeft == 0):
                heightReq = (height - inch * 2)
            else:
                heightReq = excessHeight % (height - inch * 2)
            if (heightReq == excessHeight) and (lastY == None):
                lastY = heightReq


        c.line(inch,height - inch - lastY,width - inch,height - inch - lastY)
        if not (height - inch * 1.5 - lastY) < inch:
            c.line(inch, height - inch * 1.5 - lastY, width - inch,
                   height - inch * 1.5 - lastY)  # oops forgot the money thingy, yk money words thingy
        else:
            c.showPage()
            lastY = height - inch
            c.line(inch, height - inch * 2, width - inch,
                   height - inch * 2)
            c.rect(inch, inch, width - 2 * inch, height - 2 * inch, fill=0)
        if not (height - inch * 2.5 - lastY) < inch:
            c.line(inch, height - inch * 2.5 - lastY, width - inch, height - inch * 2.5 - lastY)

            lastY = height - inch * 2.5 - lastY
        else:
            c.showPage()
            lastY = height - inch
            c.line(inch, height - inch * 2, width - inch,
                   height - inch * 2)
            c.rect(inch, inch, width - 2 * inch, height - 2 * inch, fill=0)

    bankReference = ["BANK REFERENCE:",
                    "Cheque / DD shall be paid in favour of : M/s HomePlanGuru Civil",
                    "Consultants Pvt Limited payable at : Chennai.",
                    "Funds Transfer shall be done in favour of M/s HomePlanGuru",
                    "Civil Consultants Pvt Ltd to the Axis Bank, Nanganallur Branch,",
                    "Chennai",
                    "Current Account Number: 913020014289687",
                    "IFS Code: UTIB0000486"]

    c.setFont("Helvetica", 7)
    if not  (lastY - 4 * inch) < 0:
        yCoor = lastY - 0.3 * inch
        for i in bankReference:
            c.drawString(inch * 1.3 , yCoor,i)
            yCoor -= inch * 0.3

    else:
        c.showPage()
        c.rect(inch, inch, width - 2 * inch, height - 2 * inch, fill=0)
        lastY = height - inch
        yCoor = lastY - 0.3 * inch
        for i in bankReference:
            c.drawString(inch * 1.3, yCoor, i)
            yCoor -= inch * 0.3





    '''
    if not (height - inch * 3.5 - lastY) < inch:
        c.line(inch, height - inch - lastY, width - inch, height - inch * 3.5 - lastY)
    else:
        c.showPage()
        lastY = height - inch
        c.line(inch, height - inch * 2, width - inch,
               height - inch * 2)
        c.rect(inch, inch, width - 2 * inch, height - 2 * inch, fill=0)
    '''

'''
def addData(allItems,otherInfo,selfBuyerInfoFile=None):
    for i in otherInfo:
'''

def main():
    c = canvas.Canvas("invoice.pdf")

    abc = []

    for i in range(1,16):
        bcd = []
        for j in range(1,6):
            if j == 1:
                bcd.append(i)
            else:
                bcd.append(j)
        abc.append(bcd)
    drawOutline(c)
    drawOutline2(c,abc)
    c.showPage()
    c.save()
if __name__ == "__main__":
    main()