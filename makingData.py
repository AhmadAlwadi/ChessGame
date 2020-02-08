import json

types = ["Rook", "Knight", "Bishop", "Queen", "King", "Bishop", "Knight", "Rook",
"Pawn", "Pawn", "Pawn", "Pawn", "Pawn", "Pawn", "Pawn", "Pawn"]

data = {}
data['pieces'] = []

for i in range(0,16):
    #calculating the position 
    #calculating x
    x = (i + 1)* 100 
    #calculating y 
    y = 100
    if x > 800:
        x -= 800  #-- because there are only 8 pices horixontally
        y = 200 #-- because this means that now we are talking about the pawn pieces 
    position = [x, y]
    #print(position)
    #'pos':position
    #pieceID will be used to make the grid self aware and to use the right image for the right piece
    current_piece = {'type' : types[i], 'pos':position, 'team':'Black', 'pieceID':i+1}
    data['pieces'].append(current_piece)

counter = 0 
for i in range(48,64):
    #calculating the position 
    #calculating x
    x = (counter + 1)* 100 
    #calculating y 
    y = 800
    if x > 800:
        x -= 800  #-- because there are only 8 pices horixontally
        y = 700 #-- because this means that now we are talking about the pawn pieces 
    position = [x, y]
    current_piece = {'type' : types[counter], 'pos':position, 'team':'White', 'pieceID':i+1}
    data['pieces'].append(current_piece)
    counter += 1 

with open (('pieces.json'), 'w') as f:
    json.dump(data, f, indent=3)