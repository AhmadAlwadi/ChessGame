#list of things i need to do later: ['Make it transparent (look at TransparentBKGD.py)']


import pygame, time, random, sys, json
#Colors
black = (0, 0, 0)
white = (255, 255, 255)
gray = (144, 144, 144)
lightblue = (173, 216, 230, 200)

#Possible piece types: [King, Rook, Bishop, Queen, Knight, Pawn]
#Position will be a property of each piece and it will be in the
#form of [int, int] as in [x, y]
#positions on the grid will be labeled 1 to 8

#Global vars
pygame.init()
pieces = []
clock = pygame.time.Clock()
pygame.display.set_caption("Chess Game That Will Probably Not Work")
screen_width = 1000
screen_height = 1000
display = pygame.display.set_mode((screen_width, screen_height))
#this dict holds all the positions to be dumped to json
posHistory = {}
posHistory['postions'] = []

#This is to make a grid
def make_grid(width, height):
    gridline = []
    for i in range(0, width):
        gridline.append(i)
    grid = []
    for j in range(0, height):
        grid.append(list(gridline))
    for i in range(len(grid)):
        print(grid[i])
    return grid
#This is to draw the grid
def draw_grid(grid):
    x = 100
    y = 100
    filled = 0
    color = ''
    counter = 0
    #Current comparision is a variable that is used to aid
    # the program choosing a color for the grid
    current_comparision = 0
    for i in range(len(grid)):
        current_comparision = i%2
        #This is to print them horizontally
        for j in range(len(grid)):
            if current_comparision == 0:
                if j%2 == 0:
                    color = white
                else:
                    color = black
            else:
                if j%2 == 0:
                    color = black
                else:
                    color = white
            pygame.draw.rect(display, color, [x, y, 100, 100], filled)
            x += 100
        x = 100
        y += 100

#Importing & populating the pieces
def import_data(grid):
    with open('pieces.json') as f:
        data = json.load(f)
    for i in data['pieces']:
        pieces.append(i)

    #making the grid self aware
    #storing the piece ids into a list, i will then break into into segments of 8 and store it in
    #a different list
    pieceIDs = []
    for i in pieces:
        pieceIDs.append(i['pieceID'])
    print(pieceIDs)

    #making the list have a length of 64 with a zero in the places that don't have a piece
    for i in range(0, 63):
        if pieceIDs[i] != i+1:
            pieceIDs.insert(i, 0)

    #breaking the list into lists of 8
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    list5 = []
    list6 = []
    list7 = []
    list8 = []
    counter = 0
    for i in range(0, 8):
        list1.append(pieceIDs[i])
    for i in range(8, 16):
        list2.append(pieceIDs[i])
    for i in range(16, 24):
        list3.append(pieceIDs[i])
    for i in range(24, 32):
        list4.append(pieceIDs[i])
    for i in range(32, 40):
        list5.append(pieceIDs[i])
    for i in range(40, 48):
        list6.append(pieceIDs[i])
    for i in range(48, 56):
        list7.append(pieceIDs[i])
    for i in range(56, 64):
        list8.append(pieceIDs[i])

    print(list1, '\n', list2, '\n', list3, '\n', list4,
     '\n', list5, '\n', list6, '\n', list7, '\n', list8, '\n')

    for i in range(len(grid)):
        if i == 0:
            grid[i] = list1
        elif i == 1:
            grid[i] = list2
        elif i == 2:
            grid[i] = list3
        elif i == 3:
            grid[i] = list4
        elif i == 4:
            grid[i] = list5
        elif i == 5:
            grid[i] = list6
        elif i == 6:
            grid[i] = list7
        elif i == 7:
            grid[i] = list8
    print(grid)

def draw_images(pieces):
    #how to blit an image
    #display.blit(Black_rook_image, [800,100])
    for i in pieces:
        #print(i['pos'])
        image_name = 'Resources/'.strip() + i['team'].strip() + "_" + i['type'].lower().strip() + '.png'
        #print(image_name)
        image = pygame.image.load(image_name)
        display.blit(image, i['pos'])


def round_pos(pos):
    pos = list(pos)
    x = pos[0]
    y = pos[1]
    x /= 100
    y /= 100
    x = int(x) * 100
    y = int(y) * 100
    pos = [x, y, 100, 100]
    return pos

def validatePos(pos):
    x, y, posValid = pos[0], pos[1], False
    newPos = [x, y]
    if x < 100 or x > 800:
        posValid = False
    else:
        if y < 100 or y > 800:
            posValid = False
        else:
            #if checkForPiece(newPos) == True:
            posValid = True
    return posValid

def checkForPiece(pos):
    x, y = pos[0], pos[1]
    pieceNumber, rowNumber = int((x/100)-1), int((y/100)-1)
    #new list will hold all the pices in the correct row
    newList = grid[rowNumber]
    holderVal = newList[pieceNumber]
    if holderVal > 0:
        return True
    else:
        return False

def checkTeam(pos):
    x, y = pos[0], pos[1]
    pieceNumber, rowNumber = int((x/100)-1), int((y/100)-1)
    #new list will hold all the pices in the correct row
    newList = grid[rowNumber]
    holderVal = newList[pieceNumber]
    team = ''
    index = 0 
    if holderVal > 0:
        for i in pieces:
            print(index)
            index+=1
            if i['pieceID'] == holderVal:
                team = i
                break
        return team, index-1
    else:
        team = 'No piece'
        return team, -1


def makeImage(pos):
    #This is me using stuff i dont know but try to make them work
    size = (100, 100)
    image = pygame.Surface(size, pygame.SRCALPHA)
    other_image = pygame.Surface(size)
    pygame.draw.rect(image, lightblue, image.get_rect(), 10)
    display.blit(image, (pos[0], pos[1]))

def outputPos():
    with open(('PositionHistory.json'), 'w') as f:
        json.dump(posHistory, f, indent=2)



def addPosition(pos):
    #To write out the positions, make a dict and then add a list to the dict called positions
    #then add all the positions to the it and then dump it out to json 
    #for refernce, look at makingData.py or visit
    #'https://stackabuse.com/reading-and-writing-json-to-a-file-in-python/'
    x, y = pos[0], pos[1]
    pieceNumber, rowNumber = int((x/100)-1), int((y/100)-1)
    #new list will hold all the pices in the correct row
    newList = grid[rowNumber]
    holderVal = newList[pieceNumber]
    team = ''
    if holderVal > 0:
        for i in pieces:
            if i['pieceID'] == holderVal:
                currentPiece = i
                posHistory['postions'].append(currentPiece)
                outputPos()

def checkPreviousPiece():
    positions = posHistory['postions']
    previousPiece = positions[0]
    return previousPiece

def idkwhattocallthisfunction(isSelec, currentTeam, selectedTeam):
    pos = pygame.mouse.get_pos()
    pos = round_pos(pos)
    posValid = validatePos(pos)
    isPieceTrue = checkForPiece(pos)
    if posValid == True and isPieceTrue == True:
        if isSelec == False:
            addPosition(pos)
            makeImage(pos)
            isSelec = True
            currentPiece, index = checkTeam(pos)
            currentTeam = currentPiece['team']
            print(currentTeam, index)
        else:
            previousPiece = checkPreviousPiece()
            previousTeam = previousPiece['team']
            if previousTeam == currentTeam:
                isSelec = False
                idkwhattocallthisfunction()
        if selectedTeam == currentTeam:
            print('ya')
    elif isPieceTrue == False:
        print('No piece found')
    elif posValid == False:
        print('outside of boundries')

#The main loop
def game_loop():
    isRunning = True
    display.fill(gray)
    draw_grid(grid)
    import_data(grid)
    draw_images(pieces)
    #isSelec is a variable that will say if there is a piece selected
    isSelec = False
    #pos is [x, y, length, breadth]
    currentTeam, selectedTeam = '', ''
    while isRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            mouseClick = list(pygame.mouse.get_pressed())
            if mouseClick[0] == 1:
                idkwhattocallthisfunction(isSelec, currentTeam, selectedTeam)

                

        pygame.display.update()

grid = make_grid(8, 8)
game_loop()
pygame.quit()
