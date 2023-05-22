import os
from colorama import Fore, Back
from random import randint

def printWhite(data):
    print(Fore.WHITE,data,end="",sep="")

def printRed(data):
    print(Fore.RED,data,end="",sep="")

def printGreen(data):
    print(Fore.GREEN,data,end="",sep="")

def screenXO(screen):
    os.system('cls')

    
    corners = {
               "upperLeft":     "┌",    #218 np. chr(218)
               "upperRight":    "┐",    #191
               "mediumLeft":    "├",    #195 
               "mediumRight":   "┤",    #180
               "bottomLeft":    "└",    #192
               "bottomRight":   "┘",    #217
               "upperMid":      "┬",    #194
               "midiumMid":     "┼",    #197
               "bottomMid":     "┴"     #193
              }
    lines =   {
               "vertical": "│",         #179
               "horizontal": "─"        #196
              }
    
    size = len(screen)                  #rozmiar ekranu

    verticalLine = [lines["horizontal"]*3]*size         #lista zawierająca poziome linie
    # print(verticalLine)
    
    verticalUp = corners["upperMid"].join(verticalLine)
    verticalMid = corners["midiumMid"].join(verticalLine)
    verticalDown = corners["bottomMid"].join(verticalLine)
    # print(verticalUp)
    # print(verticalMid)
    # print(verticalDown)

   

    printWhite(corners["upperLeft"]+verticalUp+corners["upperRight"]+"\n")
 
    for i,row in enumerate(screen):
        printWhite(lines["vertical"])
        for j in row:
            if j == 1: printGreen(" X ")
            elif j == -1: printRed(" O ")
            else: printWhite("   ")
            printWhite(lines["vertical"])            
        print()
        if(i < size-1): printWhite(corners["mediumLeft"]+verticalMid+corners["mediumRight"]+"\n")

    printWhite(corners["bottomLeft"]+verticalDown+corners["bottomRight"]+"\n")

def ustawRuch(x, y, gracz):
    if x in range(3) and y in range(3):
        if dane[y][x] == 0:
            dane[y][x] = gracz
            return True
        else:
            if gracz == 1 or not komputer: input("Pole jest już zajęte")
            return False
    else:
        if gracz == 1 or not komputer: input("Podano błędne współrzędne")
        return False

def sprawdzWygrana():
    if (
        dane[0][0] == dane[1][0] == dane[2][0] or
        dane[0][1] == dane[1][1] == dane[2][1] or
        dane[0][2] == dane[1][2] == dane[2][2] or
        dane[0][0] == dane[0][1] == dane[0][2] or
        dane[1][0] == dane[1][1] == dane[1][2] or
        dane[2][0] == dane[2][1] == dane[2][2] or
        dane[0][0] == dane[1][1] == dane[2][2] or
        dane[0][2] == dane[1][1] == dane[2][0]
    ):
        return True
    else:
        return False

if __name__ == "__main__":
    
    dane = []
    komputer = 0
    gracz = 0
    ruch = 0
    
    for i in range(3):
        kolumna = [0 for i in range(3)]
        dane.append(kolumna)
    
    while True:
        os.system('cls')
        wyborKomputer = input("Czy chcesz grać na komputer?(T/N)\n")
        if wyborKomputer == "T":
            komputer = True
            break
        elif wyborKomputer == "N":
            komputer = False
            break
        else: input("Podano błędne dane")
    
    gracz = randint(0, 1)
    if gracz == 0:
        gracz = -1
        input("Zaczyna gracz 2")
    else: input("Zaczyna gracz 1")
    
    while True:
        try:
            screenXO(dane)
            if gracz == 1:
                if komputer: printWhite("Twój ruch\n")
                else: printWhite("Gracz 1\n")
            elif not komputer: printWhite("Gracz 2\n")
            if gracz == 1 or not komputer:
                x = int(input("Podaj wsp x: "))
                y = int(input("Podaj wsp y: "))
            else:
                x = randint(0, 2)
                y = randint(0, 2)
            if(ustawRuch(x, y, gracz)):
                ruch += 1
                if ruch > 4:
                    if(sprawdzWygrana()):
                        screenXO(dane)
                        if gracz == 1:
                            if komputer: printWhite("Wygrałeś")
                            else: printWhite("Wygrał gracz 1")
                        else:
                            if komputer: printWhite("Przegrałeś")
                            else: printWhite("Wygrał gracz 2")
                        break
                    elif ruch == 9:
                        screenXO(dane)
                        printWhite("Remis")
                        break
                gracz *= -1
        except: input("Podano błędne dane")
